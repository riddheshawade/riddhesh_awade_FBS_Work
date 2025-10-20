n = int(input("Enter n: "))
sum_geo = 0
for i in range(n):
    sum_geo += 2 ** i
print("Sum of geometric series =", sum_geo)
