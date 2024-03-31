def parse(feet_inches1):
    parts = feet_inches1.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
