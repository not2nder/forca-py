import sys
import os
import time
import random

from util import ui
from util import pretty

tentativas = 4
adivinhado = False
entradas = set()

with open('palavras.txt', 'r') as f:
    lista = f.readlines()
    palavra = random.choice(lista).strip()

resposta = "_" * len(palavra)

os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        ui.draw(tentativas)

        pretty.printf(f"Tentativas: {tentativas}", 0)
    
        pretty.printf(f"Letras: {', '.join(sorted(entradas))}", 2)

        pretty.printf(resposta,4)
        
        char = pretty.scanf("Digite uma letra: ", 6).lower()[0]
    

        if char in entradas:
            pretty.printf(f"A letra {char} já foi!", 8)
            continue

        elif not char.isalpha():
            pretty.printf("Entrada inválida", 6)
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
                ui.draw(tentativas)
                break
            
    except KeyboardInterrupt:
        sys.exit(0)

print(f"A palavra era: {palavra}")
