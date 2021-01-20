import math


class Stack:
    def __init__(self):
        self.item = []
        self.top = -1

    def pop(self):
        self.top -= 1
        if len(self.item) >= 1:
            element = self.item.pop()
            return element
        else:
            print("List is Empty")

    def push(self, item):
        self.top += 1
        self.item.append(item)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False

    def Head(self):
        if self.top != -1:
            return self.item[self.top]
        else:
            return None


OPriority = {'(': 4, '-': 3, '+': 3, '%': 2, '/': 2, '*': 2, '^': 1}

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Operatorcheck = ['+', '-', '/', '*', '%', '^', '.']
parantesproblem = ['/', '*', '%', '^', '.']
Othercheck = ["s", "c", "t", "k", 'r']
Error = "Invalid Input!!!"
all = numbers + Operatorcheck + Othercheck + ['(', ')']
starterror = ['+', '/', '*', '%', '^', '.']
endingerrors = Operatorcheck + Othercheck + ['(']


def isOk(input):
    if input[0] in starterror or input[-1] in endingerrors:
        print(Error, ': Operator Problem...')
        return False
    for flag in range(0, len(input)):
        if input[flag] not in all:
            print(Error)
            return False
        if input[flag] in Operatorcheck:
            if input[flag + 1] in Operatorcheck:
                if input[flag] in ['*', '/']:
                    if input[flag + 1] != '-':
                        print(Error)
                        return False
                else:
                    print(Error)
                    return False
        if input[flag] in Othercheck:
            if input[flag] == 'r':
                if input[flag + 1] == '-':
                    print(Error, 'Error: The square root of negative numbers is undefined.')
                    return False
            if input[flag + 1] in Operatorcheck and input[flag + 1] in Othercheck:
                if input[flag + 1] != '-':
                    print(Error)
                    return False
        if input[flag] == '(':
            if input[flag + 1] in parantesproblem:
                print(Error)
                return False
    return True


def degtoradian(number):
    y = number / 180
    z = math.pi
    r = z * y
    return r


def calculatefns(sign, number):
    num = float(number)
    rad = degtoradian(num)

    if sign == 's':
        return math.sin(rad)

    if sign == 'c':
        return math.cos(rad)

    if sign == 't':
        if num % 90 == 0 and num % 180 != 0:
            print("Tan is undefined! The answer will be wrong!")
        tan = math.tan(rad)
        return tan

    if sign == 'k':
        if num % 180 == 0:
            print("cot is undefined! The answer will be wrong!")
        cot = 1 / (math.tan(rad))
        return cot

    if sign == 'r':
        return math.sqrt(num)


def calculation(a, item, b):
    if item == "+":
        return a + b

    if item == "-":
        return a - b

    if item == "*":
        return a * b

    if item == "/":
        if b == 0:
            print('ZeroDivisionError!!')
            return None
        return a / b

    if item == "%":
        if b == 0:
            print('ZeroDivisionError!!')
            return None
        return a % b

    if item == "^":
        return a ** b


def Main(Input):
    Equation = str(Input)
    Operators = ['+', '-', '/', '*', '%', '(', '^', ')']
    OtherOps = ["s", "c", "t", "k", 'r']

    Operator = Stack()
    Operand = Stack()

    number = ""
    sign = ''
    for flag in range(0, len(Equation)):
        if Equation[flag] not in Operators and Equation[flag] not in OtherOps:
            number = number + Equation[flag]
            if flag == len(Equation) - 1:
                if sign != '':
                    number = calculatefns(sign, number)
                    sign = ''
                Operand.push(float(number))
                number = ""
        else:
            if number != "":
                if sign != '':
                    number = calculatefns(sign, number)
                    sign = ''
                Operand.push(float(number))
                number = ""
        if Equation[flag] in Operators:
            if Equation[flag] == '-':
                if Equation[flag - 1] in ["*", "/", "("] or flag == 0:
                    if Equation[flag + 1] == '(':
                        Operand.push(0)
                        Operator.push(Equation[flag])
                    else:
                        number = '-'
                else:
                    Operator.push(Equation[flag])

            else:
                if Operator.isEmpty():
                    Operator.push(Equation[flag])
                else:

                    if Equation[flag] == ')':
                        while Operator.Head() != "(":
                            b = Operand.pop()
                            a = Operand.pop()
                            Operand.push(calculation(a, Operator.pop(), b))
                        if Operator.Head() == "(":
                            Operator.pop()
                    else:
                        if Equation[flag] != '(':
                            if OPriority[Equation[flag]] >= OPriority[Operator.Head()]:
                                b = Operand.pop()
                                a = Operand.pop()
                                Operand.push(calculation(a, Operator.pop(), b))
                        Operator.push(Equation[flag])

        if Equation[flag] in OtherOps:
            sign = Equation[flag]

    while not Operator.isEmpty():
        if Operator.Head() == "(":
            Operator.pop()
        b = Operand.pop()
        a = Operand.pop()
        Operand.push(calculation(a, Operator.pop(), b))
    final = Operand.pop()
    return final


def guide():
    print("Signs Guide:")
    print("sin -> s")
    print("cos -> c")
    print("tan -> t")
    print("cot -> k")
    print("Power -> ^")
    print("SquareRoot -> r")
    print("Multiplication -> *")
    print("Division -> /")
    print("Summation -> +")
    print("Submission -> -")
    print("Remainder -> %\n")
    print('Enter q for Quit')


print("\nEngineering Calculator\n")
Status = True
guide()
while Status:
    Input = input("\nEnter your calculations string: ")
    if Input == 'q':
        break
    while not isOk(Input):
        Input = input("Enter another calculations string: ")
    print("The Result = ", Main(Input))
