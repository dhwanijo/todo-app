todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for i, item in enumerate(todos):
                row = f"{i+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of a Todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of a Todo completed: "))
            number = number - 1
            if (len(todos) >= number):
                todos.pop(number)
            else:
                print("No todos at that number")
        case 'exit':
            break



print("Bye!")






