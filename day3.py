import os

todos = []


while True:
    user_action = input("Type 1 for add or 2 for show or 3 for exit: ")



    match user_action:
        case "1":
            todo = input("enter a todo :")
            todos.append(todo)
        case "2":
            print(todos)
            for item in todos:
                print(item)
        case "3":
            break


print("Bye!!!!!!!")