import os
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from  Scripts import  List_Circular_Dob
import msvcrt

Li = List_Circular_Dob.ListaCircularDob()


def iniciar(self):
    while not salir:

        print(
            "---------------------- presione n para izquierda y m para derecha  --------- salir => 3--------------")
        print(
            "<- N                                                                                             M ->")

        print("\n")
        opcion = msvcrt.getch()
        print(opcion)
        if opcion == "m":
            print(Li.primero.dato.siguiente.dato)
        elif opcion == "n":
            print(li.primero.dato.anterior.dato)
        elif opcion == 3:
            salir = True
        else:
            print("Introduce un valor valido")

    print("Fin")

