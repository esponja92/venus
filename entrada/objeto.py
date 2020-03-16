class Objeto(object):
    #variáveis estáticas para os objetos do jogo
    JOGO = 1
    LIVRO = 2

    tradutor = {'jogo':JOGO, 'livro':LIVRO}

    @staticmethod
    def getObjeto(objeto):
        return Objeto.tradutor[objeto]