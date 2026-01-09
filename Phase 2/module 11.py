python_students = {101, 102, 103, 104}
datascience_students = {103, 104, 105}

both_courses = python_students.intersection(datascience_students)
print("Students in both courses:", both_courses)

only_python = python_students.difference(datascience_students)
print("Only Python students:", only_python)

all_students = python_students.union(datascience_students)
print("All unique students:", all_students)

print("Are sets disjoint?", python_students.isdisjoint(datascience_students))

frozen_all_students = frozenset(all_students)
print("Frozen set of all students:", frozen_all_students)

python_students.add(110)
print("Updated Python students:", python_students)

datascience_students.discard(999)  # 999 not present but no error
print("Updated Data Science students:", datascience_students)

