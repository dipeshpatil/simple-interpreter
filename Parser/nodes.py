from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"


@dataclass
class IntDivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} // {self.node_b})"


@dataclass
class ModNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} % {self.node_b})"


@dataclass
class PowNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} ** {self.node_b})"


@dataclass
class NRTNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} # {self.node_b})"


@dataclass
class LogNBaseXNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} LB {self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"


@dataclass
class NatLogNode:
    node: any

    def __repr__(self):
        return f"(LN{self.node})"


@dataclass
class CosNode:
    node: any

    def __repr__(self):
        return f"(C{self.node})"


@dataclass
class CosInvNode:
    node: any

    def __repr__(self):
        return f"(CI{self.node})"
