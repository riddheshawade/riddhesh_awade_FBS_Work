import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Enter this number:", captcha)
    user_input = int(input("Enter the number again: "))
    if user_input == captcha:
        print("Login Success!")
    else:
        print("Captcha Failed!")
else:
    print("Invalid User ID or Password!")
