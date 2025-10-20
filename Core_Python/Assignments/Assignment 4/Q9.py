start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
divisor = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % divisor == 0:
        print(i)
