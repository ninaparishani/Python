"""Create a function called getNumbers() that asks the user for two numbers. 1 pt

Store the numbers in two variables, num1 and num2  2 pts
If both numbers are greater than 0 4 pts
Display "2 positive numbers"
elif both numbers are less than 0
Display "2 negative numbers"
elif num1 is positive, and num2 negative
Display "num1 is positive, num2 is negative"
elif num1 is negative and num2 positive
Display "num1 is negative, num2 is positive"

if num1 or num2 is positive		2 pts
Display "One number is positive"
elif num1 or num2 is negative
Display "One number is negative"

Finally, display addition(num1 + num2), subtraction (num1 - num2), multiplication (num1 x num2),
 division (num1 / num2)

IE "Addition Result: 45"	4 pts
   "Subtraction Result: -72"
   "Multiplcation Result: 483"
   "Division Result: 0.3333"

Include at least 3 comments 1 pt

Call the function 1pt

- Do not worry about validation of numbers vs text"""

def getNumbers():
    # Ask the user for two numbers
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # Check conditions
    if num1 > 0 and num2 > 0:
        print("2 positive numbers")
    elif num1 < 0 and num2 < 0:
        print("2 negative numbers")
    elif num1 > 0 and num2 < 0:
        print("num1 is positive, num2 is negative")
    elif num1 < 0 and num2 > 0:
        print("num1 is negative, num2 is positive")

    if num1 > 0 or num2 > 0:
        print("One number is positive")
    elif num1 < 0 or num2 < 0:
        print("One number is negative")

    # display calculation results
    print(f"Addition Result: {num1 + num2}")
    print(f"Subtraction Result: {num1 - num2}")
    print(f"Multiplication Result: {num1 * num2}")

    # Check if num2 is not 0 to avoid division by zero
    if num2 != 0:
        print(f"Division Result: {num1 / num2}")
    else:
        print("Cannot divide by zero.")

# Call the function
getNumbers()




