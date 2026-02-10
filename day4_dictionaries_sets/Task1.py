contacts={
    "Shri" : 9876543210,
    "Dhanya" : 9012345678,
    "Alice" : 9000012345
}
contacts["Bob"] = 8976453729
contacts["Alice"] = 789654321

existing_contact=contacts.get("Alice","Contact not found")
missing_contact=contacts.get("Eve","Contact not found")

print("Lookup Results :")
print("Alice",existing_contact)
print("Eve",missing_contact)
print()

print("Contact List :")
for name,number in contacts.items():
    print(f"Contact : {name} | Phone : {number} ")



