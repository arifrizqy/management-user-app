# Built-in library
from os import name as os_name

# My library
from helper import clear_screen


def App():
    clear_screen(os_name)


if __name__ == "__main__":

    App()
