import os

cols, lines = os.get_terminal_size()

def render():
    header()
    footer()

def header():
    texto = "JOGO DA FORCA"

    gap = (cols//2)-(len(texto)//2)

    print(f"\x1b[7m{' '*(gap-1 if cols%2==0 else gap)}{texto}{' '*gap}\x1b[0m", end="")

def footer():
    aviso = "[Pressione ^C para sair.]"
    print(f"\x1b[7m\x1b[3;{(cols//2)-(len(aviso)//2)}H{aviso}\x1b[0m", end="")

def ascii(tentativas: int):
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

    os.system("cls" if os.name == "nt" else "clear")

    render()
    
    linhas = ascii_art.strip().splitlines()
    
    largura = max(len(linha) for linha in linhas)
    altura = len(linhas)
    
    l_inicial = 4
    c_inicial = (cols//2) - (largura//2)
    
    for i, linha in enumerate(linhas):
        print(f"\x1b[{l_inicial+i};{c_inicial}H{linha}",end="")

    print("\n")
