import json
from getpass import getpass
from os import system

SAVEFILE = "passwd.json"

try:
    with open(SAVEFILE, 'r', encoding='utf-8') as f:
        saved = json.load(f)
except:
    saved = {}


def shift(string: str, amount: int, back: bool = False) -> str:
    amount = int(amount) if not amount.isalpha() and len(amount) > 0 else 404
    amount = amount if not back else -amount
    return "".join([chr(ord(i) + amount) for i in string])


def main() -> None:
    showall: bool = False

    while True:
        system('cls')
        print('Type "help" for help.')

        key = input('key: ').lower()

        if key == "quit" or key[0] == "q":
            break

        elif key == "save" or key[0] == "s":
            with open(SAVEFILE, 'w', encoding='utf-8') as f:
                json.dump(saved, f)

        elif key[0:6] == "toggle" or key[0] == "t":
            args = key.split(" ")
            args.pop(0)

            for i in args:
                if i == "showall":
                    showall = False if showall else True

        elif key == "config":
            print(
                "",
                " Config:",
                f"   showall: {showall}",
                "",
                sep="\n"
            )
            input()

        elif key == "help":
            print(
                "",
                " Type:",
                "   help - shows all available commands",
                "   save or s - saves all changes made",
                "   quit or q - closes the program",
                "   toggle or t [args] - toggles the args",
                "   config - prints out config",
                "",
                sep="\n"
            )
            input()

        elif key in saved.keys():
            pin = getpass("pin: ")
            passwd = shift(saved[key], pin, True)

            if showall:
                print(passwd)
            else:
                slicestart = input('from index: ')
                sliceend = input('to index: ')

                slicestart = int(slicestart) if not slicestart.isalpha() else 0
                sliceend = int(sliceend) if not sliceend.isalpha() else 0

                print(passwd[slicestart:sliceend])
            input()

        elif len(key) > 0:
            pin = getpass("pin: ")
            passwd = shift(getpass(), pin)

            saved[key] = passwd


if __name__ == "__main__":
    main()
