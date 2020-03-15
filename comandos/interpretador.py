from comandos.comando import Comando


class Interpretador(object):
    def __init__(self):
        pass

    def obtemComando(self):
        entrada_do_jogador = input("=> ")
        return Comando('sair', 'jogo')
