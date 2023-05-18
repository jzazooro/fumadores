import threading
import time
import random
from fumadores import *

def main():
    hiloagente=threading.Thread(target=agente)
    hilofumador1=threading.Thread(target=fumador, args=("1", "papel", "tabaco"))
    hilofumador2=threading.Thread(target=fumador, args=("2", "papel", "cerillas"))
    hilofumador3=threading.Thread(target=fumador, args=("3", "tabaco", "cerillas"))
    hilofumador4=threading.Thread(target=fumador, args=("4", "green", "filtros"))
    hilofumador5=threading.Thread(target=fumador, args=("5", "green", "cerillas"))
    
    hiloagente.start()
    hilofumador1.start()
    hilofumador2.start()
    hilofumador3.start()
    hilofumador4.start()
    hilofumador5.start()
    
    hiloagente.join()
    hilofumador1.join()
    hilofumador2.join()
    hilofumador3.join()
    hilofumador4.join()
    hilofumador5.join()