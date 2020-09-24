import random

def generarBaraja():
  return [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"] * 4

def veintiuna(baraja, manoJugador, manoMaquina):
  print(baraja)
  if esPrimeraRonda(manoJugador, manoMaquina):
    return veintiuna(baraja, [baraja.pop(), baraja.pop()], [baraja.pop(), baraja.pop()])
  
  if manoSePaso(manoJugador):
    return print ('Jugador Perdió', sumar(manoJugador))
  
  print(manoJugador) 
  if jugadorDeseaOtraCarta():
    manoJugador.append(baraja.pop())
    return veintiuna(baraja, manoJugador, manoMaquina)
  else:
    print ('Jugador Planta')

def jugadorDeseaOtraCarta(): 
  if input ("Desea otra carta? ") == "Y":
    return True
  else:
    return False

def manoSePaso (mano):
  return sumar(mano) > 21

def esPrimeraRonda(manoJugador, manoMaquina):
  return manoJugador is None and manoMaquina is None

def sumar(mano):
  if (len(mano) == 1):
    return interpretador(mano[0])
  else:
    print(interpretador(mano[0]))
    return interpretador(mano[0]) + sumar(mano[1:])

def interpretador(carta):
  print(carta)
  if(carta == "K" or carta == "Q" or carta == "J"):
    return 10
  elif carta == "A":
    return 1
  else:
    return carta

veintiuna(generarBaraja(), None, None)
