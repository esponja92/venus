import sys
from comandos.interpretador import Interpretador

if __name__ == "__main__":

    interpretador = Interpretador()

    # loop principal
    while(1):
        print("O que você deseja fazer?")
        comando = interpretador.obtemComando()
        if((comando.obtemAcao() == 'sair')and(comando.obtemObjeto() == 'jogo')):
            sys.exit()
