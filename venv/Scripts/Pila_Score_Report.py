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


pila = Stack()  # Creamos una instancia de la pila

# ingresamos algunos elementos a la pila
pila.push('a')
pila.push('b')
pila.push('c')

pila.print_stack()  # Mostramos los elementos de la pila

pila.pop()  # Utilizamos el metodo pop
pila.print_stack()  # Mostramos nuevamente los elementos de la pila
