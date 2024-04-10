from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    s = Stack(30)

    # iterating through each part of the list
    for item in input_str.split():
        value = None
        try:
            value = int(item)
        except ValueError:
            try:
                value = float(item)
            except ValueError:
                pass

        if value is not None:
            s.push(value)
        elif item not in {"+", "-", "*", "/", "**", "<<", ">>"}:
            raise PostfixFormatException("Invalid token")
        else:
            try:
                op2 = s.pop()
                op1 = s.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")

            if item == "+":
                s.push(op1 + op2)
            elif item == "-":
                s.push(op1 - op2)
            elif item == "*":
                s.push(op1 * op2)
            elif item == "/":
                if op2 == 0:
                    raise ZeroDivisionError()
                s.push(op1 / op2)
            elif item == "**":
                s.push(op1 ** op2)
            elif item == ">>":
                try:
                    s.push(op1 >> op2)
                except TypeError:
                    raise PostfixFormatException("Illegal bit shift operand")
            elif item == "<<":
                try:
                    s.push(op1 << op2)
                except TypeError:
                    raise PostfixFormatException("Illegal bit shift operand")

    if s.size() > 1:
        raise PostfixFormatException("Too many operands")
    elif s.is_empty():
        raise PostfixFormatException("Empty input")

    return s.pop()

def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''

    stack = Stack(30)
    rpn = []

    # first number is precedence, false is from the left, true is from the right
    operators = {
        "<<": (4, False),
        ">>": (4, False),
        "**": (3, True),
        "*" : (2, False),
        "/" : (2, False),
        "+" : (1, False),
        "-" : (1, False),
    }

    # for each item in the split string, we go through to check for operands, operators, and parenthesis
    for item in input_str.split():
        if item == "(":
            stack.push("(") # push the first parenthesis onto stack
        elif item == ")":
            while not stack.is_empty(): # keep popping everything before the closing parenthesis
                x = stack.pop()
                if x == "(": # when we pop the first parenthesis, stop the while loop
                    break
                rpn.append(x) # appends the popped things into rpn
        elif item in operators:
            o1 = operators[item]
            while not stack.is_empty():
                x = stack.peek()
                if x not in operators:
                    break
                o2 = operators[x] # compare o1 and o2 precedence and orientation
                if not ((not o1[1]) and (o1[0] <= o2[0])) or ((o1[1]) and (o1[0] < o2[0])):
                    break

                rpn.append(stack.pop())

            stack.push(item)
        else:
            rpn.append(item) # not operator or parenthesis, append the number

    # if it is a number, because what we looked through earlier
    while not stack.is_empty():
        x = stack.pop()
        if x in operators:
            rpn.append(x)

    return " ".join(rpn)

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''

    stack = Stack(30)

    # algorithm is always string = op1 + op2 + operator until there is only 1 left
    # until it reaches an operator, you continue with the algorithm
    for item in reversed(input_str.split()):
        if item not in {"+", "-", "*", "/", "**", "<<", ">>"}:
            stack.push(item)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.push("{} {} {}".format(op1, op2, item))

    return stack.pop()



