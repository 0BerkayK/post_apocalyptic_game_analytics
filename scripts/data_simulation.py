import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

# Config
NUM_USERS = 5000
START_DATE = datetime(2025, 5, 1)
END_DATE = datetime(2025, 7, 1)
DATE_RANGE = pd.date_range(START_DATE, END_DATE)

# Attribution sources
ACQUISITION_CHANNELS = ['Facebook Ads', 'Google Ads', 'TikTok Ads', 'Unity Ads']

# Create folders if not exist
os.makedirs("data", exist_ok=True)

### USERS ###
user_ids = [f"user_{i}" for i in range(1, NUM_USERS + 1)]
registration_dates = np.random.choice(DATE_RANGE, NUM_USERS)

users_df = pd.DataFrame({
    "user_id": user_ids,
    "registration_date": registration_dates
})
users_df.to_csv("../data/users.csv", index=False)

### ATTRIBUTION ###
attribution_df = pd.DataFrame({
    "user_id": user_ids,
    "acquisition_channel": np.random.choice(ACQUISITION_CHANNELS, NUM_USERS, p=[0.4, 0.3, 0.2, 0.1]),
    "install_date": registration_dates
})
attribution_df.to_csv("../data/attribution.csv", index=False)

### SESSIONS ###
sessions = []
for user_id, reg_date in zip(user_ids, registration_dates):
    num_sessions = np.random.poisson(15)
    for _ in range(num_sessions):
        reg_date = pd.to_datetime(reg_date)
        session_date = reg_date + timedelta(days=int(np.random.exponential(scale=10)))
        if session_date > END_DATE:
            continue
        session_length = max(1, int(np.random.exponential(scale=20)))  # minutes
        sessions.append([user_id, session_date.strftime("%Y-%m-%d"), session_length])

sessions_df = pd.DataFrame(sessions, columns=["user_id", "session_date", "session_length_minutes"])
sessions_df.to_csv("../data/sessions.csv", index=False)

### PURCHASES ###
purchases = []
for user_id in np.random.choice(user_ids, size=int(NUM_USERS * 0.3), replace=False):  # 30% monetizing users
    for _ in range(np.random.poisson(2)):
        purchase_date = users_df.loc[users_df.user_id == user_id, "registration_date"].values[0]
        purchase_date = pd.to_datetime(purchase_date) + timedelta(days=int(np.random.exponential(7)))
        if purchase_date > END_DATE:
            continue
        amount = round(np.random.exponential(5), 2)  # in USD
        purchases.append([user_id, purchase_date.strftime("%Y-%m-%d"), amount])

purchases_df = pd.DataFrame(purchases, columns=["user_id", "purchase_date", "amount_usd"])
purchases_df.to_csv("../data/purchases.csv", index=False)

### A/B TEST ###
ab_test_df = pd.DataFrame({
    "user_id": user_ids,
    "group": np.random.choice(["control", "treatment"], size=NUM_USERS)
})
ab_test_df["clicked_special_offer"] = ab_test_df["group"].apply(lambda x: int(np.random.rand() < (0.08 if x == "control" else 0.12)))
ab_test_df.to_csv("../data/ab_test.csv", index=False)
