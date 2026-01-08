print("----- Cafe Billing System -----")

customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")

total_bill = 0

choice = input("Do you want to place an order? (y/n): ")

if choice == "y" or choice == "Y":

    while True:
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        item_total = price * quantity
        total_bill += item_total

        print(f"Total for {item_name}: {item_total}")

        more = input("Do you want to add more items? (y/n): ")

        if more == "n" or more == "N":
            break

else:
    print("Thank you for visiting!")

print("\n----- Bill Summary -----")
print(f"Customer Name: {customer_name}")
print(f"Customer ID: {customer_id}")
print(f"Total Amount Before Discount: {total_bill}")

if total_bill > 1000:
    discount = 0.10 * total_bill
elif total_bill >= 500:
    discount = 0.05 * total_bill
else:
    discount = 0

final_amount = total_bill - discount

print(f"Discount Applied: {discount}")
print(f"Final Payable Amount: {final_amount}")
print("Thank you! Visit again!!")
