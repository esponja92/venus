class Acao(object):
    # variáveis estáticas para ação
    SAIR = 1

    tradutor = {'sair' : SAIR}

    @staticmethod
    def getAcao(acao):
        return Acao.tradutor[acao]
