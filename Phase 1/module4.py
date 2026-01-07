meter_id = input("Enter Meter ID: ")
units = int(input("Enter units consumed: "))
prev_units = int(input("Enter previous month units: "))
customer_type = input("Enter customer type (R for Residential / C for Commercial): ")

if units <= 100:
    energy_charge = units * 5
elif units <= 300:
    energy_charge = (100 * 5) + ((units - 100) * 7)
else:
    energy_charge = (100 * 5) + (200 * 7) + ((units - 300) * 10)

fixed_charge = 100
gst = 0.18 * (energy_charge + fixed_charge)
bill_before_discount = energy_charge + fixed_charge + gst

if units == 0:
    usage = "No Usage"
elif units < 100:
    usage = "Low"
elif units <= 300:
    usage = "Moderate"
else:
    usage = "High"

subsidy_applied = False
surcharge_applied = False
final_bill = bill_before_discount

if (customer_type == "R" or customer_type == "r") and units < 200:
    final_bill -= 0.05 * final_bill
    subsidy_applied = True
elif (customer_type == "C" or customer_type == "c") or units > 400:
    final_bill += 0.10 * final_bill
    surcharge_applied = True
else:
    subsidy_applied = False
    surcharge_applied = False

ev_connection = "EV" in meter_id
next_month_estimate = units << 1

bill_ref_1 = final_bill
bill_ref_2 = final_bill
same_object = bill_ref_1 is bill_ref_2

print("\n------ Electricity Bill Summary ------")
print(f"Meter ID: {meter_id}")
print(f"Units Consumed: {units}")
print(f"Previous Month Units: {prev_units}")
print(f"Customer Type: {'Residential' if customer_type == 'R' else 'Commercial'}")
print(f"\nUsage Category: {usage}")
print(f"Estimated Next Month Usage: {next_month_estimate} units")
print(f"\nEnergy Charges: {energy_charge}")
print(f"Fixed Charges: {fixed_charge}")
print(f"GST: {gst:.2f}")
print(f"Final Bill Amount: {final_bill:.2f}")
print(f"\nEV Connection?: {ev_connection}")
print(f"Subsidy Applied?: {subsidy_applied}")
print(f"Surcharge Applied?: {surcharge_applied}")
print(f"Same bill reference in memory?: {same_object}")