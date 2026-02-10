total_bill=float(input("Enter the total bill amount : "))
total_num=int(input("Enter the total no of people : "))

each_bill=total_bill/total_num
print(f"Total bill is {total_bill}. Each person should pay {each_bill:.2f}  ")

