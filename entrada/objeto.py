class Objeto(object):
    #variáveis estáticas para os objetos do jogo
    JOGO = 1

    tradutor = {'jogo':JOGO}

    @staticmethod
    def getObjeto(objeto):
        return Objeto.tradutor[objeto]