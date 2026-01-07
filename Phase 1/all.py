print("=== Employee Salary & Attendance Management System ===\n")

emp_name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic monthly salary: "))
total_days = int(input("Enter total working days in month: "))
present_days = int(input("Enter number of days present: "))

print("\nProcessing data...\n")

attendance_percentage = (present_days / total_days) * 100

if attendance_percentage >= 90:
    attendance_status = "Excellent"
elif attendance_percentage >= 75:
    attendance_status = "Good"
else:
    attendance_status = "Needs Improvement"

hra = 0.20 * basic_salary     
da = 0.10 * basic_salary       
gross_salary = basic_salary + hra + da

per_day_salary = gross_salary / total_days
salary_deduction = (total_days - present_days) * per_day_salary
final_salary = gross_salary - salary_deduction

print("\n\t--- Employee Report ---\n")

print(f"Employee Name:\t{emp_name}")
print(f"Employee ID:\t{emp_id}")

print(f"\nTotal Working Days:\t{total_days}")
print(f"Present Days:\t\t{present_days}")
print(f"Attendance Percentage:\t{attendance_percentage:.2f}%")
print(f"Attendance Status:\t{attendance_status}")

print("\n\t--- Salary Details ---\n")
print(f"Basic Salary:\t\t₹{basic_salary:.2f}")
print(f"HRA (20%):\t\t₹{hra:.2f}")
print(f"DA (10%):\t\t₹{da:.2f}")
print(f"Gross Salary:\t\t₹{gross_salary:.2f}")
print(f"Salary Deduction:\t₹{salary_deduction:.2f}")
print(f"Final Payable Salary:\t₹{final_salary:.2f}")

print("\nReport saved at: C:\\Company\\HR\\SalaryReports\\")

