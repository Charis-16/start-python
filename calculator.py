running = True
while running:
    number1 = int(input("Input your first number"))
    operation = input("What operstion do you want")
    number2 = int(input("Input your second number"))
    match operation:
        case "+":
            total = number1 + number2
            print(total)
        case "-":
            total = number1 - number2
            print(total)
        case "/":
            total = number1 + number2
            print(total)
        case "*":
            total = number1 - number2
            print(total)
        case _:
            print("wrong operation")
    answer = input ("Do you have any more calculations?")
    if answer == "no":
        running=False
        print("Ok stopping now")
 