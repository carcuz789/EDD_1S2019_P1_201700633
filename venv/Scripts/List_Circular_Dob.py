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
        # METODO PARA GRAFICAR

    def graph(self):
        # INICIO DE LA LISTA
        temp = self.primero
        # SE CREA EL PUNTO DOT.; W ES PARA ESCRIBIR EN EL ARCHIVO
        f = open("UsersReport.dot", "w")
        # SE INICIA EL DIAGRAMA
        f.write("digraph G {\n")
        # SE ESTABLECE LA FORMA CUADRADA
        f.write("node [shape = square];\n")
        # SE ESTABLECE FORMA HORIZONTAL
        f.write("rankdir=LR;\n")
        # SE CREAN DOS NODOS NULL
        # f.write("Null1 [label=\"null\"];\n")
        # f.write("Null2 [label=\"null\"];\n")
        # EL PRIMERO APUNTA A NULL (1ER NULL QUE SE CREO)
        # f.write("\"" + temp.valor + "\"" + " -> Null1; \n")
        # RELACIONES ENTRE NODOS
        for i in range(0, self.__sizeof__() - 1):
            temp2 = temp.primero.siguiente
            f.write(" \"" + temp.valor + "\" -> \"" + temp2.valor + "\"; \n")
            f.write(" \"" + temp2.valor + "\" -> \"" + temp.valor + "\"; \n")
            temp = temp.primero.siguiente
        # EL ULTIMO APUNTA A NULL (EL 2DO NULL QUE SE CREO)
        # f.write("\"" + temp.valor + "\"" + " -> " + "Null2; \n")
        # SE CIERRA EL GRAFICO
        f.write("}")
        f.close()
        # SE TRANSFORMA EL .DOT A .JPG (EL NOMBRE .DOT TIENE QUE SER EL DE ARRIBA, EL .JPG PUEDE SER DIFERENTE)
        os.system("dot -Tjpg UsersReport.dot -o UsersReport.jpg")
        # SE ABRE EL ARCHIVO .JPG
        os.system("UsersReport.jpg")
        # IMPRIMIR LISTA

    def printL(self):
        temp = self.ini
        i = 0
        print("Lista: ")
        while temp is not None:
            print("Valor: " + temp.valor)
            i += 1
            temp = temp.sig






