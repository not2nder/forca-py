import os

cols, lines = os.get_terminal_size()

def scanf(text: str, offset: int) -> str:
    x = (cols//2) - (len(text)//2)
    y = (lines//2) + offset

    return input(f"\x1b[{y};{x}H{text}")

def printf(text: str, offset: int):
    x = (cols//2) - (len(text)//2)
    y = (lines//2) + offset

    print(f"\x1b[{y};{x}H{text}")
