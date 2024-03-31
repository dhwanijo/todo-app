filenames = ["1.doc", "1.report", "1.presentation"]
print("Before list comprehension.......")
print(filenames)

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print("After list comprehension............")
print(filenames)