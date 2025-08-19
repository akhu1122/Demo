number1 = float(input(" enter First number: "))
number2 = float(input(" enter Second number: "))
op = input("Operator (+ - * /): ")

if op == '+':
    print(number1 + number2)
elif op == '-':
    print(number1 - number2)
elif op == '*':
    print(number1 * number2)
elif op == '/':
     print(number1 / number2)
else:
    print("Error")
