n = int(input("Enter a number: "))
temp = n
sum_fact = 0

for digit in str(n):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum_fact += fact

if sum_fact == temp:
    print("Strong number")
else:
    print("Not a strong number")
