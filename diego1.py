
while True:
    user_action = input("1-agregar***2-mostar***3-editar***4-borrar***5-salir: ")
    user_action = user_action.strip()
    match user_action:
        case '1':
            lista = input('ingrese texto: ') + '\n'

            with open('files/lista.txt', 'r') as file:
                listas = file.readlines()

            listas.append(lista)

            with open('files/lista.txt', 'w') as file:
                listas = file.writelines(listas)

        case '2':
            with open('files/lista.txt', 'r') as file:
                listas = file.readlines()

            for i,j in enumerate(listas):
                row = f'{i}--{j}'
                print(row)

        case '3':

            num = int(input('ingrese el nro de registro a editar: '))
            with open('files/lista.txt', 'r') as file:
                listas = file.readlines()


            nueva_lista =  input('ingrese el nuevo registro: ')
            listas[num] = nueva_lista

            with open('files/lista.txt', 'w') as file:
                listas = file.writelines(listas[num])

        case '4':
            with open('files/lista.txt', 'r') as file:
                listas = file.readlines()

            num = int(input('ingrese el nro de registro a borrar'))
            listas.pop(num)

            with open('files/lista.txt', 'w') as file:
                listas = file.writelines(listas)


        case '5':
            break

print('nos olemos......')




