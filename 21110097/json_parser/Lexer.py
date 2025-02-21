import sys
class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.length = len(text)

    def advance(self):
        if self.position < self.length:
            self.position += 1

    def peek(self):
        return self.text[self.position] if self.position < self.length else None


    def skip_whitespace(self):
        while self.peek() and self.peek().isspace():
            self.advance()

    def read_string(self):
        result = []
        self.advance()  # Skiping opening quote
        while self.peek() and self.peek() != '"':
            result.append(self.peek())
            self.advance()
        if self.peek() == '"':
            self.advance()  # Skip closing quote
        return ''.join(result)

    def read_number(self):
        result = []
        if self.peek() == '-':
            result.append('-')
            self.advance()
        while (self.peek() and self.peek().isdigit()) or self.peek() =='_':
            if self.peek() =='_' and self.text[self.position +1].isdigit() :
                self.advance()
            elif self.peek() =='_' :
                raise ValueError("unexpected number format")
            result.append(self.peek())
            self.advance()
        return int(''.join(result))
    
    
    def read_bool(self):
        result = []
        while self.peek() and len(result) < 4:
            result.append(self.peek())
            self.advance()
        result_str = ''.join(result)
        if result_str == 'true':
            return True
        elif result_str == 'fals' and self.text[self.position] == 'e':
            self.advance()
            return False
        elif result_str == 'null':
            return None
        else:
            raise ValueError("Unexpected value: " + result_str)


    def get_next_token(self):
        self.skip_whitespace()
        char = self.peek()

        if char is None:
            return ('EOF', None)
        elif char == '{':
            self.advance()
            return ('LBRACE', '{')
        elif char == '}':
            self.advance()
            return ('RBRACE', '}')
        elif char == '[':
            self.advance()
            return ('LBRACKET', '[')
        elif char == ']':
            self.advance()
            return ('RBRACKET', ']')
        elif char == ':':
            self.advance()
            return ('COLON', ':')
        elif char == ',':
            self.advance()
            return ('COMMA', ',')
        elif char == '"':
            return ('STRING', self.read_string())
        elif char.isdigit() or char == '-':
            return ('NUMBER', self.read_number())
        elif char == 't':
            return ('TRUE', self.read_bool())
        elif char == 'f':
            return ('FALSE', self.read_bool())
        elif char == 'n':
            return ('NULL', self.read_bool())
        elif self.peek() == '/' and self.text[self.position +1] == '/':
            while self.peek():
                if self.peek() == '\n':
                    self.advance()
                    break
                self.advance()
            return self.get_next_token()

        raise SyntaxError(f"Unexpected character '{char}' at position {self.position}")

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            if token[0] == 'EOF':
                break
            tokens.append(token)
        return tokens



if __name__ == "__main__":

    json_text = '{ "array": [10,]}'

    lexer = Lexer(json_text)
    tokens = lexer.tokenize()
    print(tokens)
