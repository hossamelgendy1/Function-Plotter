import matplotlib.pyplot as plt
import numpy as np

def validate_expression(s):
    numbers = '0123456789'
    operators = '+-*/^'
    opened_brackets = 0
    expect_operand = True

    for i,c in enumerate(s):
        if expect_operand and (c == 'x' or c in numbers):
            expect_operand = False
        elif not expect_operand and c == 'x': #var after another var or num without a seperating operator
            raise ValueError('ERROR: consecutive operands without a seperating operator!')
        elif not expect_operand and c in numbers and s[i-1] in numbers:
            continue
        elif not expect_operand and c in numbers and s[i-1] not in numbers: #space inside a number
            raise ValueError('ERROR: there is a space inside a number!')
        elif not expect_operand and c in operators:
            expect_operand = True
        elif expect_operand and c in operators: #first operand is missing or two consecutive operators
            raise ValueError('ERROR: there exists an operator without a first operand!')
        elif c == '(' and expect_operand:
            opened_brackets += 1
        elif (c == '(' and not expect_operand) or (c == ')' and expect_operand):
            raise ValueError('ERROR: brackets misplacing!')
        elif c == ')' and not expect_operand and opened_brackets > 0:
            opened_brackets -= 1
        elif c == ')' and not expect_operand and opened_brackets == 0:
            raise ValueError('ERROR: There is a closing bracket without an opening one!')
        elif c == ' ':
            continue
        else:
            raise ValueError('ERROR: Invalid symbol exists!')
    if expect_operand: #second operand is missing
        raise ValueError('ERROR: last operator without a second operand!')
    if opened_brackets > 0: #there is an opening bracket without a closing one
        raise ValueError('ERROR: There is an opening bracket without a closing one!')

    s = s.replace('^', '**')
    return s

def f(x, exp):
    return eval(exp)

def plot(min, max, exp, f):
    points = np.arange(min, max+0.1, 0.1) #to take the endpoint(max) inclusive
    plt.plot(points, f(points, exp))

    #setting the configrations of the window
    plt.title('Graph of $f(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.axhline(color = 'black')
    plt.axvline(color = 'black')
    plt.show()

try:
    min = float(input('Enter the minimum value of x: '))
    max = float(input('Enter the maximum value of x: '))
    if min > max:
        raise ValueError('ERROR: minimum value is greater than the maximum value!')
    exp = validate_expression(input('Enter the function: '))
    plot(min, max, exp, f)
except ValueError as e:
    print(e)
    exit()

