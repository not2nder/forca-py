import os
import sys
import time
import random

from util import ui

tentativas = 4
adivinhado = False
entradas = set()

with open('palavras.txt', 'r') as f:
    lista = f.readlines()
    palavra = random.choice(lista).strip()

resposta = "_" * len(palavra)

while True:
    try:
        ui.ascii(tentativas)  

        print(f"Tentativas: {tentativas}")
    
        print(f"Letras: {', '.join(sorted(entradas))}")

        print(resposta)
        char = input("Digite uma letra: ").lower()[0]
    

        if char in entradas:
            print(f"A letra {char} já foi!")
            time.sleep(1)
            continue

        elif not char.isalpha():
            print("Entrada inválida")
            time.sleep(1)
            continue
    
        else:
            for i, letra in enumerate(palavra):
                if letra == char:
                    resposta = resposta[:i] + char + resposta[i+1:]

            if not char in palavra:
                tentativas -= 1
    
            adivinhado = palavra == resposta

            entradas.add(char)
        
            if adivinhado or tentativas == 0:
                mostrar_ascii(tentativas)
                break
    except KeyboardInterrupt:
        sys.exit(0)

print(f"A palavra era: {palavra}")
