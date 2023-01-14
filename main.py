from Modules.functions import *
from datetime import datetime

print("It is", datetime.now().strftime("%B %d, %Y %H:%M:%S"))

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    i = 1

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos('todos.txt', todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            text = f"{index + 1}. {todo}"
            print(text)

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            number = int(user_action[5:])
            existing_todo = todos[number - 1]
            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("This command is not Valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip("\n").upper()
            todos.pop(number - 1)

            write_todos("todos.txt", todos)
            message = f"Todo {todo_to_remove} was removed successfully from the list."
            print(message)
        except IndexError:
            print("Todo NOT FOUND")

    elif user_action.startswith("exit"):
        break

    else:
        print("Please enter a valid command!!!!")
