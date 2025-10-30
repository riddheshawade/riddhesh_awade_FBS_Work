n = 5
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(65, 65 + (2 * i + 1)):
        print(chr(j), end=" ")
    print()
