import sys
from entrada.interpretador import Interpretador
from entrada.acao import Acao
from entrada.objeto import Objeto
from cenas.cena import Cena
from cenas.cena_fim import CenaFim


class CenaUm(Cena):

    def obtemProximaCena(self):
        print("Aqui está o início da primeira cena.")

        while(self.testaComandoCerto(Acao.LER, Objeto.LIVRO) == False):
            print("Isso não funcionou")

        print("Aqui está o final da primeira cena.")

        return CenaFim()
