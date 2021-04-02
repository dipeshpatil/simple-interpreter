from Lexer.lexer import Lexer
from Parser.parser_ import Parser
from Interpreter.interpreter import Interpreter

while True:
    try:
        text = input("calc > ")

        if text == 'exit':
            break

        lexer = Lexer(text)
        tokens = lexer.generate_tokens()

        parser = Parser(tokens)
        tree = parser.parse()

        interpreter = Interpreter()
        value = interpreter.visit(tree)

        print(value)
    except Exception as e:
        print(e)
