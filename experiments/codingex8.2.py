filenames = ["a.txt", "b.txt", "c.txt"]
for filename in filenames:
    file = open(f"/home/dhwani/Downloads/{filename}", "r")
    name = file.read()
    print(name)




