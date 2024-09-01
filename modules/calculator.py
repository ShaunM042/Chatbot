import operator

def safe_eval(expression):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ops and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            raise ValueError("Invalid expression")
    return stack[0] if len(stack) == 1 else "Error in expression"