import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))
print(data)
city = input("Enter the city: ")

for i in data:
    if i[0] == city:
        print(i[1])

