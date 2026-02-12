import pandas as pd

# ---------------- Example messy data ----------------
data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles ", "CHICAGO"]
}

df = pd.DataFrame(data)

# ---------------- Step 1: Check unique values before cleaning ----------------
print("Unique Locations before cleaning:")
print(df["Location"].unique(), "\n")

# ---------------- Step 2: Normalize text ----------------
# Remove leading/trailing spaces and standardize casing
df["Location"] = df["Location"].str.strip().str.title()

# ---------------- Step 3: Verify cleaned values ----------------
print("Unique Locations after cleaning:")
print(df["Location"].unique(), "\n")

# ---------------- Step 4: View cleaned DataFrame ----------------
print("Cleaned DataFrame:\n", df)
