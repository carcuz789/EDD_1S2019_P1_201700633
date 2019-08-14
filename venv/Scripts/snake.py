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
usuario = ""
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
        Menu.iniciar()
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



