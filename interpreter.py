from parser import parse
from lexer import lex
from ast import Program, Print, Assign, BinOp, Number, Float, Identifier, String, If, Comparison, While, Block, Break, Continue, Array, ArrayAccess, FunctionDef, FunctionCall

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class FunctionContext:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f'Name "{name}" is not defined')

    def set(self, name, value):
        self.variables[name] = value

class Interpreter:
    def __init__(self):
        self.global_context = FunctionContext()
        self.functions = {}

    def eval(self, node, context=None):
        if context is None:
            context = self.global_context

        if isinstance(node, Program):
            for statement in node.statements:
                self.eval(statement, context)
        elif isinstance(node, Block):
            for statement in node.statements:
                self.eval(statement, context)
        elif isinstance(node, Print):
            value = self.eval(node.expression, context)
            print(value)
        elif isinstance(node, Assign):
            if isinstance(node.name, ArrayAccess):
                array = self.get_array(node.name, context)
                index = self.eval(node.name.index, context)
                value = self.eval(node.value, context)
                array[index] = value
            else:
                value = self.eval(node.value, context)
                context.set(node.name.name, value)
        elif isinstance(node, BinOp):
            left = self.eval(node.left, context)
            right = self.eval(node.right, context)
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
            return context.get(node.name)
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, If):
            condition = self.eval(node.condition, context)
            if condition:
                return self.eval(node.true_branch, context)
            elif node.false_branch:
                return self.eval(node.false_branch, context)
        elif isinstance(node, Comparison):
            left = self.eval(node.left, context)
            right = self.eval(node.right, context)
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
            while self.eval(node.condition, context):
                try:
                    self.eval(node.body, context)
                except ContinueException:
                    continue
                except BreakException:
                    break
        elif isinstance(node, Break):
            raise BreakException()
        elif isinstance(node, Continue):
            raise ContinueException()
        elif isinstance(node, Array):
            return [self.eval(element, context) for element in node.elements]
        elif isinstance(node, ArrayAccess):
            array = self.get_array(node, context)
            index = self.eval(node.index, context)
            return array[index]
        elif isinstance(node, FunctionDef):
            self.functions[node.name.name] = node.body
        elif isinstance(node, FunctionCall):
            if node.name.name not in self.functions:
                raise NameError(f'Function "{node.name.name}" is not defined')
            func_body = self.functions[node.name.name]
            new_context = FunctionContext(parent=context)
            self.eval(func_body, new_context)
        else:
            raise RuntimeError(f'Unexpected node: {node}')

    def get_array(self, node, context):
        if isinstance(node.array, ArrayAccess):
            array = self.get_array(node.array, context)
            index = self.eval(node.array.index, context)
            return array[index]
        else:
            return context.get(node.array.name)

if __name__ == '__main__':
    with open('test.s', 'r', encoding='utf-8') as file:
        code = file.read()

    tokens = lex(code)
    ast = parse(tokens)
    interpreter = Interpreter()
    interpreter.eval(ast)
