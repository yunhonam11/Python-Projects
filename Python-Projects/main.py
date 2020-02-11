import gcd

while True:
    command = input("Type in your command: ")
    if (command == "help"):
        print("Available programs: gcd2, gcdn")
    elif (command == "gcd2"):
        num1 = int(input("Type in your first integer: "))
        num2 = int(input("Type in your second integer: "))
        print(gcd.gcd2(num1, num2))
    elif (command == "gcdn"):
        inputArgs = input("Type in a list of positive integers separated by a comma: ")
        args = inputArgs.split(",")
        print(gcd.gcdn(args))
