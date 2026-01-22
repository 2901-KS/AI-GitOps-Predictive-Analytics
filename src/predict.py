import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/processed/features.csv")

X = df.drop("deployment_status", axis=1)
y = df["deployment_status"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# New deployment (example)
new_deployment = np.array([[1.2, 1.1, 0.9, 2.5, 1.3]])

prob = model.predict_proba(new_deployment)[0][1]

print("Failure Probability:", round(prob, 2))
print("Deployment Risk:", "HIGH" if prob > 0.6 else "LOW")
