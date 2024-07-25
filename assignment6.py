"""create a sqlite database called "yourname.db".
create a table in the database called "survey" with the following fields:

id PRIMARY
choice TEXT

Create a python application that runs in a loop. It first asks the user if they want to submit their favourite color. If they select yes, ask them what it is. Give them the selection of 1 - Black, 2 - White, 3 - Red, 4 - Blue, 5 - Green, or 9 - Quit.

If they make an invalid selection, tell them they have made an invalid selection and give them the color options again.

When they have submitted a valid color, insert it into the database. (insert it as "1 - Black" or "4 - Blue"

keep asking them if they want to submit their favourite color again, until they select no (this is the loop part)

When the program ends, query the results of all the colors that we submitted and output the totals for each."""

import sqlite3

connection = sqlite3.connect("yourname.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS survey(id INTEGER PRIMARY KEY,choice TEXT)")
connection.commit()

user = ""
fav_color = ""

while fav_color != 'no':
    fav_color = input("Would you like to submit your favourite color? yes or no:")
    if fav_color.lower() == 'no':
        break
    elif fav_color.lower() == 'yes':
        print("choose your favourite color: ")
        print("1- Black\n2- White\n3- Red\n4- Blue\n5- Green\n9- Quit\n\n")
        option = input("Select one color ")

        if option in ['1', '2', '3', '4', '5']:
            colors = {'1': 'Black', '2': 'White', '3': 'Red', '4': 'Blue', '5': 'Green'}
            chosen_color = f"{option}-{colors[option]}"
            print(f"You chose:{chosen_color}")

            if chosen_color == "1-Black":
                user = "Black"
            elif chosen_color == "2-White":
                user = "White"
            elif chosen_color == "3-Red":
                user = "Red"
            elif chosen_color == "4-Blue":
                user = "Blue"
            elif chosen_color == "5-Green":
                user = "Green"

            cursor = connection.cursor()
            cursor.execute("INSERT INTO survey VALUES (NULL, '" + user + "');")
            connection.commit()

        elif option == '9':
            break
        else:
            print("Invalid input. Please choose a valid option.")

connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute("SELECT * FROM survey")
rows = cursor.fetchall()

totalBlack = 0
totalWhite = 0
totalRed = 0
totalBlue = 0
totalGreen = 0

for each_row in rows:
    if each_row["Choice"] == "Black":
        totalBlack += 1
    elif each_row["Choice"] == "White":
        totalWhite += 1
    elif each_row["Choice"] == "Red":
        totalRed += 1
    elif each_row["Choice"] == "Blue":
        totalBlue += 1
    elif each_row["Choice"] == "Green":
        totalGreen += 1

print("\nTotal counts for each color (from individual counters):")
print(f"Black: {totalBlack}")
print(f"White: {totalWhite}")
print(f"Red: {totalRed}")
print(f"Blue: {totalBlue}")
print(f"Green: {totalGreen}")

cursor.close()
connection.close()