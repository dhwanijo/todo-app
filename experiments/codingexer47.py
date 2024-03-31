def get_age(year_of_birth, current_year=2024):
    age = current_year - year_of_birth
    return age

current_age = get_age(1998)
print(current_age)