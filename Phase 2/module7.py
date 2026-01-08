for n in range (1,6):
    print(f"\nTable of {n}\n")
    for i in range(1,11):
        print(i*n,end="  ")


print("\n\n----- ATM Cash Withdrawal -----")

balance = float(input("Enter your account balance: "))

while True:
    amount = float(input("Enter withdrawal amount: "))
    if amount < 100:
        print("Minimum withdrawal is ₹100.")
    elif amount > 50000:
        print("Maximum withdrawal limit is ₹50,000.")
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        break

print("\nDispensing cash...\n")

remaining_amount = int(amount)
total_notes = 0

for note in (2000, 500, 200, 100):
    count = remaining_amount // note
    remaining_amount -= count * note
    print(f"{note} x {count}")
    total_notes += count

if remaining_amount != 0:
    print("\nATM cannot dispense exact amount with available denominations.")
else:
    balance -= amount
    print(f"\nTotal notes dispensed: {total_notes}")
    print(f"Remaining Balance: ₹{balance}")
    print("\nThank you for using the ATM!")

