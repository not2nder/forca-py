import sys
import argparse

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
        
        pretty.cprint(f"Letras: {', '.join(sorted(i if i in palavra else pretty.red(i) for i in entradas))}", 2)

        pretty.cprint(resposta,4)

        pretty.cprint(pretty.justify(pretty.bold("Sair:"), pretty.dim("<Ctrl + C>"), width= 25), 10)
        # todo
        pretty.cprint(pretty.justify(pretty.bold("Ajuda:"), pretty.dim("<Ctrl + X>"), width=25), 11)
        
        char = pretty.scanf("Digite uma letra: ", 6).lower()[0]
        

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
