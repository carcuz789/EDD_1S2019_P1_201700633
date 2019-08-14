import os
class Nodo():
    def __init__(self,valor):
        self.sig=None
        self.ant=None
        self.valor=valor
class Lista():
    def __init__(self):
        self.ini=None
        self.fin=None
        self.size=0

    def addLast(self,valor):
        nuevo=Nodo(valor)
        if self.ini is None:
            self.ini=self.fin=nuevo
        else:
            self.fin.sig=nuevo
            nuevo.ant=self.fin
            self.fin=nuevo
        self.size+=1

    def addFirst(self,valor):
        nuevo=Nodo(valor)
        if self.ini is None:
            self.ini=self.fin=nuevo
        else:
            self.ini.ant=nuevo
            nuevo.sig=self.ini
            self.ini=nuevo
        self.size+=1

    def addPos(self,posicion,valor):
        if posicion > self.size:
            print("Error: Index fuera de rango!")
        else:
            temp=self.ini
            nuevo=Nodo(valor)
            for i in range(0,posicion):
                temp=temp.sig
            anterior=temp.ant
            anterior.sig=nuevo
            nuevo.ant=anterior
            nuevo.sig=temp
            temp.ant=nuevo

    def getPos(self,posicion):
        if posicion > self.size:
            print("Error: Index fuera de rango!")
        else:
            temp=self.ini
            for i in range(0,posicion):
                temp=temp.sig
            print("El valor es: "+temp.valor)
    #ELIMINAR CON UNA POSICION ESPECIFICA
    def delete(self,posicion):
        try:
            if posicion > self.size:
                print("Error: Index fuera de rango!")
            else:
                temp=self.ini
                for i in range(0,posicion):
                    temp=temp.sig
                anterior=temp.ant
                siguiente=temp.sig
                anterior.sig=siguiente
                siguiente.ant=anterior
        except:
            print("")
    #METODO PARA GRAFICAR
    def graph(self):
        #INICIO DE LA LISTA
        temp=self.ini
        #SE CREA EL PUNTO DOT.; W ES PARA ESCRIBIR EN EL ARCHIVO
        f=open("grafico.dot","w")
        #SE INICIA EL DIAGRAMA
        f.write("digraph G {\n")
        #SE ESTABLECE LA FORMA CUADRADA
        f.write("node [shape = square];\n")
        #SE ESTABLECE FORMA HORIZONTAL
        f.write("rankdir=LR;\n")
        #SE CREAN DOS NODOS NULL
        f.write("Null1 [label=\"null\"];\n")
        f.write("Null2 [label=\"null\"];\n")
        #EL PRIMERO APUNTA A NULL (1ER NULL QUE SE CREO)
        f.write("\""+temp.valor+"\""+ " -> Null1; \n")
        #RELACIONES ENTRE NODOS
        for i in range(0,self.size-1):
            temp2=temp.sig
            f.write(" \""+temp.valor+"\" -> \""+temp2.valor+"\"; \n")
            f.write(" \""+temp2.valor+"\" -> \""+temp.valor+"\"; \n")
            temp=temp.sig
        #EL ULTIMO APUNTA A NULL (EL 2DO NULL QUE SE CREO)
        f.write("\""+temp.valor+"\""+" -> "+"Null2; \n")
        #SE CIERRA EL GRAFICO
        f.write("}")
        f.close()
        #SE TRANSFORMA EL .DOT A .JPG (EL NOMBRE .DOT TIENE QUE SER EL DE ARRIBA, EL .JPG PUEDE SER DIFERENTE)
        os.system("dot -Tjpg grafico.dot -o grafico.jpg")
        #SE ABRE EL ARCHIVO .JPG
        os.system("grafico.jpg")
    #IMPRIMIR LISTA
    def printL(self):
        temp=self.ini
        i=0
        print("Lista: ")
        while temp is not None:
            print("Valor: "+temp.valor)
            i+=1
            temp=temp.sig
