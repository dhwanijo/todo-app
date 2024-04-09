import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_todo = sg.Listbox(functions.get_todos(), key="todolist",
                       enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                       layout=[[label],
                               [input_box, add_button],
                               [list_todo, edit_button, complete_button],
                               [exit_button]],
                       font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['todolist'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todolist'].update(values=todos)

        case "Edit":
            todo_to_edit = value['todolist'][0]
            new_todo = value['todo']

            todos = functions.get_todos()
            index_todo = todos.index(todo_to_edit)
            todos[index_todo] = new_todo + "\n"
            functions.write_todos(todos)
            window['todolist'].update(values=todos)

        case "Complete":
            todo_to_complete = value["todolist"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todolist'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            break

        case "todolist":
            window['todo'].update(value=value['todolist'][0])

        case sg.WIN_CLOSED:
            break

window.close()