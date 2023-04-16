import random
import os

from palavras import *

numeroSecreto = random.randint(0, 9)
PalavraSecreta = palavras[numeroSecreto]
DicaSecreta = dicas[numeroSecreto]

letrasDigitadas = []

def clear():
    os.system("cls")

while True:
    print("=-" * 30)
    print(f"Dica: {DicaSecreta}")
    letraDigitada = input("Digite uma letra: ")
    if len(letraDigitada) != 1 or letraDigitada.isdigit():
    
        print("Digite apenas uma LETRA!")
        continue

    if letraDigitada not in letrasDigitadas:
        letrasDigitadas.append(letraDigitada)

    palavraFormada = ""
    for letra in PalavraSecreta:
        if letra in letrasDigitadas:
            palavraFormada += letra
        else:
            palavraFormada += "*"
    
    clear()
    if palavraFormada == PalavraSecreta:
        
        print("🎉Parabéns! Você ganhou!🎉")
        break
    else:
        print(palavraFormada)
    
