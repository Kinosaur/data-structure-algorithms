class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None


# Helper function to check precedence of operators
def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0


# Helper function to check if the character is an operator
def is_operator(c):
    return c == "+" or c == "-" or c == "*" or c == "/"


# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    stack = Stack()
    result = []

    for char in expression:
        print(f"Processing '{char}':")

        # If character is an operand, add it to result
        if char.isalnum():
            result.append(char)
            print(f"Operand '{char}' added to result: {''.join(result)}")

        # If character is '(', push it to the stack
        elif char == "(":
            stack.push(char)
            print(f"Push '(' to stack: {stack.stack}")

        # If character is ')', pop and append until '(' is found
        elif char == ")":
            while stack.peek() != "(":
                result.append(stack.pop())
                print(f"Pop from stack and append to result: {''.join(result)}")
            stack.pop()  # Remove '(' from the stack
            print(f"Pop '(' from stack: {stack.stack}")

        # If character is an operator, pop operators from the stack with higher or equal precedence
        elif is_operator(char):
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                result.append(stack.pop())
                print(
                    f"Pop from stack and append to result due to precedence: {''.join(result)}"
                )
            stack.push(char)
            print(f"Push operator '{char}' to stack: {stack.stack}")

        print(f"Current stack: {stack.stack}")
        print(f"Current result: {''.join(result)}")
        print("----")

    # Pop remaining operators from the stack
    while not stack.is_empty():
        result.append(stack.pop())
        print(f"Pop from stack and append to result: {''.join(result)}")

    return "".join(result)


# Example Usage
expression = "A+B*(C-D)"
postfix_expression = infix_to_postfix(expression)
print("\nFinal Postfix Expression: ", postfix_expression)
