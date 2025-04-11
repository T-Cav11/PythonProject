import Functions
import FreeSimpleGUI as sg
import time

sg.theme("Reddit")

clock = sg.Text("", key="clock")
label =sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task: ", key = "task")
add_task_button = sg.Button("Add")
list_box = sg.Listbox(Functions.get_tasks(), key = "existing_tasks",
                      enable_events =  True, size = [45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("Tasks to be completed",
                   [[clock],
                    [label],
                    [input_box, add_task_button],
                    [list_box, edit_button, complete_button,],
                    [exit_button]],
                   font= ("Helvetica", 11))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            tasks = Functions.get_tasks()
            new_task = values["task"] + "\n"
            tasks.append(new_task)
            Functions.write_tasks(tasks)
            window["existing_tasks"].update(tasks)
        case "Edit":
            try:
                task_to_edit = values["existing_tasks"][0]
                new_task = values["task"]

                tasks = Functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task + "\n"
                Functions.write_tasks(tasks)
                window["existing_tasks"].update(tasks)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 11))

        case "Complete":
            try:
                task_to_complete = values["existing_tasks"][0]
                tasks = Functions.get_tasks()
                tasks.remove(task_to_complete)
                Functions.write_tasks(tasks)
                window["existing_tasks"].update(values=tasks)
                window["task"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 11))


        case "existing_tasks":
          window["task"].update(values["existing_tasks"][0].strip())

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()


