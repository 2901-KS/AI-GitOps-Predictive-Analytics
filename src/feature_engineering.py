import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/raw/synthetic_deployment_logs.csv")

features = [
    "cpu_usage",
    "memory_usage",
    "latency_ms",
    "restart_count",
    "error_rate"
]

X = df[features]
y = df["deployment_status"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

processed_df = pd.DataFrame(X_scaled, columns=features)
processed_df["deployment_status"] = y

processed_df.to_csv("data/processed/features.csv", index=False)

print("✅ Feature engineering completed")
