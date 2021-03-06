__author__ = "Nhat Nguyen"

# Lecture 30 - Test Conditions With If, ElIf & Else

# Putting int in front is like casting in Java
# Changes data types from the input (String) to int
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# Control Flow Example
# Note the indentation in the if and else
# The if statement checks the condition age is less or equal than 18
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

# Control Flow Example II
# else if (Java & JavaScript) is elif (Python)
# Bad because repeated lines of code in the if and elif statements
# guess = int(input("Please guess a number between 1 and 10: "))

# if guess < 5:                                               # Enters when guess is greater than 5
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:                                          # When guess is equal to 5
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")     # If did not enter to the previous conditions, enter
# elif guess > 5:                                             # Enters when guess is less than 5
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time")                          # If not, (or guess is equal to 5) enter


# Control Flow Example III (Better Version)
# guess = int(input("Please guess a number between 1 and 10: "))
#
# if guess != 5:                                                # Enters when guess is NOT equal to 5
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower.")
#
#     guess = int(input())
#     if guess == 5:
#         print("Sorry, you have not guessed correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
#
# # Coding Exercise - Using if with strings
# tree1 = 'put your first tree name here'
# tree2 = 'put your second tree name here'
#
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")

# Lecture 31 - More Advanced If, Elif $ Else Processing
