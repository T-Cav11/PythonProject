import Functions
import FreeSimpleGUI as sg

label =sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task: ", key = "task")
add_task_button = sg.Button("Add")
list_box = sg.Listbox(Functions.get_tasks(), key = "existing_tasks",
                      enable_events =  True, size = [45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("Tasks to be completed",
                   [[label], [input_box, add_task_button], [list_box, edit_button]],
                   font= ("Helvetica", 11))

while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            tasks = Functions.get_tasks()
            new_task = values["task"] + "\n"
            tasks.append(new_task)
            Functions.write_tasks(tasks)
            window["existing_tasks"].update(tasks)
        case "Edit":
            task_to_edit = values["existing_tasks"][0]
            new_task = values["task"]

            tasks = Functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task + "\n"
            Functions.write_tasks(tasks)
            window["existing_tasks"].update(tasks)
        case "existing_tasks":
          window["task"].update(values["existing_tasks"][0].strip())

        case sg.WIN_CLOSED:
            break


window.close()


