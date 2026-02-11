import pandas as pd

marks=pd.Series([80,90,78],index=['Math','Physics','Chemistry'])

print(marks['Math'])
print(marks[['Math','Chemistry']])