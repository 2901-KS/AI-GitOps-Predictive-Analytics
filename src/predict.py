import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/processed/features.csv")

X = df.drop("deployment_status", axis=1)
y = df["deployment_status"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

feature_importance = pd.Series(
    model.coef_[0],
    index=X.columns
).sort_values(ascending=False)

feature_importance.to_csv("results/feature_importance.csv")

print("\nTop factors contributing to deployment risk:")
print(feature_importance.head())

test_cases = [
    {
    "name": "Low Risk Deployment",
    "cpu_usage": -1.0,
    "memory_usage": -1.0,
    "latency_ms": -0.8,
    "restart_count": -0.5,
    "error_rate": -0.8
},
    {
        "name": "Medium Risk Deployment",
        "cpu_usage": 0.3,
        "memory_usage": 0.5,
        "latency_ms": 0.3,
        "restart_count": 1.0,
        "error_rate": 0.10
    },
    {
        "name": "High Risk Deployment",
        "cpu_usage": 1.2,
        "memory_usage": 1.1,
        "latency_ms": 0.9,
        "restart_count": 2.5,
        "error_rate": 1.3
    }
]

print("\nDeployment Risk Evaluation:\n")

for case in test_cases:
    case_df = pd.DataFrame([{
        "cpu_usage": case["cpu_usage"],
        "memory_usage": case["memory_usage"],
        "latency_ms": case["latency_ms"],
        "restart_count": case["restart_count"],
        "error_rate": case["error_rate"]
    }])

    prob = model.predict_proba(case_df)[0][1]

    if prob > 0.85:
        risk = "HIGH"
        action = "BLOCK deployment and alert DevOps team"
    elif prob > 0.6:
        risk = "MEDIUM"
        action = "Deploy with enhanced monitoring"
    else:
        risk = "LOW"
        action = "Safe to deploy"

    print(f"Scenario: {case['name']}")
    print(f"Failure Probability: {round(prob, 2)}")
    print(f"Risk Level: {risk}")
    print(f"Recommended Action: {action}")
    print("-" * 50)
