basic = float(input("Enter Basic Salary: "))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra
print(f"Total Salary = {total_salary}")