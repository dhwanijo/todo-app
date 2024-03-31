waiting_list = ["sen", "ben", "john"]
waiting_list.sort(reverse=True)
for index, items in enumerate(waiting_list):
    row = f"{index+1}.{items.title()}"
    print(row)
