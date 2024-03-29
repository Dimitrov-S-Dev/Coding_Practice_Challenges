# from csv import reader

# using reader

# with open("fighters.csv", "r") as file:
#     content = reader(file)
#     next(content)
#     for fighter in content:
#         print(f"{fighter[0]} is from {fighter[1]}")

# or

# with open("fighters.csv", "r") as file:
#     content = reader(file)
#     data = list(content)
#     for name, country, _ in data[1:]:
#         print(f"{name} is from {country}")

#--------------------------------------------

# using DictReader -> OrderedDict

from csv import DictReader

with open("fighters.csv", "r") as file:
    content = DictReader(file)
    for row in content:
        print(f"{row['Name']} is from {row['Country']}")
