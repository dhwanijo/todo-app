try:
    width = float(input("Please enter rectangle width: "))
    length = float(input("Please enter rectangle length: "))
    if length == width:
         exit("It looks like a square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter the number")

