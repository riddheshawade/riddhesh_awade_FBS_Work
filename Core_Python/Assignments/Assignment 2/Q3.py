feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = feet*12 + inches
total_cm = total_inches * 2.54
meters = int(total_cm // 100)
centimeters = total_cm % 100

print(f"{feet} feet and {inches} inches = {meters} meters and {centimeters} cm")