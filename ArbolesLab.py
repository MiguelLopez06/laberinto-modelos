def colocarArbol(x,y):
        raiz.setPosicion((x,y))
        arbol.setPosicion((x,y))
        raiz.setHijos([verIzquierda(x,y,arbol),verAbajo(x,y,arbol),verArriba(x,y,arbol),verDerecha(x,y,arbol)])

        return ""


def validarVecinos (laberinto,posicion, arbol):
    arriba=[posicion[0],posicion[1]-1]
    abajo= [posicion[0],posicion[1]+1]
    derecha= [posicion[0]+1,posicion[1]]
    izquierda= [posicion[0]-1,posicion[1]]
 
    if ("x" in laberinto[posicion[0]][posicion[1]] or "0" in laberinto[posicion[0]][posicion[1]]):
        print(listarArbol(arbol))
        validarVecinos(laberinto,arriba,insertar(arbol , arriba))
        validarVecinos(laberinto,abajo,insertar(arbol , abajo))
        validarVecinos(laberinto,derecha,insertar(arbol , derecha))
        validarVecinos(laberinto,izquierda,insertar(arbol , izquierda))
        if laberinto[posicion[0]-1][posicion[1]]=="0":           
            print("gola1")
            arbol = insertar(arbol,[posicion[0]-1,posicion[1]])
            return validarVecinos(laberinto,[4,4],arbol)
        if laberinto[posicion[0]][posicion[1]-1]=="0":
            print("gola2")
            arbol = insertar(arbol, [[posicion[0]],[posicion[1]-1]])
            return validarVecinos(laberinto,[posicion[0],posicion[1]-1],arbol)
        if laberinto[posicion[0]+1][posicion[1]]=="0":
            print("gola3")
            arbol = insertar(arbol, [[posicion[0]+1],[posicion[1]]])
            return validarVecinos(laberinto,[posicion[0]+1,posicion[1]],arbol)
        if laberinto[posicion[0]][posicion[1]+1]=="0":
            print("gol4a")
            arbol = insertar(arbol, [[posicion[0]],[posicion[1]+1]])
            return validarVecinos(laberinto,[posicion[0],posicion[1]+1],arbol)
    return arbol;



def buscar(nodo, valor, camino):
    if nodo == None:
        return False

    if nodo.valor[0] == valor:
        camino.append(nodo.valor[1])
        return True

    if nodo.hijos == []:
        return False

    if buscar(nodo.hijos[0], valor, camino) or buscar(nodo.hijos[1], valor, camino)\
    or buscar(nodo.hijos[2], valor, camino) or buscar(nodo.hijos[3], valor, camino):
        camino.append(nodo.valor[1])
        return reversar(camino)

    return False


def crearLab():
    return SaltoLinea([y.strip("\n") for y in open("laberintomodelos.txt", "r").readlines()])



def hijob(tabla,valor):
    if tabla == []:
        return False
    return (buscar(tabla[0],valor) or hijob(tabla[1:],valor))
        
def buscar(extension,valor):
    if extension.valor == valor:
        return True
    else:
        return hijob(extension.hijos,valor)

def enListaDeListas(lista, v, f, c):
    if len(lista) == f:
        return 0, -1

    if len(lista[f]) == c:
        return enListaDeListas(lista, v, f + 1, 0)

    if (lista[f][c] == v):
        return f, c

    return enListaDeListas(lista, v, f, c + 1)

def agregar(valor, lista):
    lista.append(valor)
    return lista

def parametros(lista):
    return (lista,*enListaDeListas(lista, "x", 0, 0))


def hijop(tabla):
    if tabla == []:
        return []
    return [imp(tabla[0])+hijop(tabla[1:])]        

def adelante(tabla1,tabla2):
    if len(tabla2)>len(tabla1):
        return adelante(tabla2,tabla1)
    if tabla2==[]:
        return tabla1
    return tabla1[0]+tabla2[0] + adelante(tabla1[1:],tabla2[1:])
