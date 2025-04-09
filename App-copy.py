def get_tasks():
    with open("app.txt", "r") as file:
        tasks = file.readlines()
    return tasks


while True:
    user_prompt = input("Type add or show, edit, complete or exit: ")
    user_prompt = user_prompt.strip()

    if user_prompt.startswith("add"):
        task = user_prompt[4:]
        print("Task added!")

        tasks = get_tasks()

        tasks.append(task + "\n")

        with open("app.txt", "w") as file:
            file.writelines(tasks)


    elif user_prompt.startswith("show"):
        tasks = get_tasks()

        new_tasks = [item.strip("\n") for item in tasks]

        for index, item in enumerate (new_tasks):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_prompt.startswith("edit"):
        try:
            number = int(user_prompt[5:])
            number = (number - 1)
            with open("app.txt", "r") as file:
                tasks = file.readlines()


            new_tasks = input("New todo: ")
            tasks[number] = new_tasks + "\n"

            with open("app.txt", "w") as file:
                file.writelines(tasks)
            print("List updated!")
        except ValueError:
            print("Command is not valid. Please try again.")
            continue


    elif user_prompt.startswith("complete"):
        try:
            number = int(user_prompt[9:])
            tasks = get_tasks()
            index = number - 1
            task_to_remove = tasks[index]
            task_to_remove = task_to_remove.strip("\n")
            task_to_remove = task_to_remove.capitalize()
            tasks.pop(index)

            with open("app.txt", "w") as file:
                file.writelines(tasks)

            print(f"{task_to_remove} was completed and removed from the list.")
        except IndexError:
            print("There is no item with that number. Please try again")
            continue

    elif user_prompt.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")