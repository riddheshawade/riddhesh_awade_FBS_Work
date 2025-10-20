n = int(input("Enter N: "))
sum_series = 0
for i in range(1, n + 1):
    sum_series += n ** i
print("Sum of power series =", sum_series)
