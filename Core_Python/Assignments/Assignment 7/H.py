n = 5
for i in range(1, n + 1):
    # Left side numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Spaces in middle
    for j in range(2 * (n - i) - 1):
        print(" ", end=" ")
    
    # Right side numbers (reverse)
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()
