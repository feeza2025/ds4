import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score


# -----------------------------
# 1. Load dataset
# -----------------------------
DATA_PATH = "02_src/diabetes_data_upload.csv"   # update if needed
MODEL_DIR = Path("./model_artifacts")
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Expected columns in the dataset:
# Age, Gender, Polyuria, Polydipsia, sudden weight loss, weakness,
# Polyphagia, Genital thrush, visual blurring, Itching, Irritability,
# delayed healing, partial paresis, muscle stiffness, Alopecia, Obesity, class

# -----------------------------
# 2. Basic cleanup
# -----------------------------
df.columns = [col.strip() for col in df.columns]

# Standardize text values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.strip()

# Target mapping
target_col = "class"
df[target_col] = df[target_col].replace({
    "Positive": 1,
    "Negative": 0
})

# -----------------------------
# 3. Define features
# -----------------------------
X = df.drop(columns=[target_col])
y = df[target_col]

categorical_features = [col for col in X.columns if X[col].dtype == "object"]
numeric_features = [col for col in X.columns if X[col].dtype != "object"]

# -----------------------------
# 4. Preprocessing
# -----------------------------
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# -----------------------------
# 5. Model pipeline
# -----------------------------
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

# -----------------------------
# 6. Train / test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# 7. Train model
# -----------------------------
model.fit(X_train, y_train)

# -----------------------------
# 8. Evaluate model
# -----------------------------
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("ROC-AUC :", round(roc_auc_score(y_test, y_prob), 4))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# 9. Save model and feature list
# -----------------------------
joblib.dump(model, MODEL_DIR / "diabetes_risk_model.pkl")
joblib.dump(list(X.columns), MODEL_DIR / "feature_columns.pkl")

print("\nModel saved to:", MODEL_DIR / "diabetes_risk_model.pkl")
print("Feature list saved to:", MODEL_DIR / "feature_columns.pkl")