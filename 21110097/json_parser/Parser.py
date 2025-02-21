class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def consume(self, expected_type):
        token_type, token_value = self.tokens[self.index]
        if token_type == expected_type:
            self.index += 1
            return token_value
        raise SyntaxError(f"Expected {expected_type} but got {token_type}")

    def parse_value(self):
        token_type, token_value = self.tokens[self.index]

        if token_type == 'STRING':
            self.index += 1
            return token_value
        elif token_type == 'NUMBER':
            self.index += 1
            return token_value
        elif token_type == 'LBRACE':
            return self.parse_object()
        elif token_type == 'LBRACKET':
            return self.parse_array()
        elif token_type == 'TRUE':
            self.index += 1
            return True
        elif token_type == 'FALSE':
            self.index += 1
            return False
        elif token_type == 'NULL':
            self.index += 1
            return None
        else:
            raise SyntaxError(f"Unexpected token {token_type}")

    def parse_object(self):
        obj = {}
        self.consume('LBRACE')
        if self.tokens[self.index][0] == 'RBRACE':
            self.consume('RBRACE')
            return obj

        while True:
            key = self.consume('STRING')
            self.consume('COLON')
            obj[key] = self.parse_value()

            if self.tokens[self.index][0] == 'RBRACE':
                break
            self.consume('COMMA')

        self.consume('RBRACE')
        return obj

    def parse_array(self):
        array = []
        self.consume('LBRACKET')
        if self.tokens[self.index][0] == 'RBRACKET':
            self.consume('RBRACKET')
            return array

        while True:
            if  self.tokens[self.index][0] == 'RBRACKET':
                break
            array.append(self.parse_value())
            self.consume('COMMA')

        self.consume('RBRACKET')
        return array

    def parse(self):
        return self.parse_value()
if __name__ == "__main__":
    tokens =[('LBRACE', '{'), ('STRING', 'array'), ('COLON', ':'), ('LBRACKET', '['), ('COMMA', ','), ('RBRACKET', ']'), ('RBRACE', '}')]
    parser = Parser(tokens)
    parsed_json = parser.parse()