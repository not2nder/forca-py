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
    aviso = "[Pressione Ctrl + C para sair]"

    col = (cols//2)-(len(aviso)//2)
    
    print(f"\x1b[7m\x1b[{lines-1};{col}H{aviso}\x1b[0m", end="")
    
    #pretty.printf(pretty.justify("Sair:","<Ctrl + C>"), lines-2)
    #pretty.printf(pretty.justify("Ajuda:","<Ctrl + X>"), lines-1)


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

    #footer()
    header()
    
    linhas = [linha.strip() for linha in ascii_art.strip().splitlines()]
    
    largura = max(len(linha) for linha in linhas)
    altura = len(linhas)
    
    l_inicial = 4
    c_inicial = (cols//2) - (largura//2)
    
    for i, linha in enumerate(linhas):
        print(f"\x1b[{l_inicial+i};{c_inicial}H{linha}",end="")

    print("\n")

