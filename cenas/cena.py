class Cena(object):
    def __init__(self, interpretador):
        self.interpretador = interpretador

    def testaComandoCerto(self, comando, acao, objeto):
        return (comando.obtemAcao() == acao)and(comando.obtemObjeto() == objeto)

    def acabou(self):
        return False
