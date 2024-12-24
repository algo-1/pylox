from pylox.error import ErrorHandler
from pylox.scanner import Scanner
from pylox.token import Token


class Lox:

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens: list[Token] = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def run_file(file):
        with open(file, "r") as f:
            code = f.read()
            Lox.run(code)

            # If there was an error, exit with status 65
            if ErrorHandler.had_error:
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
                ErrorHandler.had_error = False

            except EOFError:
                print("Goodbye!")
                break
