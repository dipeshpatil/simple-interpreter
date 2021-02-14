from Lexer.lexer import Lexer
from Parser.parser_ import Parser
from Interpreter.interpreter import Interpreter

while True:
    try:
        text = input("calc > ")

        lexer = Lexer(text)
        tokens = lexer.generate_tokens()

        lexer2 = Lexer(text)
        tokens2 = lexer2.generate_tokens()

        parser = Parser(tokens)
        tree = parser.parse()

        parser2 = Parser(tokens2)
        tree2 = parser2.parse()

        interpreter = Interpreter()
        value = interpreter.visit(tree)

        print(tree2)
        print(value)
    except Exception as e:
        print(e)
