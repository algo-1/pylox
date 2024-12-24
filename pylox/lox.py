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

            # If there was an error, exit with status 65
            if Lox.had_error:
                exit(65)

    @staticmethod
    def run_prompt():
        while True:
            try:
                line = input("> ")
                if line == "exit":
                    print("Goodbye!")
                    break

                # Run the input
                Lox.run(line)

                # Reset the error flag
                Lox.had_error = False

            except EOFError:
                print("Goodbye!")
                break

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f"[line {line}] Error {where}: {message}")
        Lox.had_error = True

    @staticmethod
    def error(line: int, message: str):
        Lox.report(line, "", message)
