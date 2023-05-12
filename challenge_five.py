"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = f"{name1}{name2}".lower()

t_count = combined_name.count('t')
r_count = combined_name.count('r')
u_count = combined_name.count('u')
e_count = combined_name.count('e')
l_count = combined_name.count('l')
o_count = combined_name.count('o')
v_count = combined_name.count('v')

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

love_score = int(f"{true_count}{love_count}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
