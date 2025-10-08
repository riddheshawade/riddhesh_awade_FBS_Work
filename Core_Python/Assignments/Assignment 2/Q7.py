num = int(input("Enter a three-digit number: "))
sum_digits = (num // 100) + (num // 10 % 10) + (num % 10)
print(f"Sum of digits = {sum_digits}")