import pandas as pd


data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles ", "CHICAGO"]
}

df = pd.DataFrame(data)


print("Unique Locations before cleaning:")
print(df["Location"].unique(), "\n")


df["Location"] = df["Location"].str.strip().str.title()


print("Unique Locations after cleaning:")
print(df["Location"].unique(), "\n")


print("Cleaned DataFrame:\n", df)
