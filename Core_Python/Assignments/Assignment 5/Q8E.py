x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))
sum_series = 0
sign = 1
denominator = 1

for i in range(1, n + 1):
    term = (x ** i) / denominator
    sum_series += sign * term
    sign *= -1
    denominator += 2

print("Sum of alternating series =", sum_series)
