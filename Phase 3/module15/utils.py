def display_student_details(name, student_id, total, percentage, grade):
    print("\n----- Report Card -----")
    print(f"Student Name: {name}")
    print(f"Student ID: {student_id}")
    print(f"Total Marks: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("------------------------")
