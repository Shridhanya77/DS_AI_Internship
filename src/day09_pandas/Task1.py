import pandas as pd

products=pd.Series([700,150,300],index=(['Laptop','Mouse','Keyboard']))

print("Full product series : ")
print(products)

print("\nPrice of Laptop")
print(products['Laptop'])

print("First Two products")
print(products.iloc[0:2])