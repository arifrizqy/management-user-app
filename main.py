from os import system
from os import name as os_name

if __name__ == "__main__":

    operating_system = os_name

    match operating_system:
        case "posix":
            system("clear")
        case "nt":
            system("cls")

    print("Hello, World!")
