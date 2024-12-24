from pylox.scanner import Scanner
from pylox.token import Token


class Lox:
    had_error = False

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens: list[Token] = scanner.scan_token()

        print(source)

    @staticmethod
    def run_file(file):
        with open(file, "r") as f:
            code = f.read()
            Lox.run(code)

    @staticmethod
    def run_prompt():
        while True:
            try:
                code = input("> ")
                if code == "exit":
                    print("Goodbye!")
                    break

                Lox.run(code)

            except EOFError:
                print("Goodbye!")
                break
