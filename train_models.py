import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create models folder if it doesn't existp
import os
if not os.path.exists("Multiple_Disease_prediction_usingML-main/models"):
    os.makedirs("Multiple_Disease_prediction_usingML-main/modezls")

# ---------- Train Heart Disease Model ----------
print("🔥 Training Heart Disease Model...")
heart_df = pd.read_csv("Multiple_Disease_prediction_usingML-main/datasets/heart.csv")
X_heart = heart_df.drop(columns=['target'])
y_heart = heart_df['target']

X_train, X_test, y_train, y_test = train_test_split(X_heart, y_heart, test_size=0.2, random_state=42)
scaler_heart = StandardScaler()
X_train_scaled = scaler_heart.fit_transform(X_train)
X_test_scaled = scaler_heart.transform(X_test)

heart_model = RandomForestClassifier(n_estimators=300, max_depth=12, random_state=42)
heart_model.fit(X_train_scaled, y_train)

# Evaluate
heart_pred = heart_model.predict(X_test_scaled)
heart_accuracy = accuracy_score(y_test, heart_pred)
print(f"✅ Heart Model Accuracy: {heart_accuracy:.4f}")

# Save model & scaler
joblib.dump(heart_model, "Multiple_Disease_prediction_usingML-main/models/heart.pkl")
joblib.dump(scaler_heart, "Multiple_Disease_prediction_usingML-main/models/scaler_heart.pkl")


print("\n🎉✅ All models trained and saved successfully!")
