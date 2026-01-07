employee_name=input("Enter Employee name: ")
employee_id=input("Enter Employee id: ")
tot_days=int(input("Enter the total number of workig days:  "))
present_days=int(input("Enter number of days present: "))

att_perc=(present_days/tot_days)*100

if att_perc >= 90:
    status="Excellent"
elif 90 > att_perc >=75:
    status="Satisfactory"
else:
    status = "Needs consistancy"

print("-------------Employee attendance-------------")
print(f"Employee name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"\nTotal working days: {tot_days}")
print(f"Days Present: {present_days}")
print(f"Percentage of attendance: {att_perc}")
print(f"\nStatus: {status}")