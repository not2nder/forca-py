import os

cols, lines = os.get_terminal_size()

def render():
    os.system("cls" if os.name == "nt" else "clear")

    header()
    footer()

def header():
    texto = "JOGO DA FORCA"

    gap = (cols//2)-(len(texto)//2)

    print(f"\x1b[7m\x1b[1;{gap if cols % 2 == 0 else gap-1}H{texto}\x1b[0m", end="")

def footer():
    aviso = "[Pressione Ctrl + C para sair]"

    col = (cols//2)-(len(aviso)//2)
    
    print(f"\x1b[7m\x1b[{lines-1};{col}H{aviso}\x1b[0m", end="")

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

    render()
    
    linhas = [linha.strip() for linha in ascii_art.strip().splitlines()]
    
    largura = max(len(linha) for linha in linhas)
    altura = len(linhas)
    
    l_inicial = 4
    c_inicial = (cols//2) - (largura//2)
    
    for i, linha in enumerate(linhas):
        print(f"\x1b[{l_inicial+i};{c_inicial}H{linha}",end="")

    print("\n")

def get_input(text: str) -> str:
    meio = cols//2
    return input(f"\x1b[{(lines//2)+8};{meio-(len(text)//2)}H{text}");

def print_aligned(text: str, offset:int):
    meio = (cols//2)-(len(text)//2)
    print(f"\x1b[{(lines//2)+offset};{meio}H{text}")

