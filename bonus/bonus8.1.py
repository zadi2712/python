
date = input('ingrese el dia: dia/mes/año: ')
mood = input('como esta su humorr hoy del 1 al 10????: ')
thoughts = input('digame cual es su pensamiento :\n')

with open(f"../journal/{date}.txt", "w") as archivo:
    archivo.write(mood +2 * "\n")
    archivo.write(thoughts)
