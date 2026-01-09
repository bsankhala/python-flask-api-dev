num_students = int(input("Enter number of students: "))

students = []

for _ in range(num_students):
    name = input("Enter student name: ").strip().title()
    roll = int(input("Enter roll number: "))
    
    marks = list(map(int, input("Enter 3 subject marks (comma separated): ").split(",")))
    
    marks_tuple = tuple(marks)

    total = sum(marks_tuple)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks_tuple,
        "total": total
    }

    students.append(student)

topper = max(students, key=lambda s: s["total"])

fail_students = [s["name"] for s in students if any(m < 40 for m in s["marks"])]

distinction_students = [s["name"] for s in students if all(m >= 75 for m in s["marks"])]

unique_names = {s["name"] for s in students}

unique_marks = set()
for s in students:
    unique_marks.update(s["marks"])

print("\n--- Student Records ---")
for s in students:
    print(s)

print("\nTopper:", topper["name"], "with total", topper["total"])

print("\nStudents who failed in any subject:", fail_students)

print("\nStudents with distinction in all subjects:", distinction_students)

print("\nUnique student names:", unique_names)

print("\nUnique marks obtained:", unique_marks)
