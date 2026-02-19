import pandas as pd
import numpy as np

np.random.seed(42)

data=np.random.normal(loc=170,scale=10,size=1000)

data=pd.DataFrame({
    "Heights":data
    })

mu=data["Heights"].mean()
sigma=data["Heights"].std()

print("Mean (μ):",round(mu,2))
print("Standard Deviation (σ):",round(sigma,2))

data["z_score"]=(data["Heights"]-mu)/sigma

outliers=data[np.abs(data["z_score"])>3]

print("\nRows where |Z|>3 (Statistical Outliers):")
print(outliers)

print("\nTotal Outliers Found : ",len(outliers))
