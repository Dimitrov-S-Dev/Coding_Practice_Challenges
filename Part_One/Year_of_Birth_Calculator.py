"""Create a script that asks the user to enter their age,
and the script calculates the user's year of birth and prints it out
in a string like in the expected output.
Please make sure you generate the current year dynamically.
"""
from datetime import datetime

today = datetime.now().year
user_age = int(input("Enter your age: "))
year_born = today - user_age
print(f"We think you were born back in {year_born}")
