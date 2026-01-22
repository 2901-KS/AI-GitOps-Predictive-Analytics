import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/processed/features.csv")

X = df.drop("deployment_status", axis=1)
y = df["deployment_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

with open("results/model_metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.2f}\n\n")
    f.write(classification_report(y_test, y_pred))

print("✅ Model trained successfully")
print("Accuracy:", round(accuracy, 2))
