# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

from functools import reduce


print("\n******************* Calculadora em Python *******************")


def soma(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def div(a, b):
    print(a / b)


def mult(a, b):
    print(a * b)


def pot(a, b):
    print(a**b)


def calculadora():
    while True:
        operacao = input(
            """
operações disponíveis
+: Adição
-: Subtração
/: Divisão
*: Multiplicacão
**: potência
operação: """
        )
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        if operacao == "+":
            soma(numero1, numero2)
        elif operacao == "-":
            sub(numero1, numero2)
        elif operacao == "/":
            div(numero1, numero2)
        elif operacao == "*":
            mult(numero1, numero2)
        elif operacao == "**":
            pot(numero1, numero2)
        else:
            print("Operação ainda não disponível")

        repetir = input("Deseja efetuar outra operação?[s/n] ").lower()

        if repetir[0] != "s":
            break


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in map(lambda a: a * a, lista):
    print(item)
