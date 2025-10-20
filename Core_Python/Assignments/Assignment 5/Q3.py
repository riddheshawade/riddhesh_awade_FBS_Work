num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_amount = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))

    if age < 12:
        amount = ticket_cost * 0.7
    elif age > 59:
        amount = ticket_cost * 0.5
    else:
        amount = ticket_cost

    total_amount += amount

print("\nTotal ticket cost for all passengers =", total_amount)
