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

        ui.print_aligned(f"Tentativas: {tentativas}", 0)
    
        ui.print_aligned(f"Letras: {', '.join(sorted(entradas))}", 2)

        ui.print_aligned(resposta,4)
        char = ui.get_input("Digite uma letra: ").lower()[0]
    

        if char in entradas:
            ui.print_aligned(f"A letra {char} já foi!", 6)
            time.sleep(1)
            continue

        elif not char.isalpha():
            ui.print_aligned("Entrada inválida", 6)
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
                ui.ascii(tentativas)
                break
            
    except KeyboardInterrupt:
        sys.exit(0)

print(f"A palavra era: {palavra}")
