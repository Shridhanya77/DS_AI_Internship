import pandas as pd

usernames=pd.Series(['Alice','bOB','Charlie_Data','daisy'])
print("Original Username Series : ")
print(usernames)

cleaned_usernames=usernames.str.strip().str.lower()

print("\nCleaned Usernames Series : ")
print(cleaned_usernames)

contains_a=cleaned_usernames.str.contains('a')

print("\nContains letter 'a' : ")
print(contains_a)