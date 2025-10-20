start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    sum_pow = 0
    for d in str(num):
        sum_pow += int(d) ** digits
    if sum_pow == temp:
        print(num)
