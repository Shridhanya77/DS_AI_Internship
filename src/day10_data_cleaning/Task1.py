import pandas as pd

# STEP 1 — Load the dataset
df = pd.read_csv("customer_orders.csv")

# STEP 2 — Print shape BEFORE cleaning
print("Shape before cleaning:", df.shape)

# STEP 3 — Report missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 4 — Fill missing NUMERIC values with MEDIAN
# Select only numeric columns
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# STEP 5 — Remove duplicate rows (exact matches across all columns)
df = df.drop_duplicates()

# STEP 6 — Print shape AFTER cleaning
print("Shape after cleaning:", df.shape)

# (Optional) Save cleaned dataset
df.to_csv("customer_orders_cleaned.csv", index=False)

print("\nCleaned dataset preview:")
print(df.head())
