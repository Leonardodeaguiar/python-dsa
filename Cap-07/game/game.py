# pylint: disable
from random import randint


lista_de_palavras = [
    "O Poderoso Chefão",
    "O Mágico de Oz",
    "Cidadão Kane",
    "Um sonho de liberdade",
    "Pulp Fiction",
    "Casablanca",
    "O Poderoso Chefão 2",
    "E T",
    "2001 Uma odisseia no espaço",
    "A lista de Schindler",
    "Guerra nas estrelas",
    "De volta para o futuro",
    "Os caçadores da Arca Perdida",
    "Forrest Gump",
    "E o vento levou",
    "O sol é para todos",
    "Apocalypse Now",
    "Noivo neurótico, noiva nervosa",
    "Os bons companheiros",
    "A felicidade não se compra",
    "Chinatown",
    "O silêncio dos inocentes",
    "Lawrence da Arábia",
    "Tubarão",
    "A noviça rebelde",
    "Cantando na chuva",
    "Clube dos cinco",
    "A primeira noite de um homem",
    "Blade Runner - O caçador de andróides",
    "Um estranho no ninho",
    "A princesa prometida",
    "Star Wars Episódio V O Império Contra-Ataca",
    "Fargo",
    "Beleza americana",
    "Laranja mecânica",
    "Curtindo a vida adoidado",
    "Dr. Fantástico",
    "Harry & Sally Feitos um Para o Outro",
    "O iluminado",
    "O clube da luta",
    "Psicose",
    "Alien",
    "Toy Story",
    "Matrix",
    "Titanic",
    "O resgate do soldado Ryan",
    "Quanto mais quente melhor",
    "Os suspeitos",
    "Janela indiscreta",
    "Jurassic Park",
    "O grande Lebowski",
    "A malvada",
    "Gênio indomável",
    "Butch Cassidy",
    "Taxi Driver",
    "Brilho eterno de uma mente sem lembranças",
    "O cavaleiro das trevas",
    "Crepúsculo dos deuses",
    "Thelma e Louise",
    "O fabuloso destino de Amelie Poulain",
    "Amor, sublime amor",
    "Intriga internacional",
    "Feitiço do tempo",
    "Mary Poppins",
    "Touro indomável",
    "O Rei Leão",
    "Avatar",
    "Monty Python e o cálice sagrado",
    "Gladiador",
    "Um corpo que cai",
    "Quase famosos",
    "O jovem Frankenstein",
    "Todos os homens do presidente",
    "Banzé no Oeste",
    "A ponte do Rio Kwai",
    "Brokeback Mountain",
    "Os caça fantasma",
    "12 homens e uma sentença",
    "Wall E",
    "Sindicato dos ladrões",
    "Amadeus",
    "O Senhor dos Anéis A sociedade do anel",
    "Duro de matar",
    "Inception",
    "Seven",
    "A bela e a fera",
    "Quem quer ser um milionário",
    "Coração selvagem",
    "Amnésia",
    "Rocky: O lutador",
    "Up",
    "Contatos imediatos do terceiro grau",
    "O franco atirador",
    "Doutor Jivago",
    "O labirinto do fauno",
    "Apertem os cintos O piloto sumiu",
    "Cães de aluguel",
    "Bonnie e Clyde",
    "Os sete samurais",
]


class Game(object):
    def __init__(self, palavras) -> None:
        self.frase = list(palavras[randint(0, len(palavras))])

    def start_game(self):
        nome = "".join(self.frase).lower()
        segredo = list("-" * len(self.frase))
        contador = 0
        pessoinha = ["...O...", "../|\..", "...|...", "../.\..", "..-.-.."]

        while True:
            if "-" not in segredo:
                print("Cê ganhou rapaz!")
                break

            for i in range(len(pessoinha) - contador):
                print(pessoinha[i])

            for i, k in enumerate(self.frase):
                if self.frase[i] == " ":
                    segredo[i] = " "

            print("A pista é Filmes.")
            print("".join(segredo))
            print("".join(self.frase))

            letra = input("Digite uma letra: ")[0]
            if letra not in self.frase:
                contador += 1
            else:
                for item in self.frase:
                    if item == letra:
                        segredo[self.frase.index(letra)] = letra
                        self.frase[self.frase.index(letra)] = "-"

            if contador > 4:
                print("Perdeu! A palavra era: " + "".join(nome))
                break


if __name__ == "__main__":
    forca = Game(lista_de_palavras)
    forca.start_game()
