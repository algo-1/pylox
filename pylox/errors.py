class PyloxError:
    had_error = False

    @staticmethod
    def error(line: int, message: str):
        PyloxError.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f"[line {line}] Error{where}: {message}")
        PyloxError.had_error = True
