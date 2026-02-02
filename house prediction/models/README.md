# 🏠 Bengaluru House Price Prediction

## 📌 Overview
This project predicts house prices in Bengaluru using machine learning.  
It applies data preprocessing, feature engineering, regression modeling, and model persistence to estimate property prices based on key housing attributes.

---

## 🎯 Objective
To build an end-to-end machine learning pipeline that accurately predicts house prices using historical Bengaluru housing data.

---

## 📊 Dataset
- **Source:** Kaggle – Bengaluru House Price Dataset
- **Target:** `price` (in lakhs)
- **Features:**  
  `total_sqft`, `size (BHK)`, `bath`, `balcony`, `location`, `availability`

---

## ⚙️ Technologies Used
- Python
- NumPy, Pandas
- Scikit-learn
- Joblib
- VS Code

---

## 🛠 Methodology
- Data cleaning and feature engineering
- Scaling numerical features and encoding categorical features
- Model training using **Linear Regression**
- Model evaluation using **MAE** and **R² score**
- Model saving and reuse using `joblib`

---

## 📈 Results
- **MAE:** ~18 Lakhs  
- **R² Score:** ~0.84  
- The model explains around **84% of price variance**

---

## 🏠 Sample Prediction
**Input:** 2 BHK, 1200 sqft, Whitefield  
**Predicted Price:** ~₹72 Lakhs

---

## ▶️ How to Run
```bash
pip install numpy pandas scikit-learn joblib
python house_price_prediction.py
