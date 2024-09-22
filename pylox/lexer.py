from enum import Enum, auto, unique
from typing import Literal

from .errors import PyloxError


@unique
class TokenType(Enum):
    # Single-character tokens.
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    # One or two character tokens.
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Literals.
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    # Keywords.
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    EOF = auto()


class Token:

    def __init__(
        self,
        token_type: TokenType,
        lexemme: str,
        literal: object,
        line: int,
    ) -> None:
        self._token_type = token_type
        self._lexemme = lexemme
        self._literal = literal
        self._line = line

    @property
    def token_type(self) -> TokenType:
        return self._token_type

    @property
    def lexemme(self) -> str:
        return self._lexemme

    @property
    def literal(self) -> object:
        return self._literal

    @property
    def line(self) -> int:
        return self._line

    def __str__(self) -> str:
        return f"{self.token_type} {self.lexemme} {self.literal}"


def is_at_end(current, source_length) -> bool:
    return current >= source_length


def match(expected: str, current: int, source: str) -> bool:
    if is_at_end(current, len(source)):
        return False

    if source[current] != expected:
        return False

    return True


def scan_multiple_characters(
    second_char,
    single_token_type,
    double_token_type,
    start,
    current,
    line,
    source,
    tokens,
):
    if match(second_char, current, source):
        # consume second character
        current += 1
        add_token(double_token_type, start, current, line, source, tokens)
    else:
        add_token(single_token_type, start, current, line, source, tokens)

    return current


def scan_token(
    start: int, current: int, line: int, source: str, tokens: list[Token]
) -> int:
    # consume the current character
    char = source[current]
    current += 1

    match char:
        case "(":
            add_token(TokenType.LEFT_PAREN, start, current, line, source, tokens)
        case ")":
            add_token(TokenType.RIGHT_PAREN, start, current, line, source, tokens)
        case "{":
            add_token(TokenType.LEFT_BRACE, start, current, line, source, tokens)
        case "}":
            add_token(TokenType.RIGHT_BRACE, start, current, line, source, tokens)
        case ",":
            add_token(TokenType.COMMA, start, current, line, source, tokens)
        case ".":
            add_token(TokenType.DOT, start, current, line, source, tokens)
        case "-":
            add_token(TokenType.MINUS, start, current, line, source, tokens)
        case "+":
            add_token(TokenType.PLUS, start, current, line, source, tokens)
        case ";":
            add_token(TokenType.SEMICOLON, start, current, line, source, tokens)
        case "*":
            add_token(TokenType.STAR, start, current, line, source, tokens)
        case "!":
            current = scan_multiple_characters(
                "=",
                TokenType.BANG,
                TokenType.BANG_EQUAL,
                start,
                current,
                line,
                source,
                tokens,
            )
        case "=":
            current = scan_multiple_characters(
                "=",
                TokenType.EQUAL,
                TokenType.EQUAL_EQUAL,
                start,
                current,
                line,
                source,
                tokens,
            )
        case "<":
            current = scan_multiple_characters(
                "=",
                TokenType.LESS,
                TokenType.LESS_EQUAL,
                start,
                current,
                line,
                source,
                tokens,
            )
        case ">":
            current = scan_multiple_characters(
                "=",
                TokenType.GREATER,
                TokenType.GREATER_EQUAL,
                start,
                current,
                line,
                source,
                tokens,
            )
        case "/":
            if match("/", current, source):
                current += 1  # consume the second /
                while (not is_at_end(current, len(source))) and (
                    source[current] != "\n"
                ):
                    current += 1
            else:
                add_token(TokenType.SLASH, start, current, line, source, tokens)
        case " " | "\r" | "\t":
            # Ignore whitespace.
            pass
        case "\n":
            line += 1
        case _:
            PyloxError.error(line, "Unexpected character.")

    return current


def add_token(
    token_type: TokenType,
    start: int,
    current: int,
    line: int,
    source: str,
    tokens: list[Token],
):
    text = source[start:current]
    tokens.append(Token(token_type=token_type, start=text, lexemme=None, line=line))


def scan_tokens(source: str) -> list[Token]:

    tokens: list[Token] = []
    start = 0
    current = 0
    line = 1

    while not is_at_end(current, len(source)):
        # We are at the beginning of the next lexeme.
        start = current
        current = scan_token(start, current, line, source, tokens)

    tokens.append(Token(TokenType.EOF, "", None, line))
    return tokens
