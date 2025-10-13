num = int(input("Enter a 3-digit number: "))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome number")
else:
    print("Not a Palindrome")
