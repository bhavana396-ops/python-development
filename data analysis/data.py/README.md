# Fitness Data Analysis using Pandas and Matplotlib

## Project Overview
This project performs Exploratory Data Analysis (EDA) on a fitness dataset using Python. 
It focuses on data cleaning, statistical analysis, and visualization to understand the 
relationship between workout duration, heart rate, and calories burned.

---

## Tech Stack
- Python
- Pandas
- Matplotlib

---

## Key Features
- Safe CSV file loading using OS path handling
- Data inspection using head(), info(), and describe()
- Missing value handling using mean imputation
- Statistical analysis of calories burned
- Visualizations:
  - Bar chart
  - Scatter plot
  - Heatmap
  - Histogram
- Outlier detection using the IQR method
- Outlier visualization using boxplots

---

## Insights and Observations
- Average calories burned increase with workout duration.
- Higher pulse rates are associated with higher calorie expenditure.
- Strong correlations exist between Duration, Calories, Pulse, and Maxpulse.
- Maxpulse values mostly follow a normal distribution with few extreme cases.
- Outliers detected in calories may represent high-intensity workouts or anomalies.
- Overall trends remain consistent despite the presence of outliers.

---

## How to Run the Project
```bash
pip install pandas matplotlib
cd data.py
python pylib.py
