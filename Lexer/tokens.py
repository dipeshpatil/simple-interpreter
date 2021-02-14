from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    INT_DIVIDE = 5
    MOD = 6
    POW = 7
    SQRT = 8
    LOGNBASEX = 9
    LPAREN = 10
    RPAREN = 11


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
