"""Contains functions to convert infix expressions
to postfix, then evaluating them.

Project 2: Evaluating Expressions using Stacks
Author:
    Richard Hua
Class: CPE202
"""

from stacks import StackArray

# Create an empty stack called opstack for keeping operators. Create an empty list for output.
#
# Convert the input infix string to a list by using the string method split.
#
# Scan the token list from left to right.
#
# If the token is an operand, append it to the end of the output list.
#
# If the token is a left parenthesis, push it on the opstack.
#
# If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
#
# If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
#
# When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
def infix_to_postfix(infix_expr):
    """ Convert an infix expression into a postfix expression.
    Assumes valid inputs.

    Args:
        list (infix_expr): properly formatted/valid str for conversion

    Returns:
        str: a string of the converted postfix expression
    """
    # Append adds new item to list
    # Concat creates a new list every time instead

    opstack = StackArray()
    res = []
    lstr = infix_expr.split()
    # l_para = r_para = 0
    # operator precedence dict
    prec = { # higher val = higher prec
        "(" : 4,
        "^" : 3, # r-to-l (i.e. 2^3^2 = 2^(3^2) )
        "~" : 3, # right-to-left (i.e. -3^2 = -9)
        # '*/+-' are associated left to right
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1
    }
    for token in lstr:
        if token[0] in '0123456789':
            res.append(token)
            # not opstack.is_empty() guards against IndexError on empty peek
            if not opstack.is_empty() and opstack.peek() == '^':
                res.append(opstack.pop())
                if not opstack.is_empty() and opstack.peek() == '~':
                    res.append(opstack.pop())
        elif token == '(':
            # l_para += 1
            opstack.push(token)
        elif token == ')':
            # r_para += 1
            # opstack can't be empty for proper formatted input
            while opstack.peek() != '(':
                res.append(opstack.pop())
            opstack.pop() # remove left paran '('
        else: # token is ^ ~ * / + -: <-- operators
            while not opstack.is_empty() and prec[token] <= prec[opstack.peek()]:
                if opstack.peek() == '(':
                    break
                elif token == '^' and opstack.peek() == '~':
                    break
                else:
                    res.append(opstack.pop())
            opstack.push(token)
    # if l_para != r_para:
    #     raise SyntaxError
    while not opstack.is_empty():
        res.append(opstack.pop())
    res = " ".join(res)
    res.strip()
    return res

def postfix_eval(postfix_expr):
    """to evaluate a postfix expression into a value.
    Use the postfix_valid function described below to
    check the validity of the expression

    Args:
        list (postfix_expr): postfix expression for evaluation

    Returns:
        int: value of postfix_expr after evaluation

    Raises:
        ZeroDivisionError
    """
    s = StackArray()
    expr = postfix_expr.split()
    for token in expr:
        if token[0] in '0123456789':
            res = token
            s.push(res)
        else: # token is operator
            op2 = s.pop()
            op2 = float(op2)
            if s.is_empty(): # token is ~
                # could also be ~ for non-empty stack
                res = -1 * op2
            else:
                op1 = s.pop()
                op1 = float(op1)
                if token == '^':
                    res = op1 ** op2
                elif token == '~':
                    s.push(op1)
                    res = -1 * op2
                elif token == '*':
                    res = op1 * op2
                elif token == '/':
                    if op2 == 0:
                        raise ZeroDivisionError
                    else:
                        res = op1 / op2
                elif token == '+':
                    res = op1 + op2
                else: # token == '-'
                    res = op1 - op2
            s.push(res)
    return res

def postfix_valid(postfix_expr):
    """ To test for an invalid postfix expression.
    You may assume that what is passed in is a string
    that only contains numbers and operators. These are separated into
    valid tokens by spaces so you can use split and join as necessary.

    Note:
        No parantheses in postfix expression.

    Args:
        list (postfix_expr): list to check for postfix validity

    Returns:
        bool: True if valid, False otherwise
    """
    expr = postfix_expr.split()
    count = 0
    if postfix_expr == "":
        return False
    for token in expr:
        if token[0] in '0123456789':
            count += 1
        elif token == '~':
            pass
        else: # all other binary operators
            count -= 1
        if count < 0:
            return False
    if count == 1:
        return True
    return False
