import os
import curses
import msvcrt
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
from Scripts import Menu
from Scripts import Pila_Score_Report
from Scripts import List_Circular_Dob
from Scripts import UserSelection
Li = List_Circular_Dob.ListaCircularDob()
Ingreso = Pila_Score_Report.Stack()
usuario = "YO"
WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 3
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100
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
salir1 = False
salir3 = False
opcion = 0
Usuario = ""
while not salir:

    print("---------------------- MAIN MENU------------------------")
    print("-                                                      -")
    print("-                       1. Play                        -")
    print("-                       2. Scoreboard                  -")
    print("-                       3. User Selection              -")
    print("-                       4. Reports                     -")
    print("-                       5. Bulk Loading                 -")
    print("-                       6. Exit                        -")
    print("-                                                      -")
    print("--------------------------------------------------------")
    print("\n")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("----Play----")
        curses.initscr()
        window = curses.newwin(HEIGHT, WIDTH, 0, 0)
        window.timeout(TIMEOUT)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.border(0)

        snake = Menu.Snake(SNAKE_X, SNAKE_Y, window)
        food = Menu.Food(window, '*')

        while True:
            window.clear()
            window.border(0)
            snake.render()
            food.render()

            window.addstr(0, 5, snake.score)
            window.addstr(0, 16, "usuario ->"+usuario)
            event = window.getch()

            if event == 27:
                break

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                snake.change_direction(event)

            if snake.head.x == food.x and snake.head.y == food.y:
                Ingreso.push("("+str(food.x)+","+str(food.y)+")")
                snake.eat_food(food)
            if event == 32:
                key = -1
                while key != 32:
                    key = window.getch()

            snake.update()
            if snake.collided:
                break

        curses.endwin()
    elif opcion == 2:
        print("----Scoreboard----")

    elif opcion == 3:
        print("----User Selection----")
        au = Li.primero
        while not salir1:

            print( "---------------------- presione n para izquierda y m para derecha  --------- salir => l--------------")
            print( "<-N                                                                                                M ->")

            print("\n")
            opcion = msvcrt.getch()

            if opcion == b'm':
                print("siguiente")
                print(au.dato)
                usuario = au.dato
                au = au.siguiente

            elif opcion == b'n':
                print("anterior")
                au = au.anterior
                print(au.dato)
                usuario = au.dato
            elif opcion == b'l':
                print("----Usuario seleccionado --- " )
                print(usuario)
                salir1 = True
            else:
                print("Introduce un valor valido")

        print("Fin")

    elif opcion == 4:
        print("----Reports----")
        while not salir3:

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
                
            elif opcion == 2:
                print("score report")
                Ingreso.graph()
            elif opcion == 3:
                print("scoreboard report")
            elif opcion == 4:
                print("users report")
                Li.graph()
            elif opcion == 5:
                salir3 = True
            else:
                print("Introduce un numero entre 1 y 5")

        print("Fin")

    elif opcion == 5:
        print("----Bulk Loading----")
        direc = input("Introduce una direccion: ")
        archivo=open(direc,"r")
        for linea in archivo:
            print(linea)
            Li.agregar_inicio(linea)
        archivo.close()

    elif opcion == 6:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")



