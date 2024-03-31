contents = ["This is my Python " \
            "Program",
            "I am sitting in " \
            "McDonald's",
            "I love Dancing in the morning"]

filenames = ["python.txt", "place.txt", "hobby.txt"]

for filename, content in zip(filenames, contents):
    file = open(f"../files/{filename}", "w")
    file.writelines(content)
    file.close()