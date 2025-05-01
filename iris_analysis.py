# iris_analysis.py
# Analyzing the Iris Dataset using Pandas and Visualizing with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load and Explore the Dataset
# -------------------------------

# Load dataset from online source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first few rows
print("\nFirst five rows:")
print(df.head())

# Dataset structure and types
print("\nData types and null values:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------
# 2. Basic Data Analysis
# -------------------------------

print("\nBasic statistics:")
print(df.describe())

print("\nColumn-wise Mean:\n", df.mean(numeric_only=True))
print("\nColumn-wise Median:\n", df.median(numeric_only=True))
print("\nColumn-wise Standard Deviation:\n", df.std(numeric_only=True))

# Group by species and calculate mean
grouped_means = df.groupby('species').mean(numeric_only=True)
print("\nGroup-wise Means (by species):\n", grouped_means)

# Observations from data
print("\nObservations:")
print("- Setosa has significantly smaller petal length and width.")
print("- Virginica has the highest average sepal and petal measurements.")
print("- Petal measurements are more useful than sepal measurements for distinguishing species.")

# -------------------------------
# 3. Data Visualization
# -------------------------------

# 1. Line Chart – Simulated Trend using sample index
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal_length'], label='Sepal Length', color='blue')
plt.plot(df.index, df['petal_length'], label='Petal Length', color='green')
plt.title('Simulated Trend of Sepal and Petal Length Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart – Average Petal Length per Species
plt.figure(figsize=(6, 4))
df.groupby('species')['petal_length'].mean().plot(kind='bar', color='orchid', edgecolor='black')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.grid(axis='y')
plt.xticks(rotation=0)
plt.show()

# 3. Histogram – Sepal Width Distribution
plt.figure(figsize=(7, 4))
plt.hist(df['sepal_width'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 4. Scatter Plot – Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], label=species)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()
