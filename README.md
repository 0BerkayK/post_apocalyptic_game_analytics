# 🧟‍♂️ Post-Apocalyptic Survival Game Data Analysis Dashboard

Bu proje, bir mobil hayatta kalma oyununa ait kullanıcı davranışları, monetizasyon ve A/B test performanslarının analiz edildiği uçtan uca bir veri analitiği çözümüdür. Projede kullanılan veriler simülasyonla oluşturulmuş olup, oyuncu davranışları, gelir modelleri ve kullanıcı kazanım kanallarının performansı Tableau ile görselleştirilmiştir.

🎯 Hedef
Bu proje, mobil oyun şirketlerinde:

Oyun içi kullanıcı davranışlarını anlamak

Gelir artırıcı stratejileri belirlemek

Hedefli kullanıcı edinim kampanyaları planlamak

A/B testleriyle ürün kararlarını desteklemek

amaçlarıyla kullanılabilecek analitik modellerin örneklemesini sunar.

🧰 Kullanılan Teknolojiler
Python (Pandas, NumPy)

Tableau Desktop (Dashboard)

Jupyter Notebook (Veri analizi & EDA)

Simülasyon verisi (gerçeğe uygun kurgulanmış veri setleri)

---

## 📊 Dashboard Özeti

Dashboard, aşağıdaki 5 temel metrik sayfasından oluşmaktadır:

### 1. **Retention Metrics**
- D1, D3, D7 kullanıcı tutma oranları
- Kanal bazlı retention karşılaştırması
- Kullanıcıların zaman içindeki bağlılık trendi

### 2. **Engagement Metrics**
- DAU, WAU, MAU (Günlük/Haftalık/Aylık Aktif Kullanıcı)
- Avg. Sessions per User (Kullanıcı başına ortalama oturum)
- Kullanıcı etkileşim süreleri

### 3. **Monetization Metrics**
- ARPU (Average Revenue Per User)
- ARPDAU (Average Revenue Per Daily Active User)
- Paying Users analizi

### 4. **Attribution Metrics**
- Kanal bazlı kullanıcı sayısı ve gelir katkısı
- Kanal başına retention analizi (D1-D7)
- Kullanıcı edinim performansı

### 5. **A/B Test Analysis**
- A/B grubu click-through oranları
- Gelir karşılaştırması
- Conversion ve kullanıcı başına gelir (RPU) farkları

---
📊 Dashboard'u İncele

[https://public.tableau.com/views/Post-ApocalypticGameKPIDashboard/Post-ApocalypticGameKPIDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]

## 📁 Klasör Yapısı

```bash
├── data/
│   ├── users.csv
│   ├── sessions.csv
│   ├── purchases.csv
│   ├── attribution.csv
│   └── ab_test.csv
├── dashboards/
│   └── KPI_Dashboard.twbx
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_KPI_Tracking.ipynb
│   ├── 03_Attribution_Analysis.ipynb
│   └── 04_AB_Test_Analysis.ipynb
├── scripts/
│   ├── data_simulation.py
│   ├── metrics_calculator.py
│   └── ab_test_helper.py
├── requirements.txt
└── README.md
