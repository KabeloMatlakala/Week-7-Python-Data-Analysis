# Week-7-Python-Data-Analysis

# Iris Dataset Analysis and Visualization

This project performs data loading, exploration, analysis, and visualization on the classic **Iris dataset** using Python's `pandas` and `matplotlib` libraries.

## 📊 Project Overview

The goal of this project is to:
- Load and explore the Iris dataset.
- Compute basic statistics and group-wise analysis.
- Visualize the data using different types of plots.
- Provide insights based on the analysis.

## 🛠️ Tools & Libraries

- Python 3.11+
- pandas
- matplotlib
- seaborn *(optional for enhanced plots)*
- Jupyter Notebook or VS Code

## 📁 Files Included

- `iris_analysis.py` – Main Python script for analysis.
- *(or)* `iris_analysis.ipynb` – Jupyter Notebook version with code and markdown explanations.
- `README.md` – Project overview and instructions.

## 🔍 Features

### 1. Data Loading & Exploration
- Load dataset from a remote CSV file.
- Inspect dataset structure, types, and missing values.

### 2. Basic Analysis
- Compute mean, median, standard deviation.
- Group data by species and calculate group-wise statistics.
- Summary of insights observed from the data.

### 3. Data Visualization
Four different visualizations were created to explore and communicate patterns:
- 📈 **Line Chart**: Simulated trend using sample index.
- 📊 **Bar Chart**: Average petal length per species.
- 📉 **Histogram**: Distribution of sepal width.
- 🔵 **Scatter Plot**: Sepal length vs. petal length by species.

Each plot includes:
- Titles
- Axis labels
- Legends (where appropriate)
- Grid lines for readability

## ✅ How to Run

1. Clone the repository or download the files.
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn notebook
   ```
3. Open iris_analysis.py in VS Code, or run iris_analysis.ipynb in Jupyter Notebook.
4. Execute the script or notebook cells to see outputs and plots.

## 📌 Observations
- Setosa has significantly smaller petal length and width than other species.
- Virginica has the largest measurements on average.
- Petal measurements are more useful than sepal measurements for classification.
- The dataset is clean with no missing values.

## 📚 Dataset Source
Iris dataset loaded from Seaborn GitHub, originally from the UCI Machine Learning Repository.
