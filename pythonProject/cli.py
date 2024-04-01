# from functions import get_todos, write_todos
from functions import *
import time

now = time.strftime("%b %m, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{i + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is invalid. You need to add number")
            continue
        except IndexError:
            print("Your todo is not available on the list to edit.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except (ValueError, IndexError):
            print("You need to enter number which exists in the todo list")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")






