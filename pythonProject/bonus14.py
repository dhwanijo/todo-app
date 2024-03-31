from pythonProject.parsers.converters import convert
from pythonProject.parsers.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("Kid is too small to use the slide")
else:
    print("Kid can use the slide")