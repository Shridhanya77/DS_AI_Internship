import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler

data={
      "Age":[22,25,30,35,40,45,50],
      "Salary":[20000,25000,30000,35000,40000,45000,50000]
      }

df=pd.DataFrame(data)

standard_scaler=StandardScaler()
df_standardized=pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
    )

minmax_scaler=MinMaxScaler()
df_normalized=pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
    )

plt.figure()
plt.hist(df['Salary'],bins=5,edgecolor='black')
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_standardized['Salary'],bins=5,edgecolor='black')
plt.title("Salary After Standardization")
plt.xlabel("Standardized salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_normalized['Salary'],bins=5,edgecolor='black')
plt.title("Salary After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()

print("Original Salary:\n", df['Salary'])
print("\nStandardized Salary:\n", df_standardized['Salary'])
print("\nNormalized Salary:\n", df_normalized['Salary'])
