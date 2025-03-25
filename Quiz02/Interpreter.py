import re
import sys

class ForthInterpreter:
    def __init__(self):
        self.stack = []
        self.operators = {
            '+': self.op_add,
            '-': self.op_sub,
            '*': self.op_mul,
            '/': self.op_div,
            '^': self.op_pow,
            'get': self.op_get,
            'put': self.op_put,
            'print': self.op_print,
            'pop': self.op_pop,
            'dup': self.op_dup,
            'rot': self.op_rot,
            'concat': self.op_concat,
        }
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def parse_input(self, input_str):
            tokens = []
            parts = []
            in_quote = False
            current_token = ""
            
            for char in input_str:
                if char == '"':
                    if in_quote:
                        current_token += char
                        parts.append(current_token)
                        current_token = ""
                        in_quote = False
                    else:
                        if current_token:
                            parts.append(current_token)
                            current_token = ""
                        current_token += char
                        in_quote = True
                elif char.isspace() and not in_quote:
                    if current_token:
                        parts.append(current_token)
                        current_token = ""
                else:
                    current_token += char
            
            if current_token:
                parts.append(current_token)
            for part in parts:
                if part.startswith('"'):
                    if not part.endswith('"'):
                        raise ValueError(f"Unclosed string literal: {part}")
                    try:
                        str_content = part[1:-1]
                        str_content = str_content.encode('utf-8').decode('unicode_escape')
                        tokens.append(('data', str_content))
                    except Exception as e:
                        raise ValueError(f"Invalid string literal: {part} - {e}")
                elif self.is_number(part):
                    if '.' in part:
                        tokens.append(('data', float(part)))
                    else:
                        tokens.append(('data', int(part)))
                else:
                    tokens.append(('op', part))
            
            return tokens

    def op_add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)
    
    def op_sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)
    
    def op_mul(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)
    
    def op_div(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a / b)
    
    def op_pow(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a ** b)
    
    def op_get(self):
        while True:
            user_input = input().strip()
            if not user_input:
                continue
            
            if user_input.startswith('"'):
                if not user_input.endswith('"'):
                    print("Error: String missing closing quote")
                    continue
                try:
                    str_content = user_input[1:-1]
                    str_content = str_content.encode('utf-8').decode('unicode_escape')
                    self.stack.append(str_content)
                    break
                except Exception as e:
                    print(f"Error: Invalid string - {e}")
                    continue
            else:
                try:
                    if '.' in user_input:
                        num = float(user_input)
                    else:
                        num = int(user_input)
                    self.stack.append(num)
                    break
                except ValueError:
                    print("Error: Input must be a number or quoted string")
                    continue
    
    def op_put(self):
        val = self.stack.pop()
        if isinstance(val, str):
            print(f'"{val}"')
        else:
            print(val)
    
    def op_print(self):
        val = self.stack.pop()
        print(val)
    
    def op_pop(self):
        self.stack.pop()
    
    def op_dup(self):
        val = self.stack[-1]
        self.stack.append(val)
    
    def op_rot(self):
        if len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a)
            self.stack.append(b)
    
    def op_concat(self):
        b = self.stack.pop()
        a = self.stack.pop()
        if isinstance(a, str) and isinstance(b, str):
            self.stack.append(a + b)
        else:
            raise ValueError("concat requires two strings")
    
    def evaluate(self, program):
        tokens = self.parse_input(program)
        for token_type, token_value in tokens:
            if token_type == 'data':
                self.stack.append(token_value)
            else:
                op = self.operators.get(token_value)
                if op is None:
                    raise ValueError(f"Unknown operator: {token_value}")
                op()
    
    def repl(self):
        print("Forth-like interpreter. Type 'bye' to exit.")
        while True:
            try:
                line = input("> ").strip()
                if line.lower() == 'bye':
                    break
                self.evaluate(line)
            except Exception as e:
                print(f"Error: {e}")
            print("Stack:", self.stack)

if __name__ == "__main__":
    interpreter = ForthInterpreter()
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            program = f.read()
        interpreter.evaluate(program)
    else:
        interpreter.repl()
