n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i or j == n or i == 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
