from lexer import lex
from ast import Program, Print, Assign, BinOp, Number, Identifier, String, If, Comparison, While, Block

def parse(tokens):
    tokens = list(tokens)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def advance():
        nonlocal pos
        pos += 1

    def parse_block():
        statements = []
        assert peek()[0] == 'LBRACE'
        advance()
        while peek() and peek()[0] != 'RBRACE':
            statements.append(parse_statement())
        assert peek()[0] == 'RBRACE'
        advance()
        return Block(statements)

    def parse_expression():
        left = parse_term()
        token = peek()
        while token and token[0] in ('PLUS', 'MINUS'):
            op = token[0]
            advance()
            right = parse_term()
            left = BinOp(left, op, right)
            token = peek()
        return left

    def parse_term():
        left = parse_factor()
        token = peek()
        while token and token[0] in ('MUL', 'DIV'):
            op = token[0]
            advance()
            right = parse_factor()
            left = BinOp(left, op, right)
            token = peek()
        return left

    def parse_factor():
        token = peek()
        if token[0] == 'NUMBER':
            advance()
            return Number(int(token[1]))
        elif token[0] == 'ID':
            advance()
            return Identifier(token[1])
        elif token[0] == 'STRING':
            advance()
            return String(token[1][1:-1])  # Remove the surrounding quotes
        elif token[0] in ('ADD', 'SUB', 'MUL', 'DIV'):  # Handling nested expressions
            advance()
            assert peek()[0] == 'LPAREN'
            advance()
            left = parse_expression()
            assert peek()[0] == 'COMMA'
            advance()
            right = parse_expression()
            assert peek()[0] == 'RPAREN'
            advance()
            return BinOp(left, token[0], right)
        else:
            raise SyntaxError(f'Expected term, got {token}')

    def parse_comparison():
        left = parse_expression()
        token = peek()
        if token and token[0] in ('EQ', 'NE', 'LT', 'GT', 'LE', 'GE'):
            op = token[0]
            advance()
            right = parse_expression()
            return Comparison(left, op, right)
        else:
            return left

    def parse_statement():
        token = peek()
        if token[0] == 'PRINT':
            advance()
            if peek()[0] != 'LPAREN':
                raise SyntaxError('Expected LPAREN after PRINT')
            advance()
            expr = parse_expression()
            if peek()[0] != 'RPAREN':
                raise SyntaxError('Expected RPAREN after expression')
            advance()
            return Print(expr)
        elif token[0] == 'ASSIGN':
            advance()
            if peek()[0] != 'LPAREN':
                raise SyntaxError('Expected LPAREN after ASSIGN')
            advance()
            name = peek()
            if name[0] != 'ID':
                raise SyntaxError('Expected ID for assignment')
            advance()
            if peek()[0] != 'COMMA':
                raise SyntaxError('Expected COMMA after ID in assignment')
            advance()
            value = parse_expression()
            if peek()[0] != 'RPAREN':
                raise SyntaxError('Expected RPAREN after value in assignment')
            advance()
            return Assign(name[1], value)
        elif token[0] == 'IF':
            advance()
            if peek()[0] != 'LPAREN':
                raise SyntaxError('Expected LPAREN after IF')
            advance()
            condition = parse_comparison()
            if peek()[0] != 'RPAREN':
                raise SyntaxError('Expected RPAREN after condition')
            advance()
            true_branch = parse_statement()
            false_branch = None
            if peek() and peek()[0] == 'ELSE':
                advance()
                false_branch = parse_statement()
            return If(condition, true_branch, false_branch)
        elif token[0] == 'WHILE':
            advance()
            if peek()[0] != 'LPAREN':
                raise SyntaxError('Expected LPAREN after WHILE')
            advance()
            condition = parse_comparison()
            if peek()[0] != 'RPAREN':
                raise SyntaxError('Expected RPAREN after condition')
            advance()
            body = parse_statement()
            return While(condition, body)
        elif token[0] == 'LBRACE':
            return parse_block()
        else:
            raise SyntaxError(f'Expected statement, got {token}')

    statements = []
    while peek():
        statements.append(parse_statement())

    return Program(statements)

if __name__ == '__main__':
    with open('test.s', 'r', encoding='utf-8') as file:
        code = file.read()

    tokens = lex(code)
    for token in tokens:
        print(token)
    ast = parse(tokens)
    print(ast)
