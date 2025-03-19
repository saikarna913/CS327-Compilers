
# COMPILERS QUIZ 2

## Designing a Forth-like Language

This language includes the following elements:
- **Numbers (with decimal point):** Examples include `42` and `42.5`.
- **Strings:** Example: `"Hello, World!"`
- **Words:** Everything else without spaces, such as `get`, `put`, `+`. The following are not words: `2a`, `"aa`.

### Program Structure
A program is a sequence of elements separated by whitespace. The language uses a postfix syntax and a stack for evaluation.

### Example Programs

1. **Print `5` to screen:**
   ```forth
   2 3 + put
   ```
   - Numbers or strings are pushed to the stack.
   - Words correspond to operations, which take arguments by popping the stack and push results back onto it.

2. **Read two numbers and print their sum:**
   ```forth
   get get + put
   ```

3. **For k-ary operators:**
   - The top element is the last argument.
   - The element below the top is the second-last argument, and so on.

   Example:
   ```forth
   10 2 / put
   ```
   Prints `5`.

### Stack Representation
- A stack `S` is denoted as `x y ...`, where `x` is the top element.
- `x S` indicates a stack with `x` as the top element and arbitrary elements `S` underneath it.

---

## Implementing an Interpreter

### Words to Implement
1. **Arithmetic:**
   - `+`, `-`, `*`, `/`, `^`
2. **Stack Operations:**
   - `get`: Reads a value (number or string) from keyboard input and pushes it to the stack.
   - `put`: Prints the top value (followed by a newline) to the screen.
   - `pop`: Removes the top element from the stack.
   - `dup`: Turns the stack from `x S` to `x x S`.
   - `rot`: Turns the stack from `x y S` to `y x S`.
   - `concat`: Concatenates two strings.

---

### Example: Query Two Numbers and Output Their Sum
```forth
"Enter first number: " put get
"Enter second number: " put get
"Their sum is: " put + put
```
