amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes:")

for note in notes:
    count = amount // note
    if count > 0:
        print(f"{note} x {count}")
        amount = amount % note
