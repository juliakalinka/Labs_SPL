import math


def summ(x, y):
    return x + y


def substraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error. Division by 0 unreal"
    return x / y


def power(x, y):
    return pow(x, y)


def remains(x, y):
    return x % y


def square(x):
    if x < 0:
        return "The square root of a negative number is impossible"
    return math.sqrt(x)


memory = None
history = []
decimal_places = 2

configure_decimal = input("Adjust the number of decimal places? (Y/N): ")
if configure_decimal.lower() == 'y':
    try:
        decimal_places = int(input("Enter the number of decimal places: "))
    except ValueError:
        print("Error incorrect input!")

while True:
    result = ''
    print("Enter numbers:")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("Error incorrect input!")
        continue

    # Визначте функції для операцій
    operations = {
        '+': summ,
        '-': substraction,
        '*': multiplication,
        '/': division,
        '^': power,
        'sqrt': square,
        '%': remains
    }

    # Отримайте оператор від користувача
    operation = input("Enter operation (+, -, *, /, ^, sqrt, %): ")

    # Перевірте, чи оператор існує у словнику функцій
    if operation in operations:
        if operation == 'sqrt':
            result = operations[operation](num1)
        else:
            result = operations[operation](num1, num2)
    else:
        print("Error incorrect operator!")

    rounded_result = round(result, decimal_places)
    print(f"Result: {rounded_result:.{decimal_places}f}")

    calculation = f"{num1} {operation} {num2} = {result}"
    history.append(calculation)

    save = input("Save the result in memory? (Y/N): ")
    if save.lower() == 'y':
        memory = result

    retrieve = input("Delete the result from memory? (Y/N): ")
    if retrieve.lower() == 'y' and memory is not None:
        print("Value from memory:", memory)

    view_history = input("Show history? (Y/N): ")
    if view_history.lower() == 'y':
        print("History of calculations:")
        for entry in history:
            print(entry)

        continueCalc = input("Would you like to perform another calculation? (Y/N): ")
        if continueCalc.lower() != 'y':
            break
