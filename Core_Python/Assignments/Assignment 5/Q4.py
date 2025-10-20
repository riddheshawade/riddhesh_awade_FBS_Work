n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum_pow = 0

for d in str(n):
    sum_pow += int(d) ** digits

if sum_pow == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
