# 💼 Employee Salary Prediction App

This project is a **Machine Learning–powered Streamlit web app** that predicts employee salaries based on their demographic and professional attributes such as age, gender, education level, job title, and years of experience.

---


## 📊 Features

- Predicts **annual salary** using a **Random Forest Regressor**
- Interactive **Streamlit UI**
- Live **data input via sidebar**
- Clean dashboard with:
  - Metric cards for user summary
  - Salary prediction bar chart
- ⚙️ Model trained on a real-world salary dataset
- 🧠 ML evaluation & comparison of 8+ models (code included)

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Label Encoding
2. Model Training (Random Forest selected after evaluation)
3. Outlier Handling using IQR
4. R² Score Comparison Visualization
5. Streamlit Deployment

---

## 📦 Tech Stack

| Component         | Library       |
|------------------|---------------|
| Machine Learning | `scikit-learn`, `joblib` |
| Web App          | `streamlit`   |
| Visualization    | `matplotlib`, `seaborn` |
| Data             | Real-world employee salary dataset |

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/employee-salary-predictor.git
cd employee-salary-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── app.py                        # Streamlit app
├── salary_predictor_rf_model.pkl  # Trained model
├── encoder_gender.pkl           # Gender encoder
├── encoder_edu.pkl              # Education encoder
├── encoder_job.pkl              # Job Title encoder
├── Salary_Data.csv              # Original dataset
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## 🧪 Sample Input

| Field            | Example               |
|------------------|------------------------|
| Age              | 30                    |
| Gender           | Female                |
| Education Level  | Bachelor's Degree     |
| Job Title        | Account Manager       |
| Years of Exp     | 5.0                   |

---

## ✅ Example Output

> 💰 Estimated Annual Salary: **$98,450.00**

With summary card + salary bar chart.

---

## 📌 Future Improvements

- PDF/CSV report export
- Streamlit Cloud deployment
- Model retraining from UI
- User login and prediction history

---

## 👨‍💻 Developed by

**Aman**  
> 📬 Feel free to connect or suggest features!

---
