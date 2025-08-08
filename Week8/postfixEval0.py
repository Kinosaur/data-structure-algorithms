def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


stack = []

postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        stack.append(float(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(a / b)
        elif token == "%":
            stack.append(a % b)
        elif token == "^":
            stack.append(a**b)

print("%.1f" % stack[0])


# def evaluate_postfix(expression):
#     stack = []
#     operators = {"+", "-", "*", "/", "%", "^"}

#     tokens = expression.split()

#     for token in tokens:
#         if is_number(token):
#             stack.append(float(token))
#         else:
#             b = stack.pop()
#             a = stack.pop()

#             if token == "+":
#                 stack.append(a + b)
#             elif token == "-":
#                 stack.append(a - b)
#             elif token == "*":
#                 stack.append(a * b)
#             elif token == "/":
#                 stack.append(a / b)
#             elif token == "%":
#                 stack.append(a % b)
#             elif token == "^":
#                 stack.append(a**b)

#     print(f"{stack[0]:.1f}")


# expression = sys.stdin.read().strip()
# evaluate_postfix(expression)
