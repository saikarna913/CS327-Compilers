# JSON Parser Assignment

## **Assignment Description**
Your task is to develop a JSON parser that supports the following data types:
- Strings
- Objects (dictionaries)
- Arrays
- Integers (including negative numbers, but no arithmetic operations are required)

You are expected to define the necessary tokens and Abstract Syntax Tree (AST). Implement a lexer and parser from scratch **without using built-in JSON libraries**. If you need clarification on JSON grammar, refer to official documentation or ask for guidance.


## **Submission Requirements**
- Submit a compressed file (`tar.gz` format) named **`a1234.tar.gz`**, where `1234` is your roll number.
- The archive must include:
  - **All necessary code files** for the parser.
  - A **`run.sh` script** to execute the program.
  - A **`collaborators.txt` file**, listing collaborators' names and roll numbers (one per line in the format: `Name, Roll Number`).
- Submission Deadline: **February 16, 11:59 PM**.

## **In-Lab Component**
On **February 17**, all students must attend a lab session where additional modifications will be required to enhance the program with new features.

## **Example Usage**
Given the following JSON object in `input.json`:

```json
{
  "user": {
    "id": 12345,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
      "street": "123 Main St",
      "city": "Somewhere",
      "state": "CA",
      "zip": "90210",
      "coordinates": {
        "latitude": 34,
        "longitude": -118
      }
    },
    "phoneNumbers": [
      {
        "type": "mobile",
        "number": "555-1234"
      },
      {
        "type": "home",
        "number": "555-5678"
      }
    ]
  }
}
```

Executing the following command:

```sh
./run.sh 'top.phoneNumbers[1].number' input.json
```

Should produce the output:

```sh
555-5678
```

