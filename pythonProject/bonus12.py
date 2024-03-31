feet_inches = input("Enter feet and inches: ")

def convert(feet_inches1):
    parts = feet_inches1.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meter = feet * 0.3048 + inches * 0.0254
    output = f"{feet} feet and {inches} inches is equal to {meter} meters"
    return meter



result = convert(feet_inches)

if result < 1:
    print("Kid is too small to use the slide")
else:
    print("Kid can use the slide")