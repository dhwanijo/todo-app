user_name = input("Add a new member: ")
file = open("/home/dhwani/Downloads/members.txt", "r")
member_list = file.readlines()
file.close()

member_list.append(user_name + "\n")

file = open("/home/dhwani/Downloads/members.txt", "w")
file.writelines(member_list)
file.close()


