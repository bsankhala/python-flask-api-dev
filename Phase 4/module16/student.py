FILE_NAME = "Phase 4\\module16\\marks.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    marks = []
    print("Enter marks for 5 subjects (0–100):")
    for i in range(5):
        m = int(input(f"Subject {i+1}: "))
        while m < 0 or m > 100:
            print("Marks must be between 0 and 100.")
            m = int(input(f"Re-enter marks for subject {i+1}: "))
        marks.append(m)

    with open(FILE_NAME, "a") as f:
        # store as simple comma values
        f.write(f"{roll},{name}," + ",".join(str(x) for x in marks) + "\n")

    print("Student record saved.\n")


def list_students_basic():
    print("\nRoll No  -  Name\n")
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                print(parts[0], "-", parts[1])
    except FileNotFoundError:
        print("No records yet.")
    print()


def view_student_details():
    roll = input("Enter roll no to view: ")
    try:
        found = False

        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")

                if data[0] == roll:
                    name = data[1]
                    marks = list(map(int, data[2:7]))
                    total = sum(marks)
                    percentage = total / 5

                    print("Roll:", roll)
                    print("Name:", name)
                    print("Marks:", marks)
                    print("Total:", total)
                    print("Percentage:", percentage)

                    found = True
                    break

        if not found:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records yet.\n")


while True:
    print("1. Add Student")
    print("2. List Students (Roll & Name only)")
    print("3. View Full Student Details")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        list_students_basic()
    elif ch == "3":
        view_student_details()
    elif ch == "4":
        break
    else:
        print("Invalid choice")
