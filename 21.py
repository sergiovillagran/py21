import random
lista = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"] + [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"] +[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"] + [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(lista)

def veintiuna(lista, manoJugador, manoMaquina):
        if (sumar(manoJugador) > 21):
                print ('Jugador Perdió', sumar(manoJugador))
        else:
                print(manoJugador) 
                if ( preguntar() == 1 ):
                        manoJugador.append(lista.pop())
                        veintiuna(lista, manoJugador, manoMaquina)
                else:
                        print ('Jugador Planta')

def preguntar(): 
        if input ("Desea otra carta? ") is "Y":
                return 1
        else:
                return 0

def sumar(mano):
        if (len(mano) == 1):
                return interpretador(mano[0])
        else:                
                return interpretador(mano[0]) + sumar(mano[1:])

def interpretador(carta):
        if(carta == "K" || carta == "Q" || carta == "J"):
                return 10
        else:
                return carta
        


veintinua(lista, [lista.pop(), lista.pop()], [lista.pop(), lista.pop()])
