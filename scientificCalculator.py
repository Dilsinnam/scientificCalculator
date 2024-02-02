import math

averageCalculations = []
calculationCount = 0
averageCalculationSum = 0.0

print("Current Result: 0.0\n")
print("Calculator Menu\n")
print("---------------\n")
print("0. Exit Program \n")
print("1. Addition \n")
print("2. Subtraction \n")
print("3. Multiplication \n")
print("4. Division \n")
print("5. Exponentiation \n")
print("6. Logarithm \n")
print("7. Display Average\n")

while True:
    menuChoice = int(input("Enter Menu Selection: "))
    if menuChoice == 0:
        break
    elif menuChoice == 1:
        print()
        addOne = float(input("Enter first operand: "))
        print()
        addTwo = float(input("Enter second operand: "))
        print()
        final = addOne + addTwo
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 2:
        print()
        subOne = float(input("Enter first operand: "))
        print()
        subTwo = float(input("Enter second operand: "))
        print()
        final = subOne - subTwo
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 3:
        print()
        multOne = float(input("Enter first operand: "))
        print()
        multTwo = float(input("Enter second operand: "))
        final = multOne * multTwo
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 4:
        print()
        divOne = float(input("Enter first operand: "))
        print()
        divTwo = float(input("Enter second operand: "))
        print()
        final = divOne / divTwo
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 5:
        print()
        expOne = float(input("Enter first operand: "))
        print()
        expTwo = float(input("Enter second operand: "))
        print()
        final = math.pow(expOne, expTwo)
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 6:
        print()
        logOne = float(input("Enter first operand: "))
        print()
        logTwo = float(input("Enter second operand: "))
        print()
        final = math.log(logTwo, logOne)
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}\n")
    elif menuChoice == 7:
        if calculationCount == 0:
            print("No calculations yet to average! \n")
        else:
            averageOfSums = averageCalculationSum / calculationCount
            print(f"Sum of calculations: {round(averageCalculationSum,2)}\n")
            print(f"Number of calculations: {round(calculationCount,2)}\n")
            print(f"Average of calculations: {round(averageOfSums,2)}\n")
    else:
        print("Invalid selection!\n")

    print("Calculator Menu\n")
    print("---------------\n")
    print("0. Exit Program \n")
    print("1. Addition \n")
    print("2. Subtraction \n")
    print("3. Multiplication \n")
    print("4. Division \n")
    print("5. Exponentiation \n")
    print("6. Logarithm \n")
    print("7. Display Average\n")

print("Thanks for using this calculator. Goodbye!")
