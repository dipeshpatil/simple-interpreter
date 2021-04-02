from Interpreter.values import Number
from Interpreter.calculator import *


class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    @staticmethod
    def visit_NumberNode(node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime Math Error")

    def visit_IntDivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value // self.visit(node.node_b).value)
        except:
            raise Exception("Runtime Math Error")

    def visit_ModNode(self, node):
        return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)

    def visit_PowNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_NRTNode(self, node):
        return Number(self.visit(node.node_a).value ** (1 / self.visit(node.node_b).value))

    def visit_LogNBaseXNode(self, node):
        return Number(logBaseX(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_NatLogNode(self, node):
        return Number(naturalLog(self.visit(node.node).value))

    def visit_CosNode(self, node):
        return Number(cosine(self.visit(node.node).value))

    def visit_CosInvNode(self, node):
        return Number(cosineInv(self.visit(node.node).value))
