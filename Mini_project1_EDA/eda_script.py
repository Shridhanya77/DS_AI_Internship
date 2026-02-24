"""
EDA Script for Customer Analytics Dataset
Generates visualizations and a dataset summary file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# 1. Load the dataset
# ------------------------------
df = pd.read_csv("customer_analytics.csv")   # make sure the file is in the same folder
print("✅ Data loaded successfully.")

# ------------------------------
# 2. Initial inspection (printed)
# ------------------------------
print("\n" + "="*50)
print("HEAD")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("INFO")
print("="*50)
df.info()

print("\n" + "="*50)
print("DESCRIBE")
print("="*50)
print(df.describe())

# ------------------------------
# 3. Data Cleaning
# ------------------------------
# Store missing values BEFORE cleaning for the summary
missing_before = df.isnull().sum()

# Fill missing values
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])
df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].median())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\n✅ Missing values filled, duplicates removed.")

# ------------------------------
# 4. Univariate Plots
# ------------------------------
# Histogram: Age
plt.figure()
plt.hist(df['Age'], bins=15, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_histogram.png")
plt.close()

# Bar chart: Gender
plt.figure()
df['Gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_bar.png")
plt.close()

# Histogram: AnnualIncome
plt.figure()
plt.hist(df['AnnualIncome'], bins=15, edgecolor='black')
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Frequency")
plt.savefig("income_histogram.png")
plt.close()

# ------------------------------
# 5. Bivariate Plots
# ------------------------------
# Scatter: Age vs SpendingScore
plt.figure()
plt.scatter(df['Age'], df['SpendingScore'])
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Age vs Spending Score")
plt.savefig("age_vs_spending.png")
plt.close()

# Boxplot: Gender vs SpendingScore
plt.figure()
df.boxplot(column='SpendingScore', by='Gender')
plt.title("Gender vs Spending Score")
plt.suptitle("")   # remove automatic suptitle
plt.savefig("gender_spending_box.png")
plt.close()

# ------------------------------
# 6. Correlation Heatmap
# ------------------------------
plt.figure(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

print("✅ All plots saved as PNG files.")

# ------------------------------
# 7. Generate Dataset Summary Text File
# ------------------------------
with open('dataset_summary.txt', 'w') as f:
    f.write("Dataset Summary\n")
    f.write("===============\n\n")
    f.write(f"Rows (after cleaning): {df.shape[0]}\n")
    f.write(f"Columns: {df.shape[1]}\n\n")
    f.write("Columns:\n")
    for col in df.columns:
        f.write(f" - {col}: {df[col].dtype}\n")
    f.write("\nMissing values BEFORE cleaning:\n")
    f.write(str(missing_before))
    f.write("\n\nMissing values AFTER cleaning:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\nBasic statistics (after cleaning):\n")
    f.write(df.describe().to_string())

print("✅ dataset_summary.txt created.")

print("\n🎉 EDA script completed successfully!")