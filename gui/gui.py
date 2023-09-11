import PySimpleGUI as sg
import functions
import time
sg.theme("DarkAmber")
clock=sg.Text('', key="clock")
label=sg.Text("Enter a To-Do")
input_text=sg.InputText(tooltip="Enter to-do",key="todo")
add=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
delete_button=sg.Button("Delete")
exit=sg.Button("Exit")
window=sg.Window("To-Do App",layout=[[clock],[label],[input_text,add],[list_box,edit_button],[delete_button,exit]],font=('Helvetica',10),background_color="black")
while True:
    event,values=window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todos_to_edit=values['todos'][0]
                new_todo=values['todo']
                todos=functions.get_todos()
                index=todos.index(todos_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.",font=("Helvetica",10))
        case "Delete":
            try:
                todos_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 10))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
