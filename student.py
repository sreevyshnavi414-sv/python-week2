import csv
import os
FILE = "students.csv"
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Roll Number", "Name", "Marks"])
        writer.writerow([roll, name, marks])
    print("Student added successfully.")
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if not os.path.exists(FILE):
        print("No student records found.")
        return
    with open(FILE, "r") as file:
        students = list(csv.reader(file))
    if len(students) == 0:
        print("No student records found.")
        return
    header = students[0]
    records = students[1:]
    new_records = [student for student in records if student[0] != roll]
    if len(new_records) == len(records):
        print("Student not found.")
    else:
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(new_records)
        print("Student deleted successfully.")
def search_student():
    roll = input("Enter Roll Number to search: ")
    if not os.path.exists(FILE):
        print("No student records found.")
        return
    with open(FILE, "r") as file:
        students = csv.reader(file)
        next(students, None)
        for student in students:
            if student[0] == roll:
                print("Roll Number:", student[0])
                print("Name:", student[1])
                print("Marks:", student[2])
                return
    print("Student not found.")
def display_students():
    if not os.path.exists(FILE):
        print("No student records found.")
        return
    with open(FILE, "r") as file:
        students = list(csv.reader(file))
    if len(students) <= 1:
        print("No student records found.")
        return
    print("\n----- Student Records -----")
    for student in students:
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Marks:", student[2])
        print("--------------------------")
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")