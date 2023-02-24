

todos = []


while True:
    user_action = input("Type 1 for add or 2 for show or 3 for exit or 4 for edit: ")
    user_action = user_action.strip()

    match user_action:
        case "1" | "add":
            todo = input("enter a todo :")
            todos.append(todo)
        case "2" | "show":
            print(todos)
            for item in todos:
                item = item.title()
                print(item)
        case "3" | "exit":
            break
        case "4" | "edit":
            number = int(input("Enter de Number of the todo list to edit"))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case whatever:
            print("what da fuck?????")




print("Bye!!!!!!!")
