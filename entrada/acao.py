class Acao(object):
    # variáveis estáticas para ação
    SAIR = 1
    LER = 2

    tradutor = {'sair' : SAIR,'ler':LER}

    @staticmethod
    def getAcao(acao):
        return Acao.tradutor[acao]
