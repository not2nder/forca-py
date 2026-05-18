import sys

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

print("\x1b[?1049h", end="")

while True:
    try:
        ui.draw(tentativas)

        pretty.cprint(f"{pretty.bold('Tentativas: ')}: {tentativas}", 0)
        
        pretty.cprint(f"Letras: {', '.join(sorted(pretty.green(i) if i in palavra else pretty.red(i) for i in entradas))}", 2)

        pretty.cprint(resposta,4)

        char = pretty.scanf("Digite uma letra: ", 6).lower()
        char = char[0] if char != "" else char

        if char in entradas:
            pretty.cprint(f"A letra {char} já foi!", 8)
            continue

        elif not char.isalpha():
            pretty.cprint("Entrada inválida", 6)
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
                pretty.cprint(f"A palavra era: {palavra}", 6)
                
                ui.draw(tentativas)
                
                pretty.scanf("Aperte enter para sair", 8)

                print("\x1b[?25h", end="")
                print("\x1b[?1049l", end="")
                
                break
            
    except KeyboardInterrupt:
        print("\x1b[?1049l", end="")
        sys.exit(0)
