units = float(input("Enter total units consumed: "))

if units <= 50:
    amount = units * 0.50
elif units <= 150:
    amount = (50 * 0.50) + (units - 50) * 0.75
elif units <= 250:
    amount = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
    amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

surcharge = amount * 0.20
total = amount + surcharge

print(f"Electricity Bill = ₹{total:.2f}")
