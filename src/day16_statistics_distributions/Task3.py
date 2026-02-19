import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

original_data=np.random.exponential(scale=50000,size=10000)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(original_data,kde=True)
plt.title("Original Data (Right-Skewed)")

sample_means=[]

for i in range(1000):
    sample=np.random.choice(original_data,size=30)
    sample_mean=np.mean(sample)
    sample_means.append(sample_mean)
    
sample_means=np.array(sample_means)

plt.subplot(1,2,2)
sns.histplot(sample_means,kde=True)
plt.title("Distribution of Sample Means (n=30)")

plt.tight_layout()
plt.show()

print("Original Data Mean : ",round(np.mean(original_data),2))
print("Mean of Sample Means : ",round(np.mean(sample_means),2))
print("Original Data Std Dev : ",round(np.std(original_data),2))
print("Sample Means Standard Deviation(Standard Error):",round(np.std(sample_means),2))