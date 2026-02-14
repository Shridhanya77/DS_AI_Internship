import matplotlib.pyplot as plt

categories=['Electronics','Clothing','Home']
values=[300,450,200]

months=[1,2,3,4,5]
sales_trend=[200,300,280,500,500]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.bar(categories,values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.subplot(1,2,2)
plt.plot(months,sales_trend,marker='o')
plt.title("sales Trend over Time")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()