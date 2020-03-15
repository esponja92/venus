class Comando(object):
    __acao = ''
    __objeto = ''

    def __init__(self, acao, objeto):
        self.__acao = acao
        self.__objeto = objeto

    def obtemAcao(self):
        return self.__acao

    def obtemObjeto(self):
        return self.__objeto
