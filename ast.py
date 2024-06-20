class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f'Program(statements={self.statements})'

class Print(Node):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f'Print(expression={self.expression})'

class Assign(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'Assign(name={self.name}, value={self.value})'

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'BinOp(left={self.left}, op={self.op}, right={self.right})'

class Number(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Number(value={self.value})'

class Float(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Float(value={self.value})'

class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Identifier(name={self.name})'

class String(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'String(value={self.value})'

class If(Node):
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def __repr__(self):
        return f'If(condition={self.condition}, true_branch={self.true_branch}, false_branch={self.false_branch})'

class Comparison(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'Comparison(left={self.left}, op={self.op}, right={self.right})'

class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f'While(condition={self.condition}, body={self.body})'

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f'Block(statements={self.statements})'

class Break(Node):
    def __repr__(self):
        return 'Break()'

class Continue(Node):
    def __repr__(self):
        return 'Continue()'

class Array(Node):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f'Array(elements={self.elements})'

class ArrayAccess(Node):
    def __init__(self, array, index):
        self.array = array
        self.index = index

    def __repr__(self):
        return f'ArrayAccess(array={self.array}, index={self.index})'
