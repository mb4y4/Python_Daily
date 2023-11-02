#calculator

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator: ')

if operator == '+':
    print (number1 + number2)
elif operator == '-':
    print (number1 - number2)
elif operator == '*':
    print (number1 * number2)
elif operator == '/':
    print (number1 / number2)
elif operator == '%':
    print (number1 % number2)
elif operator == '**':
    print (number1 ** number2)
else :
    print('Operation not found')