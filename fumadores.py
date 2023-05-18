import threading
import time
import random

ingredientes=["tabaco","papel","cerillas", "filtros", "green"]

fumadores=["1","2","3","4", "5"]

def agente():
    while True:
        ingredientesdisponibles=ingredientes.copy()
        ingrediente1=ingredientesdisponibles.pop(ingredientesdisponibles.index(random.choice(ingredientes)))
        ingrediente2=ingredientesdisponibles.pop(ingredientesdisponibles.index(random.choice(ingredientesdisponibles)))

        print( "El agente pone sobre la mesa " + ingrediente1 + " y " + ingrediente2)
        time.sleep(2)

def fumador(nombre, ingrediente1, ingrediente2):
    while True:
        if (ingrediente1 in ingredientes) and (ingrediente2 in ingredientes):
            ingredientes.remove(ingrediente1)
            ingredientes.remove(ingrediente2)
            print("El fumador " + nombre + " se pone a fumar con " + ingrediente1 + " y " + ingrediente2)
            time.sleep(2)
            ingredientes.append(ingrediente1)
            ingredientes.append(ingrediente2)
            print("El fumador " + nombre + " ha terminado de fumar")
            time.sleep(2)
        else:
            print("El fumador " + nombre + " no tiene los ingredientes necesarios para fumar")
            time.sleep(2)

        
