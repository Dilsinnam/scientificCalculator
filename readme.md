# Scientific Calculator

A seven-function Scientific Calculator made from Python. Operations include addition, subtraction, multiplication, division, exponents, logarithms, and the average of all calculations. 


## Breakdown
I used arrays, as well as a "while True" statement to make the general calculator.

```python
while True: # the while True statement to start it off
    menuChoice = int(input("Enter Menu Selection: "))
    if menuChoice == 0:
        break
    elif menuChoice == 1:
        print()
        addOne = float(input("Enter first operand: "))
        addTwo = float(input("Enter second operand: "))
        final = addOne + addTwo
        averageCalculations.append(final)
        calculationCount += 1
        averageCalculationSum += final
        print(f"Current Result: {final}")
        #This continues for selections 1 - 6
```
On selection seven, I used the array to call the total of the stored calculations, then averaged and numbered them.
```python
#the array: 
averageCalculations = []
calculationCount = 0
averageCalculationSum = 0.0

#the code for selectin 7:
elif menuChoice == 7:
        if calculationCount == 0:
            print("Error: No calculations yet to average! \n")
        else:
            averageOfSums = averageCalculationSum / calculationCount
            print(f"Sum of calculations: {round(averageCalculationSum,2)}")
            print(f"Number of calculations: {round(calculationCount,2)}")
            print(f"Average of calculations: {round(averageOfSums,2)}\n")
        continue
```
## Sample Output

```python
Current Result: 0.0

Calculator Menu

---------------

0. Exit Program

1. Addition

2. Subtraction

3. Multiplication

4. Division

5. Exponentiation

6. Logarithm

7. Display Average

Enter Menu Selection: 6

Enter first operand: 2

Enter second operand: 4

Current Result: 2.0

Calculator Menu

---------------

0. Exit Program

1. Addition

2. Subtraction

3. Multiplication

4. Division

5. Exponentiation

6. Logarithm

7. Display Average

Enter Menu Selection: 3

Enter first operand: 2

Enter second operand: 6
Current Result: 12.0

Calculator Menu

---------------

0. Exit Program

1. Addition

2. Subtraction

3. Multiplication

4. Division

5. Exponentiation

6. Logarithm

7. Display Average

Enter Menu Selection: 7
Sum of calculations: 14.0

Number of calculations: 2

Average of calculations: 7.0

Calculator Menu

---------------

0. Exit Program

1. Addition

2. Subtraction

3. Multiplication

4. Division

5. Exponentiation

6. Logarithm

7. Display Average

Enter Menu Selection: 0
Thanks for using this calculator. Goodbye!
```