student={"Name": "Shree", "Age":21,"Course":"B.E"}
print(student["Name"])
student["Age"]=22
student["city"]="Udupi"
print(student)

marks = {"math": 80, "science": 75, "english": 85}

print(marks.get("math"))
print(marks.get("history",0))

for subject, score in marks.items():
    print(subject, score)

