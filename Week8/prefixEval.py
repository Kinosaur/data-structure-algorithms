# Function to check precedence of operators
def precedence(op):
    if op == "^":
        return 3
    if op == "*" or op == "/":
        return 2
    if op == "+" or op == "-":
        return 1
    return 0


# Function to perform infix to prefix conversion
def infix_to_prefix(expression):
    # Step 1: Reverse the infix expression
    expression = expression[::-1]

    # Step 2: Initialize empty stack and result list
    stack = []
    result = []

    # Step 3: Loop through each character of the reversed expression
    for char in expression:
        # If the character is an operand, add it to the result
        if char.isalnum():  # Check if the character is an operand
            result.append(char)
        # If the character is '(', process operators inside it
        elif char == ")":
            stack.append(char)
        # If the character is ')', reverse its role to '('
        elif char == "(":
            while stack and stack[-1] != ")":
                result.append(stack.pop())
            stack.pop()  # Remove ')' from stack
        # If the character is an operator
        else:
            while stack and precedence(char) < precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)

    # Step 4: Pop all the remaining operators from the stack
    while stack:
        result.append(stack.pop())

    # Step 5: Reverse the result to get the correct prefix expression
    return "".join(result[::-1])


# Example usage
infix_expression = "(A-B/C)*(A/K-L)"
prefix_expression = infix_to_prefix(infix_expression)
print("Infix Expression:", infix_expression)
print("Prefix Expression:", prefix_expression)
