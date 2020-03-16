import sys
from entrada.comando import Comando
from custom_exceptions.entrada_exceptions import *
from entrada.acao import Acao
from entrada.objeto import Objeto


class Interpretador(object):

    PREPOSICOES = ['a', 'ante', 'após', 'até', 'com', 'contra', 'de', 'do', 'da', 'dos', 'das', 'dum', 'duns', 'duma', 'dumas', 'desde', 'em', 'no', 'na',
                   'nos', 'nas', 'num', 'nuns', 'numa', 'numas', 'entre', 'para', 'per', 'pelo', 'pelos', 'pela', 'pelas', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás']

    ARTIGOS = ['o', 'a', 'os', 'as', 'um', 'uns', 'uma', 'umas']

    def __init__(self):
        pass

    def obtemComando(self):
        print("O que você deseja fazer?")
        entrada_do_jogador = input("=> ")
        termos = entrada_do_jogador.lower().split()
        for preposicao in self.PREPOSICOES:
            if preposicao in termos:
                termos.remove(preposicao)

        for artigo in self.ARTIGOS:
            if artigo in termos:
                termos.remove(artigo)

        acao = ''
        if termos[0] in Acao.tradutor.keys():
            acao = Acao.getAcao(termos[0])
        else:
            raise InterpretadorException(
                "Ação não reconhecida pelo interpretador.")

        objeto = ''
        if termos[1] in Objeto.tradutor.keys():
            objeto = Objeto.getObjeto(termos[1])
        else:
            raise InterpretadorException(
                "Objeto não reconhecido pelo interpretador.")

        if((acao == Acao.SAIR)and(objeto == Objeto.JOGO)):
            print("Até logo!")
            sys.exit()

        return Comando(acao, objeto)
