"""Put a loop around the existing loop in basicmoduleimport.py,
 that asks the user if they want to format a price. Give them Y or N options.
  If they do not put in a correct answer, ask them again and keep asking until one is given.
   Tally up the formatted dollars as you go.
   Only use break statements to get out of the loops."""

from basicmodule import *

total_formatted_dollars = 0

while True:
    user_choice = input("Do you want to format a price? (Y/N): ")

    if user_choice.lower() == 'n':
        break  # Exit the main loop if the user chooses 'N'
    elif user_choice.lower() == 'y':
        validNumber = False

        while not validNumber:
            amount = input("Enter the price you would like formatted: ")

            try:
                amount = float(amount)
                validNumber = True
            except ValueError as ex:
                print("\nInput must be a number.\n\nException: %s\n" % ex)
                validNumber = False

        formatted_price = formatToDollars(amount)

