from entrada.interpretador import Interpretador

class Cena(object):
    def __init__(self):
        self.interpretador = Interpretador.getInstance()

    def testaComandoCerto(self, acao, objeto):
        comando = self.interpretador.obtemComando()
        return (comando.obtemAcao() == acao)and(comando.obtemObjeto() == objeto)

    def acabou(self):
        return False
