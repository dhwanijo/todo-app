def temperature_type(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

temp = temperature_type(8)
print(temp)

def cal_string(str_arg):
    if len(str_arg) >= 8:
        return "True"
    else:
        return "False"

length = cal_string("mypass")
print(length)