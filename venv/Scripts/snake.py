import os
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
from Scripts import Menu

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

salir = False
opcion = 0

while not salir:

    print("---------------------- MAIN MENU------------------------")
    print("-                                                      -")
    print("-                       1. Play                        -")
    print("-                       2. Scoreboard                  -")
    print("-                       3. User Selection              -")
    print("-                       4. Reports                     -")
    print("-                       5.Bulk Loading                 -")
    print("-                       6. Exit                        -")
    print("-                                                      -")
    print("--------------------------------------------------------")
    print("\n")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("----Play----")
        Menu.Snake()
    elif opcion == 2:
        print("----Scoreboard----")

        exit = false




    elif opcion == 3:
        print("----User Selection----")

    elif opcion == 4:
        print("----Reports----")
    elif opcion == 5:
        print("----Bulk Loading----")
    elif opcion == 6:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")



