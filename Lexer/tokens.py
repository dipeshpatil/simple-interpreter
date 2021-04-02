from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4

    LPAREN = 5
    RPAREN = 6

    MOD = 7
    INT_DIVIDE = 8
    POW = 9
    NRT = 10
    LOGNBASEX = 11
    NAT_LOG = 12

    COS = 13
    COS_INV = 14


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
