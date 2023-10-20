# pylint: disable
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from random import randint

# Board (tabuleiro)
board = [
    """

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========""",
    """

+---+
|   |
O   |
    |
    |
    |
=========""",
    """

+---+
|   |
O   |
|   |
    |
    |
=========""",
    """

 +---+
 |   |
 O   |
/|   |
     |
     |
=========""",
    """

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========""",
    """

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========""",
    """

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========""",
]


# Classe
class Hangman(object):
    # Método Construtor
    def __init__(self, palavra) -> None:
        self.palavra = list(palavra)
        self.segredo = list("-" * len(self.palavra))
        self.erros = []

    # Método para adivinhar a letra
    def advinha_letra(self):
        letra = input("Digite uma letra: ")[0]
        if letra in self.palavra:
            for l in self.palavra:
                if letra == l:
                    self.segredo[self.palavra.index(letra)] = letra
                    self.palavra[self.palavra.index(letra)] = "-"
        else:
            self.erros.append(letra)

    # Método para verificar se o jogo terminou
    def fim_de_jogo(self, erros):
        if len(erros) > 6:
            print("fim de Jogo")
            return True

    # Método para verificar se o jogador venceu
    def venceu(self):
        if "-" not in self.segredo:
            print("Venceu!")
            return True

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        i = len(board) - len(self.erros) - 1
        print(board[i])
        print("".join(self.segredo))


def main():
    game = Hangman(rand_word())

    while not game.fim_de_jogo(game.erros):
        game.status()

        game.advinha_letra()

        if game.venceu():
            break


def rand_word():
    frutas = ["uva", "pera", "banana", "maça", "melancia", "kiwi"]
    return frutas[randint(0, len(frutas))]


if __name__ == "__main__":
    main()
