import sys

def is_number(token):
    """Check if a token is a number."""
    try:
        float(token)
        return True
    except ValueError:
        return False

def forth_interpreter(program):
    stack = []
    tokens = program.split()
    
    for token in tokens:
        if is_number(token):
            stack.append(float(token) if '.' in token else int(token))
        elif token.startswith('"') and token.endswith('"'):
            stack.append(token[1:-1])  # Remove surrounding quotes
        elif token == '+':
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif token == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == '*':
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif token == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)
        elif token == '^':
            b, a = stack.pop(), stack.pop()
            stack.append(a ** b)
        elif token == 'get':
            stack.append(input())
        elif token == 'put':
            print(stack.pop())
        elif token == 'pop':
            stack.pop()
        elif token == 'dup':
            stack.append(stack[-1])
        elif token == 'rot':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif token == 'concat':
            b, a = stack.pop(), stack.pop()
            stack.append(str(a) + str(b))
        else:
            print(f"Unknown token: {token}")
            sys.exit(1)

# Example program
program = '"Enter first number: " put get "Enter second number: " put get "Their sum is: " put + put'
forth_interpreter(program)
