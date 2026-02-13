purchases={
    "Alice":50,
    "Bob":200,
    "Charlie":20
}

for name,amount in purchases.items():
    print(f"{name} spent $ {amount}")

    print("Total Purchases",len(purchases))
    print("Customer names",purchases.keys())
    print("customer values",purchases.values())

    purchases.update()


    top_customer=max(purchases,key=purchases.get)
    print("Top spending Customer",top_customer)