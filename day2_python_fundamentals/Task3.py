item_name=input("Enter a item name : ")
quantity=int(input("Enter quantity : "))
price=float(input("Enter the price : "))
in_stock_input=input("Is the item in stock? (True/false)")
in_stock=in_stock_input.lower()

print("Item: " ,item_name, ",Quantity: " ,quantity, ",Price: " ,price, ",Available" ,in_stock)

total_cost=quantity*price
print("Total cost:",total_cost)