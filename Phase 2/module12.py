students = {}

for i in range(3):
    name = input("Enter student name: ")
    math = int(input("Enter Math marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english
    }

print("\nTotal marks of each student:")
totals = {}
for name, marks in students.items():
    total = sum(marks.values())
    totals[name] = total
    print(name, total)

topper = max(totals, key=totals.get)
print("\nTopper:", topper, totals[topper])

print("\nStudents scoring more than 80 in Math:")
for name, marks in students.items():
    if marks["Math"] > 80:
        print(name)
