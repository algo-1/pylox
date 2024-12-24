from pylox.token import Token


class Scanner:

    def __init__(self, source: str):
        self.source = source
        self.tokens: list[Token] = []

    def scan_token(self) -> list[Token]:
        pass
