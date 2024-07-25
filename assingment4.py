#Part 1.
# Create an array to hold names.
# Allow the user to put in 5 guesses at a secret name
# Create a variable secretname that holds a secret name
# Create a function that uses a loop to go through each name.
# Check to see if the element in the array matches the secret name value.
# if it does, break out of the loop. return true
# if the secret name was found, false if not found.
# Name the function "checkNameGuesses(guesses, secretname)"

#Part 2.
# Create a function that uses a loop to output each name
# in the list in reverse order from last element to first.
# write these results to a file.
# Call this function "reverseNamesAndWriteToFile(names)"

def checkNameGuesses(guesses, secretname):
    for name in guesses:
        if name == secretname:
            return True
    return False

def reverseNamesAndWriteToFile(names):
    reverseNames=[]
    counter = len(names)-1
    while counter >= 0:
        reverseNames.append(names[counter])
        counter-=1



    file= open("result.txt", "w+")
    for name in reverseNames:
        file.write(name + "\n")
    file.close()




guesses=[]
secretname = "Alice"
counter=1

while counter<=5:
    guesses.append(input("Please enter your guess"+ str(counter)+":"))
    counter+=1
    result = checkNameGuesses(guesses, secretname)
    if result==True:
        break


if result==True:
    print("You guessed the secret name. It was:"+ secretname)

else:
    print("The secret name was not found. Please try again")


reverseNamesAndWriteToFile(guesses)



