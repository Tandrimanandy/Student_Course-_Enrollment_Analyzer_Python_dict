students = {
    101: {"name": "Tandrima", "python": 85, "java": 78, "sql": 90},
    102: {"name": "Prity", "python": 92, "java": 88, "sql": 95},
    103: {"name": "Drubo",  "python": 70, "java": 75, "sql": 68},
}


# ---------- Calculations ----------
def calculate_total(student):
    return student["python"] + student["java"] + student["sql"]


def calculate_average(student):
    return calculate_total(student) / 3


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


# ---------- Display / Search ----------
def display_students(students):
    if not students:
        print("No students available")
        return
    for student_id, student in students.items():
        print("\nID:", student_id)
        print("Name:", student["name"])
        print("Python:", student["python"])
        print("Java:", student["java"])
        print("SQL:", student["sql"])


def search_student(students, student_id):
    if student_id in students:
        print("\nStudent Found")
        print("Name:", students[student_id]["name"])
    else:
        print("Student not found")


def display_report(students, student_id):
    if student_id not in students:
        print("Student not found")
        return

    student = students[student_id]
    total = calculate_total(student)
    average = calculate_average(student)
    grade = calculate_grade(average)

    print("\n===== STUDENT REPORT =====")
    print("ID:", student_id)
    print("Name:", student["name"])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


# ---------- Add / Update / Delete ----------
def add_student(students):
    student_id = int(input("Enter student ID: "))
    if student_id in students:
        print("ID already exists")
        return

    name = input("Enter student name: ")
    python_marks = int(input("Enter Python marks: "))
    java_marks = int(input("Enter Java marks: "))
    sql_marks = int(input("Enter SQL marks: "))

    students[student_id] = {
        "name": name,
        "python": python_marks,
        "java": java_marks,
        "sql": sql_marks,
    }
    print("Student added successfully")


def update_marks(students, student_id):
    if student_id not in students:
        print("Student not found")
        return

    marks = int(input("Enter new Python marks: "))
    students[student_id]["python"] = marks
    print("Marks updated successfully")


def delete_student(students):
    student_id = int(input("Enter student ID: "))
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully")
    else:
        print("Student not found")


# ---------- Analysis ----------
def find_topper(students):
    if not students:
        print("No students available")
        return

    topper_id = max(students, key=lambda sid: calculate_total(students[sid]))

    print("\n===== TOPPER =====")
    print("ID:", topper_id)
    print("Name:", students[topper_id]["name"])
    print("Total:", calculate_total(students[topper_id]))


# ---------- Menu ----------
def menu():
    print("\n ********************* STUDENT PERFORMANCE SYSTEM *************************")
    print("1. Display Students")
    print("2. Search Student")
    print("3. Student Report")
    print("4. Add Student")
    print("5. Update Marks")
    print("6. Delete Student")
    print("7. Find Topper")
    print("8. Exit")


# ---------- Main Loop ----------
while True:
    menu()

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                display_students(students)
            case 2:
                search_student(students, int(input("Enter student ID: ")))
            case 3:
                display_report(students, int(input("Enter student ID: ")))
            case 4:
                add_student(students)
            case 5:
                update_marks(students, int(input("Enter student ID: ")))
            case 6:
                delete_student(students)
            case 7:
                find_topper(students)
            case 8:
                print("Thank you!")
                break
            case _:
                print("Invalid choice")

    except ValueError:
        print("Please enter numbers only")