import glob

result = glob.glob("../files/*.txt")

for filepath in result:
    with open(filepath, 'r') as file:
        print(file.read().upper())
