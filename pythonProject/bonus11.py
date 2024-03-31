def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
        values = data[1:]

        temp = [float(i) for i in values]

        average_local = sum(temp) / len(temp)
    return average_local


average = get_average()
print(average)
