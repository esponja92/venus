import sys
from entrada.interpretador import Interpretador
from entrada.comando import Comando
from entrada.acao import Acao
from entrada.objeto import Objeto
from entrada import *
from custom_exceptions.entrada_exceptions import *

if __name__ == "__main__":

    interpretador = Interpretador()

    # loop principal
    while(1):
        print("O que você deseja fazer?")
        try:
            comando = interpretador.obtemComando()
            if((comando.obtemAcao() == Acao.SAIR)and(comando.obtemObjeto() == Objeto.JOGO)):
                sys.exit()
        except (InterpretadorException, Exception) as e:
            print("Erro => "+str(e))
