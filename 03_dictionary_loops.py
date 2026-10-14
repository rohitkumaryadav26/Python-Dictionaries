
student = {
    "Maths": 85,
    "Physics": 78,
    "Chemistry": 90
}

for subject, marks in student.items():
    print(subject, ":", marks)

total = sum(student.values())
print("Total Marks:", total)