def SaltoLinea(tabla):
    if tabla==[]:
         return []
    return [tabla[0].split(" ")]+SaltoLinea(tabla[1:])

def caminoSimilar(valor, hijos):
    if len(hijos)==0:
        return [[]]
    if len(hijos)==1:
        return [[valor]+hijos[0]]
    return [[valor]+hijos[0]]+caminoSimilar(valor,hijos[1:])

def Despejar(tabla):
    if len(tabla)==0:
        return []
    if len(tabla[0])==0:
        return Despejar(tabla[1:])
    if ultimoVal(tabla[0]):
        return [tabla[0]]+Despejar(Despejar(tabla[1:]))



def BloqueoMov(tabla,laberinto):
 
    if tabla==[]:
        return []
    if laberinto[tabla[0][len(tabla[0])-1][0]][tabla[0][len(tabla[0])-1][1]]=='x':
        return [tabla[0]]+BloqueoMov(tabla[1:],laberinto)
    else:
        return BloqueoMov(tabla[1:],laberinto)




class Lab:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos


def verticals(laberinto):
      
    if laberinto[0][0]=='y':
        return [0,0]
    if len(laberinto[0])==1:

        return movimientoposicion(movimientoposicion([1,0],verticals(laberinto[1:]) ),[0,-(len(laberinto[1])-1)])
    if laberinto[0]!=[] :

        return  movimientoposicion ([0,1],verticals([laberinto[0][1:]]+laberinto[1:]))    
    else:
        return [0,0]
    
def movimientoposicion(coor1,coor2):
    return [coor1[0]+coor2[0],coor1[1]+coor2[1]]

def iniciar():
    print(BloqueoMov(graficarrama(armarLab(verticals(crearLab()), crearLab())),crearLab()))
    

    

def armarLab(cabeza,laberinto):
    if laberinto[cabeza[0]][cabeza[1]]=='1' or laberinto[cabeza[0]][cabeza[1]]=='>'  :
        return Lab(cabeza,[])
        
    if laberinto[cabeza[0]][cabeza[1]]=='x':
        print(graficar(laberinto))
        return Lab(cabeza,[])

    return Lab(cabeza,[armarLab(movimientoposicion(cabeza,[0,1]),remplazovalor(laberinto, cabeza)),armarLab(movimientoposicion(cabeza,[1,0]),remplazovalor(laberinto, cabeza)) ,armarLab(movimientoposicion(cabeza,[0,-1]),remplazovalor(laberinto, cabeza)),armarLab(movimientoposicion(cabeza,[-1,0]),remplazovalor(laberinto, cabeza))  ])
    
def remplazovalor(laberinto, coor):
    if coor[0]==0 and coor[1]==0:
        return [['>']+laberinto[0][1:]]+laberinto[1:]
    if coor[0]!=0:
        return [laberinto[0]] + remplazovalor(laberinto[1:],movimientoposicion(coor, [-1,0]))
    return [[laberinto[0][0]]+remplazovalor([laberinto[0][1:]], movimientoposicion(coor, [0,-1]))[0]] + laberinto[1:]


    

def graficar(laberinto):
   
    if(len(laberinto)==0):
        return "--Posible Camino--" 
    if(len(laberinto[0])==0):
        return "\n"+graficar(laberinto[1:])
        
    return laberinto[0][0]+" "+graficar([(laberinto[0])[1:]]+laberinto[1:])
    


def graficarrama(extension):
    
    if(extension.hijos==[]):
        return [[extension.valor]]
    if len(extension.hijos)==1:
        return caminoSimilar(extension.valor,graficarrama(extension.hijos[0]))
        
    return caminoSimilar(extension.valor,graficarrama(extension.hijos[0])) +graficarrama (Lab(extension.valor,extension.hijos[1:]))


    

iniciar()
