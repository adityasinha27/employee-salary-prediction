import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model and encoders
model = joblib.load("salary_predictor_rf_model.pkl")
le_gender = joblib.load("encoder_gender.pkl")
le_edu = joblib.load("encoder_edu.pkl")
le_job = joblib.load("encoder_job.pkl")

# --- UI Setup ---
st.set_page_config(page_title="Employee Salary Predictor", layout="centered")
st.title("💼 Employee Salary Prediction")
st.markdown("Use this tool to estimate an employee's salary based on their profile.")

# --- Sidebar Inputs ---
st.sidebar.header("🧾 Enter Employee Details")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", le_gender.classes_)
education = st.sidebar.selectbox("Education Level", le_edu.classes_)
job_title = st.sidebar.selectbox("Job Title", le_job.classes_)
experience = st.sidebar.slider("Years of Experience", 0.0, 40.0, 5.0, step=0.5)

if st.sidebar.button("🔍 Predict Salary"):
    # Encode input features
    gender_encoded = le_gender.transform([gender])[0]
    edu_encoded = le_edu.transform([education])[0]
    job_encoded = le_job.transform([job_title])[0]
    features = np.array([[age, gender_encoded, edu_encoded, job_encoded, experience]])

    # Prediction
    predicted_salary = model.predict(features)[0]

    # --- Results Layout ---
    st.markdown("## 🧾 Employee Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Age", age)
        st.metric("Gender", gender)
        st.metric("Experience", f"{experience:.1f} years")
    with col2:
        st.metric("Education", education)
        st.metric("Job Title", job_title)
        st.metric("Predicted Salary", f"${predicted_salary:,.2f}")

    # --- Visualization using matplotlib ---
    st.markdown("### 📈 Salary Prediction Visualization")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(["Predicted Salary"], [predicted_salary], color="skyblue")
    ax.set_ylabel("Salary ($)")
    ax.set_ylim(0, predicted_salary * 1.2)
    ax.set_title("📊 Predicted Salary")
    st.pyplot(fig)

    # --- Final Result ---
    st.success(f"💰 Estimated Annual Salary: **${predicted_salary:,.2f}**")

# Footer
st.markdown("---")
st.markdown(
    "<center><small>🔧 Built with Streamlit • Random Forest Model • Developed by Aman</small></center>",
    unsafe_allow_html=True
)
