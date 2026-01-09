from functools import reduce

marks = [45, 67, 89, 32, 76, 88, 92, 54]

updated_marks = list(map(lambda x: x + 5, marks))

passed_marks = list(filter(lambda x: x >= 40, updated_marks))

passed_count = reduce(lambda a, b: a + 1, passed_marks, 0)

highest_mark = reduce(lambda a, b: a if a > b else b, updated_marks)

print("Original marks:", marks)
print("Marks after grace:", updated_marks)
print("Passed marks:", passed_marks)
print("Number of students passed:", passed_count)
print("Highest mark:", highest_mark)
