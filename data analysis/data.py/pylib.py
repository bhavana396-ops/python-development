
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV safely

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.csv")

df = pd.read_csv(DATA_PATH)

#verifying loaded data
print("\nFirst 5 rows:")
print(df.head(7))
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
print("\nNumber of Rows and Columns")
print(df.shape)


# Handle missing values

print("\nMissing values per column:")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

# Basic analysis

avg_calories = df["Calories"].mean()
print(f"\nAverage Calories Burned: {avg_calories:.2f}")

duration_avg = df.groupby("Duration")["Calories"].mean()
print("\nAverage Calories by Duration:")
print(duration_avg)

# Visualization
# Bar chart
plt.figure(figsize=(8,5))
plt.bar(duration_avg.index, duration_avg.values,width=10)
plt.xlabel("Duration")
plt.ylabel("Average Calories")
plt.title("Average Calories Burned by Duration")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df["Pulse"], df["Calories"])
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.title("Pulse vs Calories")
plt.show()

# Heatmap
correlation = df.corr(numeric_only=True)

plt.figure()
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#Histogram
plt.figure()
plt.hist(df["Maxpulse"],bins=10)
plt.xlabel("Maxpulse")
plt.ylabel("Frequency")
plt.title("Frequency over Maxpulse")
plt.show()



# Outlier Detection 

def detect_outliers(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = dataframe[
        (dataframe[column] < lower_bound) |
        (dataframe[column] > upper_bound)
    ]

    print(f"\nOutliers detected in {column}:")
    print(outliers)

    return outliers


calorie_outliers = detect_outliers(df, "Calories")

# Outlier Visualization

def plot_outliers(dataframe, column):
    plt.figure()
    plt.boxplot(dataframe[column])
    plt.title(f"Boxplot of {column}")
    plt.ylabel(column)
    plt.show()


plot_outliers(df, "Calories")