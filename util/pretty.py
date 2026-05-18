import re
import os

cols, lines = os.get_terminal_size()

def length(text):
    ANSI_ESCAPE = re.compile(r'\x1b\[[0-9;]*m')
    return len(ANSI_ESCAPE.sub('', text))

def scanf(text: str, offset: int) -> str:
    x = (cols//2) - (length(text)//2)
    y = (lines//2) + offset

    return input(f"\x1b[{y};{x}H{text}")

def cprint(text: str, offset: int):

    x = (cols//2) - (length(text)//2)
    y = (lines//2) + offset

    print(f"\x1b[{y};{x}H{text}")

def sprint(text: str, offset = 1):
    print(f"\x1b[1;{offset}H{text}")

def justify(*args, width = 20, padding=2) -> str:
    gap = ((width) - sum(length(arg) for arg in args))-(padding*2)
    
    return f"{' '*padding}{args[0]}{' '*gap}{args[1]}{' '*padding}"

def bold(text: str):
    return f"\x1b[1m{text}\x1b[22m"

def reverse(text: str):
    return f"\x1b[7m{text}\x1b[0m"

def dim(text: str):
    return f"\x1b[38;5;244m{text}\x1b[0m"

def red(text: str):
    return f"\x1b[91m{text}\x1b[0m"

def green(text:str):
    return f"\x1b[32m{text}\x1b[0m"
