a = int(input("Enter value of a: "))
S = 0
for i in range(1, 11):
    S += (a ** i) / i
print("Sum of series =", S)
