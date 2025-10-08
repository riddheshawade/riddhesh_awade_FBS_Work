cp = float(input("Enter Cost Price of book: "))
discount = float(input("Enter Discount percentage: "))

sp = cp - (cp * discount / 100)
print(f"Selling Price of book = {sp}")