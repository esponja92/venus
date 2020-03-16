from entrada.interpretador import Interpretador

from custom_exceptions.entrada_exceptions import *
from cenas.cena_um import CenaUm

if __name__ == "__main__":

    cena = CenaUm()

    # loop principal
    while(cena.acabou() == False):
        try:
            cena = cena.obtemProximaCena()

        except (InterpretadorException, Exception) as e:
            print("Erro => "+str(e))

    print('''
    "Vênus" por Hugo de Mello Dantas
    março/2020
    ''')
