import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/processed/features.csv")

X = df.drop("deployment_status", axis=1)

model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly_score"] = model.fit_predict(X)

df["anomaly"] = df["anomaly_score"].apply(lambda x: 1 if x == -1 else 0)

df.to_csv("results/sample_predictions.csv", index=False)

print("✅ Anomaly detection completed")
