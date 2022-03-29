from msilib.schema import Class
import random
from re import S
import sys


class Comida():
     
    def __init__(self, posx, posy):
         self.posx = posx
         self.posy = posy
         self.isEat = False
         self.aun_no_comido = 90

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def isComido(self):
        return self.isEat

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def setEat(self):
        self.isEat = True

class Pared():

    def __init__(self, posx, posy,):
         self.posx = posx
         self.posy = posy
         self.isPared = False

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def isnotPared(self):
        return self.isPared

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def setPared(self):
        self.isPared = True

class Player():
    def __init__(self):
        self.nombre = ""
        self.posx = -1
        self.posy = -1
        self.puntos = 0
        self.movimientos = 0
        self.ya_comida = 0
        self.aun_no_comido = 0

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def getMovimientos(self):
        return self.movimientos

    def getPuntos(self):
        return self.puntos

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def addMovimiento(self):
        self.movimientos = self.movimientos + 1

    def addPuntos(self):
        self.puntos = self.puntos + 5
    def ya_comido(self):
        return self.ya_comida

    def getYa_Comido(self):
        self.ya_comida = self.ya_comida+1
    
    def getAunNoComido(self):
        return self.aun_no_comido
    def addAunNoComido(self):
        self.aun_no_comido = self.aun_no_comido-1

### ------ FUNCIONES


def imprimirTablero(tablero):
    for fila in tablero:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} {0[10]} {0[11]} {0[12]} {0[13]} {0[14]}| ".format(fila))

def pintarTablero(lista_comida, jugador,lista_paredes):

    tablero = [
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    ]

    for comida in lista_comida:
        if not comida.isComido():
            tablero[comida.getPosX()][comida.getPosY()] = "@"
    for pared in lista_paredes:
        if not pared.isnotPared():
            tablero[pared.getPosX()][pared.getPosY()] = "#"
    tablero[jugador.getPosX()][jugador.getPosY()] = "C"
    return tablero

def crearListaComidas(lista_comida, comidas: int):
    index = 0
    while index < comidas:

        posx_comida_generada = random.randint(0,14)
        posy_comida_generada = random.randint(0,14)
        estaOcupado = False
        for comidas_busqueda in lista_comida:
            if comidas_busqueda.getPosX() == posx_comida_generada and comidas_busqueda.getPosY() == posy_comida_generada:
                estaOcupado = True
        
        if not estaOcupado:
            comida_creada = Comida(posx_comida_generada, posy_comida_generada)
            lista_comida.append(comida_creada)
            index = index + 1
        jugador.aun_no_comido = index   

def siguienteHayComida(jugador, lista_comida):
    for comida in lista_comida:
        if jugador.getPosX() == comida.getPosX() and jugador.getPosY() == comida.getPosY():
            comida.setEat()
            jugador.getYa_Comido()
            jugador.addAunNoComido()
            jugador.addPuntos()
            return True
    return False

def aunHayComidas(lista_comidas):
    for comida in lista_comidas:
        if not comida.isComido():
            return False
    return True

def crearListaParedes(lista_paredes, paredes: int):
    index = 0
    while index < paredes:

        posx_pared_generada = random.randint(0,14)
        posy_pared_generada = random.randint(0,14)
        estaOcupado = False
        for paredes_busqueda in lista_paredes:
            if paredes_busqueda.getPosX() == posx_pared_generada and paredes_busqueda.getPosY() == posy_pared_generada:
                estaOcupado = True
        
        if not estaOcupado:
            pared_creada = Pared(posx_pared_generada, posy_pared_generada)
            lista_paredes.append(pared_creada)
            index = index + 1

def siguienteHayPared(jugador, lista_paredes):
    for pared in lista_paredes:
        if jugador.getPosX() == pared.getPosX() and jugador.getPosY() == pared.getPosY():
            pared.isnotPared
            return False
    return False
def aunHayPared(lista_paredes):
    for pared in lista_paredes:
        if not pared.isnotPared():
            return False
    return True

def moverArriba(jugador, lista_comidas,lista_paredes):
    posx = jugador.getPosX() - 1
    posy = jugador.getPosY() 

    if posx >=0:
        pared = siguienteHayPared(jugador,lista_paredes)
        if not pared:
            jugador.setPosX(int(posx))
            jugador.setPosY(int(posy))
            movimiento = siguienteHayComida(jugador, lista_comidas)
            jugador.addMovimiento()

def moverDerecha(jugador, lista_comidas,lista_paredes):
    posx = jugador.getPosX() 
    posy = jugador.getPosY() - 1

    if posy >=0:
        pared = siguienteHayPared(jugador,lista_paredes)
        if not pared:
            jugador.setPosX(int(posx))
            jugador.setPosY(int(posy))
            movimiento = siguienteHayComida(jugador, lista_comidas)
            jugador.addMovimiento()

