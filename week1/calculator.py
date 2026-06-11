from decimal import Decimal

print("Operator guide:\n 1 = + \n 2 = - \n 3 = * \n 4 = / \n 5 = power \n 6 = radical")

while True:
    operator = (input("Enter operator (1-6)"))

    numA = Decimal(input("First number "))
    numB = Decimal(input("Second number "))

    if operator == "1":
        print(numA + numB)

    elif operator == "2":
        print(numA - numB)

    elif operator == "3":
        print(numA*numB)

    elif operator == "4":
        if numB == 0:
            print("Unable to compute! (Divide by zero error!)")
        else:
            print(numA/numB)

    elif operator == "5":
        print(numA**numB)

    elif operator == "6":
        print(numA**(1/numB))
        
    else:
        print("Unable to compute! (Operator not recognized!)")
