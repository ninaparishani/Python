
#Create a program that takes in a sentence from the user
# and reverses all the characters using a loop.
#Print the original sentence and then the reversed one.

sentence=input("Input a sentence to be reversed:")
reversedSentence=""

counter=len(sentence)-1

while counter>= 0:
    reversedSentence += sentence[counter]
    counter -= 1

print("Original Sentence:"+ sentence)
print("Reversed Sentence:"+reversedSentence)