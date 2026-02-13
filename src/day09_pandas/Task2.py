import pandas as pd

grades=pd.Series([85,None,92,45,None,78,55])

print("Original Grades Series : ")
print(grades)

print("\nMissing Values (isnull) : ")
print(grades.isnull())

filled_grades=grades.fillna(0)

print("\nGrades after filling missing values with 0 : " )
print(filled_grades)

filled_grades=filled_grades[filled_grades>60]

print("\nScores greater than 60 : ")
print(filled_grades)