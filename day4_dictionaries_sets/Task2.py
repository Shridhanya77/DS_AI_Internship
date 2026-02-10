raw_logs=["1D01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_users=set(raw_logs)
is_present="ID05" in unique_users
print("Raw logs :",raw_logs)
print("Unique_users:",unique_users)

print("Is 'ID05' in unique users?",is_present)
print("Count Comparison")
print("Total log entries :",len(raw_logs))
print("Unique users count :",len(unique_users))
