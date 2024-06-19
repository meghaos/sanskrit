from parser import parse
from lexer import lex
from ast import Program, Print, Assign, BinOp, Number, Identifier, String, If, Comparison, While, Block

class Interpreter:
    def __init__(self):
        self.environment = {}

    def eval(self, node):
        if isinstance(node, Program):
            for statement in node.statements:
                self.eval(statement)
        elif isinstance(node, Block):
            for statement in node.statements:
                self.eval(statement)
        elif isinstance(node, Print):
            value = self.eval(node.expression)
            print(value)
        elif isinstance(node, Assign):
            value = self.eval(node.value)
            self.environment[node.name] = value
        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == 'ADD':
                return left + right
            elif node.op == 'SUB':
                return left - right
            elif node.op == 'MUL':
                return left * right
            elif node.op == 'DIV':
                return left / right
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, Identifier):
            return self.environment[node.name]
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, If):
            condition = self.eval(node.condition)
            if condition:
                return self.eval(node.true_branch)
            elif node.false_branch:
                return self.eval(node.false_branch)
        elif isinstance(node, Comparison):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == 'EQ':
                return left == right
            elif node.op == 'NE':
                return left != right
            elif node.op == 'LT':
                return left < right
            elif node.op == 'GT':
                return left > right
            elif node.op == 'LE':
                return left <= right
            elif node.op == 'GE':
                return left >= right
        elif isinstance(node, While):
            while self.eval(node.condition):
                self.eval(node.body)
        else:
            raise RuntimeError(f'Unexpected node: {node}')

if __name__ == '__main__':
    with open('test.s', 'r', encoding='utf-8') as file:
        code = file.read()

    tokens = lex(code)
    ast = parse(tokens)
    interpreter = Interpreter()
    interpreter.eval(ast)
