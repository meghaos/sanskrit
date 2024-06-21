import re

tokens = [
    ('PRINT', r'प्रदर्शयति'),
    ('ADD', r'योजयति'),
    ('SUB', r'वियोजयति'),
    ('MUL', r'गुणयति'),
    ('DIV', r'विभजति'),
    ('ASSIGN', r'परिवर्तन'),
    ('IF', r'यदि'),
    ('ELSE', r'अन्यथा'),
    ('WHILE', r'यावत्'),
    ('BREAK', r'ब्रेक'),
    ('CONTINUE', r'कंटिन्यू'),
    ('FUNCTION', r'कार्य'),
    ('CALL', r'कॉल'),
    ('FLOAT', r'\d+\.\d+'),
    ('NUMBER', r'\d+'),
    ('ID', r'[a-zA-Z_अ-हऀ-ॿ_][a-zA-Z0-9_अ-हऀ-ॿ_]*'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COMMA', r','),
    ('EQ', r'=='),
    ('NE', r'!='),
    ('LE', r'<='),
    ('GE', r'>='),
    ('LT', r'<'),
    ('GT', r'>'),
    ('PLUS', r'\+'),
    ('MINUS', r'\-'),
    ('STRING', r'"[^"]*"'),
    ('WS', r'\s+'),
]

def lex(characters):
    pos = 0
    while pos < len(characters):
        match = None
        for token in tokens:
            pattern, regex = token
            regex = re.compile(regex)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if pattern != 'WS':  # Ignore whitespace
                    yield (pattern, text)
                pos = match.end(0)
                break
        if not match:
            raise RuntimeError(f'Unexpected character: {characters[pos]}')
            pos += 1

if __name__ == '__main__':
    code = 'कार्य(मेरा_कार्य) {\n    प्रदर्शयति("कार्य से नमस्ते")\n}\n\nकॉल(मेरा_कार्य)\n'
    for token in lex(code):
        print(token)
