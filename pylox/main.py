from pathlib import Path
from typing import Literal
import sys


def run(source_code: str):
    print("running your code...")
    pass


def read_file(file: Path, mode: Literal["r", "rb"]):
    with open(file, mode) as f:
        data = f.read()

    return data


def run_file(file: Path):
    source_bytes: bytes = read_file(file, mode="rb")
    source_code = source_bytes.decode("utf-8")
    run(source_code)


def run_prompt():
    print("Hi!\npylox is an interpreter for the Lox programming language.")

    while True:
        try:
            line = input("> ")
        except EOFError:
            print("bye :)")
            break

        if not line:
            break

        run(line)


if __name__ == "__main__":
    args = sys.argv

    match args:
        case args if len(args) > 2:
            print("Usage: pylox [script]")
            sys.exit(64)
        case args if len(args) == 2:
            run_file(args[1])
        case _:
            run_prompt()
