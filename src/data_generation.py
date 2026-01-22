import pandas as pd
import numpy as np

np.random.seed(42)

NUM_RECORDS = 1000

data = {
    "deployment_id": range(1, NUM_RECORDS + 1),
    "cpu_usage": np.random.normal(60, 15, NUM_RECORDS).clip(5, 100),
    "memory_usage": np.random.normal(65, 15, NUM_RECORDS).clip(5, 100),
    "latency_ms": np.random.normal(200, 60, NUM_RECORDS).clip(50, 600),
    "restart_count": np.random.poisson(1.2, NUM_RECORDS),
    "error_rate": np.random.beta(2, 8, NUM_RECORDS)
}

df = pd.DataFrame(data)

# Failure labeling logic (realistic DevOps rules)
df["deployment_status"] = (
    (df["cpu_usage"] > 80) |
    (df["memory_usage"] > 85) |
    (df["error_rate"] > 0.25) |
    (df["restart_count"] > 3)
).astype(int)

df.to_csv("data/raw/synthetic_deployment_logs.csv", index=False)

print("✅ Synthetic deployment logs generated successfully")
