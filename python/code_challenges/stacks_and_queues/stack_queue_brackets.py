from stack import Stack


def multi_bracket_validation(string):

    s = Stack()
    type = {"(": ")", "{": "}", "[": "]"}

    for char in string:
        if char in type.keys():
            s.push(char)
        elif char in type.values() and (not s.top or type[s.pop()] != char):
            return False
    return True
