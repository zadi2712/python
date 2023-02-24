

todos = []


while True:
    user_action = input("Type 1 for add or 2 for show or 3 for exit: ")
    user_action = user_action.strip()

    match user_action:
        case "1" | "add" :
            todo = input("enter a todo :")
            todos.append(todo)
        case "2" | "show" :
            print(todos)
            for item in todos:
                item = item.title()
                print(item)
        case "3" | "exit" :
            break
        case whatever :
            print("what da fuck?????")


print("Bye!!!!!!!")
