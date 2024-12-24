import sys

from pylox.scanner import Scanner
from pylox.token import Token


def run(source: str):
    scanner = Scanner(source)
    tokens: list[Token] = scanner.scan_token()

    print(source)


def run_file(file):
    with open(file, "r") as f:
        code = f.read()
        run(code)


def run_prompt():
    while True:
        try:
            code = input("> ")
            if code == "exit":
                print("Goodbye!")
                break

            run(code)

        except EOFError:
            print("Goodbye!")
            break


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: pylox [script]")
        sys.exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()
