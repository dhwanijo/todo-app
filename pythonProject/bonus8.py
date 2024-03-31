date = input("Enter the date: " )
mood = input("Enter the mood from 1 to 10: ")
thoughts = input("Enter the thoughts: " + "\n")

with open(f"../Journals/{date}.txt", 'w') as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)