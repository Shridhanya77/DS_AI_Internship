n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
print("% for Modulus")

op = input("Enter your choice (+, -, *, /, %): ")

if op == '+':
    print(f"Result: {n1 + n2}")
elif op == '-':
    print(f"Result: {n1 - n2}")
elif op == '*':
    print(f"Result: {n1 * n2}")
elif op == '/':
    if n2 != 0:
        print(f"Result: {n1 / n2}")
    else:
        print("Error: Division by zero is not defined!")
elif op == '%':
    print(f"Result: {n1 % n2}")
else:
    print("Invalid operator entered.")
