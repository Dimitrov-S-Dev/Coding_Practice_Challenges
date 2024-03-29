import requests
from random import choice
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKE 3000!")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

resp = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":user_input}
)

data = resp.json()
results = data["results"]

num_jokes = (data["total_jokes"])
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
    print(choice(results)["joke"])

elif num_jokes == 1:
    print("There is one joke")
    print(results[0]["joke"])

else:
    print(f"Sorry , couldn't find a joke with your term: {user_input}!")