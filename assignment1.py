name = input("Please enter your name:")
age = input("Please enter your Age:")
print('Welcome,' + name)
age = int(age)
if age < 5:
    print("You are very young")
elif age >= 5 and age < 15:
    print("You are young")
elif age >= 15 and age < 30:
    print("You are a young adult")
elif age >= 30 and age < 50:
    print("You are an adult")
elif age >= 50 and age < 65:
    print("You are middle aged")
else:
    print("You are a senior citizen")