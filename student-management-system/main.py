import json
import os

FILE = "students.json"

# Load students
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        students = json.load(f)
else:
    students = []

def save_students():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        students.append({"name": name, "roll": roll})
        save_students()
        print("Student Added Successfully!")

    elif choice == "2":
        if not students:
            print("No Students Found!")
        else:
            for s in students:
                print(f"Name: {s['name']} | Roll: {s['roll']}")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        found = False
        for s in students:
            if s["roll"] == roll:
                print(f"Found -> Name: {s['name']}, Roll: {s['roll']}")
                found = True
                break
        if not found:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")
        found = False
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                save_students()
                print("Student Deleted Successfully!")
                found = True
                break
        if not found:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")