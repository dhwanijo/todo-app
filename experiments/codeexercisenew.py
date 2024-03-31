password = input("Enter new password: ")
checkpass = {}
def check_password(password):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
        result["digit"] = digit

    letter = False
    for letters in password:
        if letters.isupper():
            letter = True
        result["UppercaseLetter"] = letter

    return result

checkpass = check_password(password)

print(checkpass)

if all(checkpass.values()):
    print("Strong Password")
else:
    print("Weak password")
