students = []

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
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            for student in students:
                print(f"Name: {student['name']} | Roll: {student['roll']}")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        found = False
        for student in students:
            if student["roll"] == roll:
                print(f"Found: {student['name']} - {student['roll']}")
                found = True
        if not found:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")
        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student Deleted!")
                break
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")