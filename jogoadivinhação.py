import random
from abc import ABC, abstractmethod

class Jogo(ABC):

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


class JogoAdivinhacao(Jogo):

    ranking = []

    def __init__(self):
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0
        self.__limite = 10
        self.__pontuacao = 100
        self.__nome = ""

    def iniciar(self):
        print("Jogo de advinhação")
        self.__nome = input("Digite seu nome: ")
        print(f"Bem-vindo, {self.__nome}!")
        print("Tente adivinhar o número entre 1 e 100")
        print("Você tem", self.__limite, "tentativas")

    def jogar(self):
        while self.__tentativas < self.__limite:
            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Digite um número válido!")
                continue

            self.__tentativas += 1
            self.__pontuacao -= 10

            if palpite == self.__numero_secreto:
                print("Parabéns, Você acertou!")
                self.__pontuacao += 20
                break
            elif palpite < self.__numero_secreto:
                print("O número secreto é MAIOR")
            else:
                print("O número secreto é MENOR")
        else:
            print("Você perdeu!")
            print("O número era:", self.__numero_secreto)

        self.salvar_ranking()
        print(f"Sua pontuação: {self.__pontuacao}")

    def salvar_ranking(self):
        JogoAdivinhacao.ranking.append({
            "nome": self.__nome,
            "pontuacao": self.__pontuacao
        })

        JogoAdivinhacao.ranking.sort(
            key=lambda x: x["pontuacao"],
            reverse=True
        )

    def exibir_ranking(self):
        print("\nRANKING")
        for i, jogador in enumerate(JogoAdivinhacao.ranking, start=1):
            print(f"{i}º - {jogador['nome']} ({jogador['pontuacao']} pts)")


def executar_jogo(jogo: Jogo):
    jogo.iniciar()
    jogo.jogar()
    jogo.exibir_ranking()


jogo = JogoAdivinhacao()
executar_jogo(jogo)