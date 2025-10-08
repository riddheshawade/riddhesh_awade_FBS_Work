amount = int(input("Enter the amount: "))

notes_2000 = amount // 2000
amount = amount % 2000

notes_500 = amount // 500
amount = amount % 500

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_10 = amount // 10
amount = amount % 10

notes_5 = amount // 5
amount = amount % 5

notes_1 = amount

print(f"2000: {notes_2000}, 500: {notes_500}, 100: {notes_100}, 50: {notes_50}, 10: {notes_10}, 5: {notes_5}, 1: {notes_1}")