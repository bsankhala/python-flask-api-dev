marks = list(map(int, input("Enter marks of 5 students (comma separated): ").split(",")))

print("First mark:", marks[0])
print("Last mark:", marks[-1])

print("Marks of 2nd to 4th students:", marks[1:4])

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

average = sum(marks) / len(marks)
print("Average marks:", average)

new_mark = int(input("Enter marks of new student: "))
marks.append(new_mark)
print("Updated marks list:", marks)

marks = [m for m in marks if m >= 33]
print("Marks after removing failed students (<33):", marks)

class1 = marks
class2 = list(map(int, input("Enter marks of second class (comma separated): ").split(",")))
nested_marks = [class1, class2]

print("Nested list of two classes:", nested_marks)
