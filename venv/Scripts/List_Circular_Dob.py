class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaCircularDob :
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.unir_nodos()

    def agregar_final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.unir_nodos()

    def unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
    def Recorrer_inicio_A_Fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
    def Recorrer_fin_a_Inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break



hola = ListaCircularDob()
hola.agregar_inicio("kk")
hola.agregar_inicio("la")
hola.agregar_inicio("lo")
hola.agregar_inicio("pu")
hola.Recorrer_inicio_A_Fin()

