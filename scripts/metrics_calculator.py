import pandas as pd
from datetime import timedelta
import numpy as np

# Load data
users = pd.read_csv("../data/users.csv", parse_dates=["registration_date"])
sessions = pd.read_csv("../data/sessions.csv", parse_dates=["session_date"])
purchases = pd.read_csv("../data/purchases.csv", parse_dates=["purchase_date"])

### --- DAU, WAU, MAU --- ###
dau = sessions.groupby("session_date")["user_id"].nunique().reset_index(name="DAU")

sessions["week"] = sessions["session_date"] - pd.to_timedelta(sessions["session_date"].dt.dayofweek, unit='D')
wau = sessions.groupby("week")["user_id"].nunique().reset_index(name="WAU")

sessions["month"] = sessions["session_date"].dt.to_period("M")
mau = sessions.groupby("month")["user_id"].nunique().reset_index(name="MAU")

### --- ARPU --- ###
total_revenue = purchases["amount_usd"].sum()
num_users = users["user_id"].nunique()
arpu = total_revenue / num_users

### --- ARPDAU --- ###
merged = pd.merge(sessions, purchases, how="left", left_on=["user_id", "session_date"], right_on=["user_id", "purchase_date"])
revenue_by_day = merged.groupby("session_date")["amount_usd"].sum().reset_index()
revenue_by_day = pd.merge(revenue_by_day, dau, on="session_date", how="left")
revenue_by_day["ARPDAU"] = revenue_by_day["amount_usd"] / revenue_by_day["DAU"]
revenue_by_day.fillna(0, inplace=True)

### --- Retention (D1, D7, D30) --- ###
retention = {"D1": [], "D7": [], "D30": []}

for days in [1, 7, 30]:
    label = f"D{days}"
    retained = 0
    total = 0
    for _, row in users.iterrows():
        user_id = row["user_id"]
        reg_date = row["registration_date"]
        followup_date = reg_date + timedelta(days=days)
        total += 1
        if user_id in sessions[sessions["session_date"] == followup_date]["user_id"].values:
            retained += 1
    retention[label] = round(retained / total * 100, 2)

### --- Print Results --- ###
print("\n🔹 DAU (first 5 days):\n", dau.head())
print("\n🔹 WAU (first 5 weeks):\n", wau.head())
print("\n🔹 MAU:\n", mau)

print(f"\n🔹 ARPU: ${arpu:.2f}")
print("\n🔹 ARPDAU (first 5 days):\n", revenue_by_day[["session_date", "ARPDAU"]].head())

print("\n🔹 Retention Rates:")
for k, v in retention.items():
    print(f"{k} Retention: {v}%")
