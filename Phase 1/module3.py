employee_name=input("Enter Employee name: ")
basic_salary=int(input("Enter basic salary: "))

hra=0.1*basic_salary
da=0.05*basic_salary

total_salary=basic_salary+hra+da

is_high_earner=total_salary>50000

print("------Employee Salary Details------")
print(f"Employee name: {employee_name}")
print(f"Employee salary: {basic_salary}")
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"Total Salary: {total_salary}")
print(f"High Earner?: {is_high_earner}")

print("\n------Datatypes------")
print(type(employee_name))
print(type(basic_salary))
print(type(hra))
print(type(da))
print(type(is_high_earner))