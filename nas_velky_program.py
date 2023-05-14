#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d. %b, %Y %H:%M:%S")
print("Today is", now)

while True:
    user_action = input("Type add, show, edit, complete and exit:")

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        with open("svap.txt") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            riadok = f"{index + 1}.{item}"
            print(riadok)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("New todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid: ")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            massage = f"Todo {todo_to_remove} was removed from the list."
            print(massage)
        except IndexError:
            print("There is no item with that value")

    elif "exit" in user_action:
        print("BYE ! ")
        break
    else:
        print("Ty pač poradne co maš pisac chuju !")
