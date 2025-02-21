import sys
from Parser import Parser
from Lexer import Lexer


def query_json(json_obj, query):
    keys = query.split('.')
    result = json_obj

    for key in keys:
        if key =='top':
            continue
        if '[' in key and ']' in key:
            key, index = key[:-1].split('[')
            result = result[key][int(index)]
        else:
            result = result[key]

    return result

if __name__ == "__main__":

    query = sys.argv[1]
    with open(sys.argv[2], "r") as file:
        json_text = file.read()

    lexer = Lexer(json_text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parsed_json = parser.parse()

    print(query_json(parsed_json, query))
