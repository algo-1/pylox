class ErrorHandler:
    had_error = False

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f"[line {line}] Error {where}: {message}")
        ErrorHandler.had_error = True

    @staticmethod
    def error(line: int, message: str):
        ErrorHandler.report(line, "", message)
