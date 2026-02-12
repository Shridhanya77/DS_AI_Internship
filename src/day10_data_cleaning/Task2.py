import pandas as pd


data = {
    "Price": ["$100.50", "$200.75", "$50.00", "$300.25"],
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]
}


df = pd.DataFrame(data)


print("Initial data types:\n", df.dtypes, "\n")



df["Price"] = df["Price"].str.replace(r"\$", "", regex=True).astype(float)


df["Date"] = pd.to_datetime(df["Date"])

print("Cleaned DataFrame:\n", df, "\n")
print("Final data types:\n", df.dtypes)
