def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []  # to keep operators
    output = [] # to build the output expression
    for char in expression:
        # If the character is an operand, add it to output
        if char.isalnum():
            output.append(char)
        
        # If the character is '(', push it to stack
        elif char == '(':
            stack.append(char)
        
        # If the character is ')', pop and output from the stack 
        # until an '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # pop '('
        
        # An operator is encountered
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)
    
    # pop all the operators from the stack
    while stack:
        output.append(stack.pop())
    return "".join(output)

# Example usage
expression = "A*(B+C)/D"
postfix = infix_to_postfix(expression)
print("Infix expression:", expression)
print("Postfix expression:", postfix)
