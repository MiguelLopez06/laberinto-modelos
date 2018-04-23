class Nodo:
    def __init__ (self, valor, izq = None, der = None):
        self.valor = valor
        self.izquierda = izq
        self.derecha = der

def buscar(arbol,valor):
    if arbol == None:
        return false
    if arbol.valor == valor:
        return true
    if valor < arbol.valor:
        return buscar(arbol.izquierda, valor)
    return buscar(arbol.derecha,valor)

def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if valor < arbol.valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)
    return Nodo(arbol.valor, arbol.izquierda, insertar (arbol.derecha,valor))

def listaAArbol(arbol, lista):
    if lista == []:
        return arbol
    return listaAArbol(insertar(arbol, lista[0]), lista[1:])

def inorden(arbol):
    if arbol != None:
        inorden(arbol.izquierda)
        print(arbol.valor)
        inorden(arbol.derecha)

def preorden(arbol):
    if arbol != None:
        print(arbol.valor)
        preorden(arbol.izquierda)
        preorden(arbol.derecha)

def posorden(arbol):
    if arbol != None:
        posorden(arbol.izquierda)
        posorden(arbol.derecha)
        print(arbol.valor)


