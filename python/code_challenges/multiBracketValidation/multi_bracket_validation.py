def multi_bracket_validation(input):
    brac_check = []
    for char in input:
        if char == "{" or char == "(" or char == "[":
            brac_check.append(char)
        elif char == "}" or char == ")" or char == "]":
            if len(brac_check) == 0:
                return False
            top = brac_check.pop()
            if not compare(top,char):
                return False
    if len(brac_check) != 0:
        return False
    return True


def compare(open, close):
    if open == '(' and close == ')':
        return True
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    return False
