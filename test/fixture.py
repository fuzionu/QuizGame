import sys
from io import StringIO
from typing import Union

from main import main


def run(input: Union[str, list]) -> str:
    if type(input) == list:
        return execute("\n".join(input))
    return execute(input)


def execute(input: str) -> str:
    _sys_stdout = sys.stdout
    _sys_stdin = sys.stdin
    sys.stdout = LinesStringIO()
    sys.stdin = StringIO(input)
    try:
        try:
            main()
        except SystemExit:
            pass
        return str(sys.stdout)
    except EOFError:
        raise Exception("Insufficient user input at: " + str(sys.stdout)) from None
    finally:
        sys.stdout = _sys_stdout
        sys.stdin = _sys_stdin


class LinesStringIO(StringIO):
    def __init__(self):
        super().__init__()
        self._lines = []

    def write(self, s: str) -> int:
        self._lines.append(s)
        return super().write(s)

    def __str__(self) -> str:
        return ''.join(self._lines)


def answers(first: str, second: str, third: str, fourth: str) -> str:
    amount = [first, second, third, fourth].count("Correct")
    return f"""Welcome to my computer quiz!
Do you want to play? Okay! Let's play :)
What does CPU stand for? {first}!
What does GPU stand for? {second}!
What does RAM stand for? {third}!
What does PSU stand for? {fourth}!
You got {amount} questions correct
You got {amount * 25.0}% correct
"""
