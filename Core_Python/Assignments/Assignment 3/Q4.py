a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
