password = input("Enter new Password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase_letter = False
for i in password:
    if i.isupper():
        uppercase_letter = True

result["uppercase"] = uppercase_letter

if all(result.values()):
    print("Strong password")
else:
    print("Weak Password")
