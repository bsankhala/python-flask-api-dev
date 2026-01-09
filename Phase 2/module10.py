
employees = [
    (101, "Rahul Sharma", "IT", 55000),
    (102, "Sneha Patel", "HR", 48000),
    (103, "Amit Verma", "Finance", 62000),
    (104, "Priya Singh", "Marketing", 50000),
    (105, "Karan Mehta", "IT", 70000)
]

print("----- Employee Records -----")

for emp in employees:
    emp_id, name, dept, salary = emp
    print(f"ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: {salary}")

search_id = int(input("\nEnter Employee ID to search: "))

found = False

for emp in employees:
    emp_id, name, dept, salary = emp
    if emp_id == search_id:
        print("\n--- Employee Found ---")
        print(f"Name: {name}")
        print(f"Department: {dept}")
        print(f"Salary: {salary}")
        found = True
        break

if not found:
    print("\nEmployee not found.")
