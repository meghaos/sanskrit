from parser import parse
from lexer import lex
from ast import Program, Print, Assign, BinOp, Number, Float, Identifier, String, If, Comparison, While, Block, Break, Continue, Array, ArrayAccess

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

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
            if isinstance(node.name, ArrayAccess):
                array = self.get_array(node.name)
                index = self.eval(node.name.index)
                value = self.eval(node.value)
                array[index] = value
            else:
                value = self.eval(node.value)
                self.environment[node.name.name] = value
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
        elif isinstance(node, Float):
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
                try:
                    self.eval(node.body)
                except ContinueException:
                    continue
                except BreakException:
                    break
        elif isinstance(node, Break):
            raise BreakException()
        elif isinstance(node, Continue):
            raise ContinueException()
        elif isinstance(node, Array):
            return [self.eval(element) for element in node.elements]
        elif isinstance(node, ArrayAccess):
            array = self.get_array(node)
            index = self.eval(node.index)
            return array[index]
        else:
            raise RuntimeError(f'Unexpected node: {node}')

    def get_array(self, node):
        if isinstance(node.array, ArrayAccess):
            array = self.get_array(node.array)
            index = self.eval(node.array.index)
            return array[index]
        else:
            return self.environment[node.array.name]

if __name__ == '__main__':
    with open('test.s', 'r', encoding='utf-8') as file:
        code = file.read()

    tokens = lex(code)
    ast = parse(tokens)
    interpreter = Interpreter()
    interpreter.eval(ast)
