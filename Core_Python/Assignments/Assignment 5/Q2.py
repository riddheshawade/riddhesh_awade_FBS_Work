num_students = int(input("Enter number of students: "))
all_percentages = []

for i in range(num_students):
    print(f"\nEnter marks for student {i+1}:")
    total = 0
    for j in range(5):
        marks = float(input(f"Subject {j+1} marks: "))
        total += marks
    percent = total / 5
    all_percentages.append(percent)
    print(f"Percentage of Student {i+1}: {percent:.2f}%")

average = sum(all_percentages) / num_students
print("\nAll Percentages:", all_percentages)
print("Average Percentage:", average)
