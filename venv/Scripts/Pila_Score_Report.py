class Stack:  # Creamos la clase Stack
    def __init__(self):
        self.items = []

    def is_empty(self):  # Metodo para verificar si la pila esta vacia
        return self.items == []

    def push(self, item):  # Metodo para insertar elementos a la pila
        self.items.insert(0, item)

    def pop(self):  # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)

    def print_stack(self):  # Metodo para mostrar los elementos de la pila
        print(self.items)


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
        f.write("rankdir=TB;\n")
        # SE CREAN DOS NODOS NULL
        # f.write("Null1 [label=\"null\"];\n")
        # f.write("Null2 [label=\"null\"];\n")
        # EL PRIMERO APUNTA A NULL (1ER NULL QUE SE CREO)
        # f.write("\"" + temp.valor + "\"" + " -> Null1; \n")
        # RELACIONES ENTRE NODOS
        while temp:
            temp2 = temp.siguiente
            f.write(" \"" + temp.dato + "\" -> \"" + temp2.dato + "\"; \n")
            temp = temp.siguiente
            if temp == self.primero:
                break

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

#pila = Stack()  # Creamos una instancia de la pila

# ingresamos algunos elementos a la pila
#pila.push('a')
#pila.push('b')
#pila.push('c')

#pila.print_stack()  # Mostramos los elementos de la pila

#pila.pop()  # Utilizamos el metodo pop
#pila.print_stack()  # Mostramos nuevamente los elementos de la pila
