# Built-in library
from os import system


def clear_screen(os_type: str):
    system("clear") if os_type == "posix" else system("cls")
