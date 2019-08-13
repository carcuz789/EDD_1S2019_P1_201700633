import os
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
from Scripts import Menu
from Scripts import Pila_Score_Report

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
    print("-                       1. SNAKE REPORT                -")
    print("-                       2. SCORE REPORT                -")
    print("-                       3. SCOREBOARD REPORT           -")
    print("-                       4. USERS REPORT                -")
    print("-                       5. EXIT                        -")
    print("-                                                      -")
    print("-                                                      -")
    print("--------------------------------------------------------")
    print("\n")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("snake report")
        Menu.snake
    elif opcion == 2:
        print("score report")
        pil = Pila_Score_Report.Stack()
        pil.print_stack()
    elif opcion == 3:
        print("scoreboard report")
    elif opcion == 4:
        print("users report")
    elif opcion == 5:
        salir = True
    else:
        print("Introduce un numero entre 1 y 5")

print("Fin")