def moverIzquierda(jugador, lista_comidas,lista_paredes):
    posx = jugador.getPosX() 
    posy = jugador.getPosY() + 1

    if posy >=0:
        pared = siguienteHayPared(jugador,lista_paredes)
        if not pared:
            jugador.setPosX(int(posx))
            jugador.setPosY(int(posy))
            movimiento = siguienteHayComida(jugador, lista_comidas)
            jugador.addMovimiento()

def moverAbajo(jugador, lista_comidas,lista_paredes):
    posx = jugador.getPosX() + 1
    posy = jugador.getPosY() 

    if posx >=0:
        pared = siguienteHayPared(jugador,lista_paredes)
        if not pared:
            jugador.setPosX(int(posx))
            jugador.setPosY(int(posy))
            movimiento = siguienteHayComida(jugador, lista_comidas)
            jugador.addMovimiento()

def movimientos(jugador, lista_comidas,lista_paredes):
    menu = """
        _____________________________
        MENU
        1. mover adelante
        2. mover atras
        3. arriba
        4. abajo
        ______________________________
    """

    while True:
        movimiento = input("Movimiento: ")
        """
        primerLugar = -1
        segundoLugar = jugador
        tercerLugar = jugador
         --> 
        try:
            print("2. {0} - {1} MOVIIENTOS - {2} PUNTOS".format(sL.nombre,sL.movimientos,sL.puntos))
        except:
            print("2. ")

            1. Jose 5
            2. Jose 7
            3. Jose 20
            -------------------
            Jose 15
            ---> 3

            Jose 3

            1. Jose 3
            2. Jose 5
            3. Jose 7

            if movimiento == "a": ----- derecha
            elif movimiento == "4":
            elif movimiento == "d":


        posx_jugador = movimiento.split(",")[0]
        posy_jugador = movimiento.split(",")[1]
        jugador.setPosX(int(posx_jugador))
        jugador.setPosY(int(posy_jugador))
        movimiento = siguienteHayComida(jugador, lista_comidas)
        if movimiento:
            jugador.addMovimiento()
        """
        if str(movimiento) == "a" or str(movimiento) == "4":
            moverDerecha(jugador,lista_comidas,lista_paredes)
        elif str(movimiento) == "e":
            jugador = Player()
            juego(jugador)
        elif str(movimiento) == "d" or str(movimiento) == "6":
            moverIzquierda(jugador,lista_comidas,lista_paredes)
        elif str(movimiento) == "w" or str(movimiento) == "8":
            moverArriba(jugador,lista_comidas,lista_paredes)
        elif str(movimiento) == "s" or str(movimiento) == "5":
            moverAbajo(jugador,lista_comidas,lista_paredes)
        print(" "+jugador.nombre+" - PUNTOS: {0} - MOVIMIMENTOS: {1} - COMIDO: {2} - POR COMER {3}".format(jugador.getPuntos(), jugador.getMovimientos(),jugador.ya_comido(),jugador.getAunNoComido()))
        tablero = pintarTablero(lista_comidas, jugador,lista_paredes)
        imprimirTablero(tablero)
        if jugador.getPuntos() >= 40 or aunHayComidas(lista_comidas):
            jugador = Player()
            juego(jugador)
        

def poscionAleatoriaJugador(jugador, lista_comidas):
    while True:
        posx = random.randint(0,12)
        posy = random.randint(0,12)

        isOcupado = False
        for comida in lista_comidas:
            try:
                if comida.posx == posx and comida.posy == posy:
                    isOcupado = True
            except Exception as e:
                """"""
        
        if not isOcupado:
            jugador.setPosX(posx)
            jugador.setPosY(posy)
            break;
            
            

def juego(jugador):
    a=input("""
    --------------------------BIENVENIDO--------------------------
    1.                                                INCIAR JUEGO
    2.                                         TABLA DE POSICIONES
    3.                                                       SALIR
    """)
    if a == "1":
        ### --- definir las comidas
        nombre = input("Cual es tu nombre? ")
        jugador.nombre = nombre.upper()
        comidas_solicitadas = random.randint(1,int((15*15)*0.4))
        lista_comidas = []
        jugador.comidas_solicitadas = comidas_solicitadas
        crearListaComidas(lista_comidas, comidas_solicitadas)
        paredes_solicitadas = random.randint(1,int((15*15)*0.3))
        lista_paredes = []
        crearListaParedes(lista_paredes,paredes_solicitadas)
        poscionAleatoriaJugador(jugador, lista_comidas)
        ### inicializar el tablero de juego
        tablero = pintarTablero(lista_comidas, jugador,lista_paredes)
        imprimirTablero(tablero)
    
        ## logica de juego
        movimientos(jugador, lista_comidas,lista_paredes)

        ## setear tabla posiciones
        #--- unicamente 3 lugares
        
    elif a == "2":
        print("Chale aun no estoy programado :(")
    elif a == "3":
        sys.exit("La ejecución del programa ha finalizado")
    else:
        print("Disculpa pero la opción que ingresaste no existe")
        jugador = Player()
        juego(jugador)
    

#----------------
jugador = Player()
juego(jugador)