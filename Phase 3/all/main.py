from marks import calculate_total, calculate_percentage
from grade import get_grade
from report import print_report

name = input("Enter student name: ")

while True:
    marks = list(map(int, input("Enter marks of 5 subjects separated by space: ").split()))
    
    if len(marks) == 5:
        break
    else:
        print("Please enter exactly 5 marks!")

total = calculate_total(marks)
percentage = calculate_percentage(marks)
grade = get_grade(percentage)

print_report(name, marks, total, percentage, grade)
