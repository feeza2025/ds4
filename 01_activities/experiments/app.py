import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Diabetes Risk Screening Tool",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Load model
# -----------------------------
MODEL_DIR = Path("./model_artifacts")
model_path = MODEL_DIR / "diabetes_risk_model.pkl"
feature_path = MODEL_DIR / "feature_columns.pkl"

if not model_path.exists() or not feature_path.exists():
    st.error("Model files not found. Please run train_diabetes_model.py first.")
    st.stop()

model = joblib.load(model_path)
feature_columns = joblib.load(feature_path)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1f4e79;
        margin-bottom: 0.2rem;
    }
    .subtext {
        font-size: 1rem;
        color: #555;
        margin-bottom: 1rem;
    }
    .card {
        background-color: #f7f9fc;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .risk-high {
        padding: 0.8rem;
        border-radius: 10px;
        background-color: #fde2e1;
        color: #8b1e1e;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
    }
    .risk-moderate {
        padding: 0.8rem;
        border-radius: 10px;
        background-color: #fff4d6;
        color: #8a6d1d;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
    }
    .risk-low {
        padding: 0.8rem;
        border-radius: 10px;
        background-color: #dff3e4;
        color: #1f6b3b;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">🩺 Diabetes Risk Screening Tool</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtext">Enter age, sex, and symptoms to estimate diabetes risk based on the trained model.</div>',
    unsafe_allow_html=True
)

st.info(
    "This tool is for educational screening support only. It does not replace professional medical advice or diagnosis."
)

# -----------------------------
# Helpers
# -----------------------------
def symptom_checkbox(label):
    return "Yes" if st.checkbox(label) else "No"

def classify_risk(probability):
    if probability < 0.30:
        return "Low Risk", "risk-low"
    elif probability < 0.60:
        return "Moderate Risk", "risk-moderate"
    else:
        return "High Risk", "risk-high"

# -----------------------------
# Layout
# -----------------------------
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.markdown("### Patient Information")
    age = st.number_input("Age", min_value=1, max_value=120, value=45, step=1)
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

    st.markdown("### Symptoms")
    c1, c2 = st.columns(2)

    with c1:
        polyuria = symptom_checkbox("Polyuria (frequent urination)")
        polydipsia = symptom_checkbox("Polydipsia (excessive thirst)")
        sudden_weight_loss = symptom_checkbox("Sudden weight loss")
        weakness = symptom_checkbox("Weakness")
        polyphagia = symptom_checkbox("Polyphagia (increased hunger)")
        genital_thrush = symptom_checkbox("Genital thrush")
        visual_blurring = symptom_checkbox("Visual blurring")

    with c2:
        itching = symptom_checkbox("Itching")
        irritability = symptom_checkbox("Irritability")
        delayed_healing = symptom_checkbox("Delayed healing")
        partial_paresis = symptom_checkbox("Partial paresis")
        muscle_stiffness = symptom_checkbox("Muscle stiffness")
        alopecia = symptom_checkbox("Alopecia")
        obesity = symptom_checkbox("Obesity")

# -----------------------------
# Build input
# -----------------------------
input_dict = {
    "Age": age,
    "Gender": gender,
    "Polyuria": polyuria,
    "Polydipsia": polydipsia,
    "sudden weight loss": sudden_weight_loss,
    "weakness": weakness,
    "Polyphagia": polyphagia,
    "Genital thrush": genital_thrush,
    "visual blurring": visual_blurring,
    "Itching": itching,
    "Irritability": irritability,
    "delayed healing": delayed_healing,
    "partial paresis": partial_paresis,
    "muscle stiffness": muscle_stiffness,
    "Alopecia": alopecia,
    "Obesity": obesity
}

input_df = pd.DataFrame([input_dict])

for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = None

input_df = input_df[feature_columns]

selected_symptoms = [
    label for label, value in input_dict.items()
    if value == "Yes" and label not in ["Gender"]
]

# -----------------------------
# Prediction
# -----------------------------
with right_col:
    st.markdown("### Screening Result")

    if st.button("Predict Diabetes Risk", use_container_width=True):
        probability = model.predict_proba(input_df)[0][1]
        risk_label, risk_class = classify_risk(probability)

        st.markdown(
            f'<div class="{risk_class}">{risk_label}</div>',
            unsafe_allow_html=True
        )

        st.metric("Predicted Probability", f"{probability * 100:.1f}%")
        st.progress(int(probability * 100))

        st.markdown("### Interpretation")
        if risk_label == "High Risk":
            st.error(
                "This person appears to have a high predicted risk of diabetes based on the symptoms entered."
            )
        elif risk_label == "Moderate Risk":
            st.warning(
                "This person appears to have a moderate predicted risk of diabetes and may benefit from follow-up screening."
            )
        else:
            st.success(
                "This person appears to have a lower predicted risk of diabetes based on the symptoms entered."
            )

        st.markdown("### Screening Summary")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Symptoms selected:** {len(selected_symptoms)}")

        if selected_symptoms:
            st.write(", ".join(selected_symptoms))
        else:
            st.write("No symptoms selected.")

        st.markdown("### Public Health Message")
        st.info(
            "Early detection of diabetes risk can support prevention through lifestyle changes, clinical follow-up, and timely care."
        )

        st.download_button(
            label="Download Screening Data as CSV",
            data=input_df.to_csv(index=False),
            file_name="diabetes_screening_input.csv",
            mime="text/csv",
            use_container_width=True
        )

with st.expander("Show entered data"):
    st.dataframe(input_df, use_container_width=True)