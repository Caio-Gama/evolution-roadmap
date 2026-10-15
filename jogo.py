# Jogo de adivinhação de números utilizando a biblioteca random
import random

print("Adivinhe o número! ")

segredo = random.randint(1,100)
tentativas = 0
limite = 10
distancia = abs(tentativas - segredo )

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < segredo:
         print("Tente um número maior ")
    elif palpite > segredo:
         print("Tente um número menor ")
    else:
          print("Você acertou!", tentativas)
          break

  
    if tentativas >= limite:
         print("Fim! Era:", segredo)
         break

    if distancia <= 5:
         print("Muito quente!")
    elif distancia <= 15:
         print("Morno")
    else:
         print("Frio")
    