import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

heights=np.random.normal(loc=170,scale=10,size=1000)
income=np.random.exponential(scale=50000,size=1000)
scores=100-np.random.exponential(scale=15,size=1000)
scores=np.clip(scores,0,100)

df=pd.DataFrame({
    "Heights (Normal)" : heights,
    "Income (Right-Skewed)" : income,
    "Scores (Left-Skewed)" : scores
    })

plt.figure(figsize=(18,5))

# Normal Distribution
plt.subplot(1,3,1)
sns.histplot(df["Heights (Normal)"],kde=True)
plt.title("Human Heights (Normal Distribution)")

# Right-Skewed Distribution
plt.subplot(1,3,2)
sns.histplot(df["Income (Right-Skewed)"],kde=True)
plt.title("Household Income (Right-Skewed)")

plt.subplot(1,3,3)
sns.histplot(df["Scores (Left-Skewed)"],kde=True)
plt.title("Easy Exam Scores (Left-Skewed)")

plt.tight_layout()
plt.show()

print("Mean vs Median Comparison")

for column in df.columns:
    mean=df[column].mean()
    median=df[column].median()
    
    print(f"{column}")
    print(f"Mean : {mean:.2f}")
    print(f"Median : {median:.2f}")
    
    if mean>median:
        print("Distribution :Right-Skewed")
    elif mean<median:
        print("Distribution : Left-Skewed")
    else:
        print("Distriibution : Normal (Symmetrical)")
        
    print("-"*40)