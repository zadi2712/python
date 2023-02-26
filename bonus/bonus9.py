
while True:

    user_action=input('*add/*show/*edit/*delete: ' + '\n')


    if 'add' in user_action or 'new' in user_action:



        with open(f"../files/bonus9.txt", "r") as file:
            list = file.readlines()
            user_actions = user_action[4:] + "\n"

            list.append(user_actions)

        with open("../files/bonus9.txt", "w") as file:
            list = file.writelines(list)


        print(user_action[4:])

    elif 'show' in user_action:
        print(user_action[5:])
        with open("../files/bonus9.txt", "r") as file:
            for i,j in enumerate(file):
                row = f"{i}--{j}"
                print(row)

    elif 'edit' in user_action:
        print(user_action[5:])

    elif 'delete' in user_action:
        print(user_action[7:])

    else:
        print('ninguno de los comandos existe')

