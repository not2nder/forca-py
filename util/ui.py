import os

from util import pretty

cols, lines = os.get_terminal_size()

def header():
    texto = "JOGO DA FORCA"
    creditos = "Desenvolvido por not2nder"

    gap = (cols//2) - len(texto) - (len(texto)//2)

    titulo = pretty.justify(texto, creditos, width=(cols//2)+len(texto))
    
    resto = cols-(len(titulo))
    pretty.sprint(pretty.reverse(f"{titulo}{' '*resto}"))

def footer():
    pretty.cprint(pretty.justify(pretty.bold("Sair:"), pretty.dim("<Ctrl + C>"), width= 25), 10)
    pretty.cprint(pretty.justify(pretty.bold("Ajuda:"), pretty.dim("<Ctrl + X>"), width=25), 11)

def draw(tentativas: int):    
    match tentativas:
        case 4:
            ascii_art =  """
            ________
            |      |
            |          
            |   
            |       
            |
            |
            ██████████
            ████████████
            """
        case 3:
            ascii_art =  """
            ________
            |      |
            |     (_)
            |          
            |       
            |
            |
            ██████████
            ████████████
            """
        case 2:
            ascii_art =  """
            ________
            |      |
            |     ( )
            |      | 
            |      |
            |       
            |
            ██████████
            ████████████
            """
        case 1:
            ascii_art =  """
            ________
            |      |
            |     ( )
            |     /|\\  
            |      |
            |      
            |
            ██████████
            ████████████
            """
        case 0:
            ascii_art =  """
            ________
            |      |
            |     ( )
            |     /|\\
            |      |
            |     / \\
            |
            ███████████
            █████████████
            """

    footer()
    header()
    
    linhas = [linha.strip() for linha in ascii_art.strip().splitlines()]
    
    largura = max(len(linha) for linha in linhas)
    altura = len(linhas)
    
    l_inicial = 4
    c_inicial = (cols//2) - (largura//2)
    
    for i, linha in enumerate(linhas):
        print(f"\x1b[{l_inicial+i};{c_inicial}H{linha}",end="")

    print("\n")

