#Create a function named sortName(firstname, lastname, sortorder = "firstlast")
# that has an optional parameter sortorder. This will be defaulted at "firstlast"
# but the user can also input "lastfirst".
# If it is left at default, print out the name as "First Last".
# If they select "lastfirst" print out the name as "Last, First".
# Write a program that will ask the user for their first and last name,
# then supply these to the sortName function for both default and lastfirst sortorder.

def sortName(firstname, lastname, sortorder="firstlast"):
    if sortorder == "firstlast":
        return firstname + "" + lastname
    elif sortorder == "lastfirst":
        return lastname + "" + firstname
    else:
        return "Invalid sort order"


firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")

default_sorted_name = sortName(firstname, lastname)

last_first_sorted_name = sortName(firstname, lastname, sortorder="lastfirst")

print("Default Sort Order:", default_sorted_name)
print("Last-First Sort Order:", last_first_sorted_name)