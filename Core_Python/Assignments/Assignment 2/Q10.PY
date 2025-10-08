num = int(input("Enter a three-digit number: "))

reversed_num = (num % 10) * 100 + (num // 10 % 10) * 10 + (num // 100)
print(f"Reversed number = {reversed_num}")