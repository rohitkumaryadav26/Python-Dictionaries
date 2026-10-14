
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    for roll, details in students.items():
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("-------------------")

def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        print("Student Details:", students[roll])
    else:
        print("Student not found.")

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program Ended.")
        break
    else:
        print("Invalid choice. Try again.")