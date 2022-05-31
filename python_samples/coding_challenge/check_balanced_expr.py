'''Verify if string is having balanced open and closed brackets'''

def balanced_expr(expr):
    '''Function to verify if string is balanced'''
    stack = []
    for char in expr:
        if char in ('{', '[', '('):
            stack.append(char)
        elif char not in ('}', ']', ')'):
            continue
        else:
            if not stack:
                return False

            cur_char = stack.pop()
            if cur_char == '{' and char != '}':
                return False
            if cur_char == '[' and char != ']':
                return False
            if cur_char == '(' and char != ')':
                return False
    if stack:
        return False
    return True

str1 = '{}{[]}'
str2 = '{Suraj}{[Jaiswal]}'
str3 = '{Suraj[}]{Jaiswal}'
str4 = '{[{]}}'

print(balanced_expr(str1))
print(balanced_expr(str2))
print(balanced_expr(str3))
print(balanced_expr(str4))
