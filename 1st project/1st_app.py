calc = True

while calc:

    done = True
    q = input("Ready to calculate? (Y/N)")
    if q == "Y":
        done = False
    elif q == "N":
        quit()
    else:
        print("Invalid input.")

    while done == False:

        num1 = float(input("Enter 1st number:"))
        op = input("Enter operation:")
        num2 = float(input("Enter 2nd number:"))

        if op == "+":
            result = num1 + num2
            print("Your result is " + str(result))
            done = True
        elif op == "/":
            result = num1 / num2
            print("Your result is " + str(result))
            done = True
        elif op == "-":
            result = num1 - num2
            print("Your result is " + str(result))
            done= True
        elif op == "*":
            result = num1 * num2
            print("Your result is " + str(result))
            done = True
        else:
            print("Invalid operation/number!")