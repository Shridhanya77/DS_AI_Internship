n=int(input("Enter number of customers"))
user_purchases={}
for i in range(n):
    name=input("Enter Customer name : ")
    amount=int(input(f"Enter purchase amount for {name} :"))
    user_purchases[name]=amount
    print("Customer purchase data :" ,user_purchases)

