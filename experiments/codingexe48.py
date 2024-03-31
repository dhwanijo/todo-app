def get_nr_items(str_arg):
    items = str_arg.split(",")
    num_items = len(items)
    return num_items

item = get_nr_items("Lisa, Joe, dhwani")
print(item)

