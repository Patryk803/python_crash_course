# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they
# live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person_details = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 32,
    "city": "London"
}

for info in person_details:
    print(info,":", person_details[info])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of
# a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun,
# poll a few friends and get some actual data for your program.

ppls_favourite_numbers = {
    "patryk": 3,
    "Jack": 8,
    "Stuart": 15,
    "John": 22,
    "Paul": 15
}

for number in ppls_favourite_numbers:
    print(number, ":", ppls_favourite_numbers[number])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
# their meanings as values. Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and
# then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n)
# to insert a blank line between each word-meaning pair in your output.

words = {
    "string": "It's just a string",
    "integer": "a number",
    "float": "number with decimals",
    "list": "you defined it with []",
    "tuples": "immutable defined with ()"
}

for word in words:
    print(word, ":", words[word])

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

words = {
    "string": "It's just a string",
    "integer": "a number",
    "float": "number with decimals",
    "list": "you defined it with []",
    "tuples": "immutable defined with ()"
}

for k, v in words.items():
    print(k, v)

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If
# they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }

peoples = ['jen', 'patryk', 'jerry', 'edward']

for people in peoples:
    if people in favorite_languages.keys():
        print(f"{people} you don't need to take a part you already in the pool")
    if people not in favorite_languages.keys():
        print(f"{people} please take a part in the vote!")



# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print 
# everything you know about each person.

person_details_1 = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 32,
    "city": "London"
}

person_details_2 = {
    "first_name": "Anna",
    "last_name": "Kowalska",
    "age": 21,
    "city": "Szczecin"
}

person_details_3 = {
    "first_name": "Jarry",
    "last_name": "White",
    "age": 22,
    "city": "London"
}

people = [person_details_1, person_details_2, person_details_3]

for person in people:
    name = person["first_name"].title() + " " + person["last_name"].title()
    age = person["age"]
    city = person["city"]
    print(name, age, city)

# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal
# and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you
# know about each pet.

pet1 = {
    "kind": "dog",
    "owner's name": "Patryk"
}

pet2 = {
    "kind": "cat",
    "owner's name": "Asia"
}

pets =[pet1, pet2]

for pet in pets:
    print(pet["owner's name"] + " has a " + pet["kind"])


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three
# favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop
# through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    "Patryk": ["Spain", "UK", "Portugal"],
    "Joanna": ["Spain", "Poland", "Greece"],
    "Anna": ["Spain", "USA", "Italy"]
}

"""
name = input("What's your name?\n").title()
if name == "Patryk" or name == "Joanna" or name =="Anna":
    print(f"Hey {name}")
    favorite_place = input(f"What's your favorite place {name}\n").title()
    if favorite_place not in favorite_places[name]:
        favorite_places[name].append(favorite_place)
        # print(f"{name} your favorites places are {favorite_places[name]}")
        for name, places in favorite_places.items():
            print(f"{name} likes the following places:")
            for place in places:
                print("- " + place)
        
else:
    print(f"Sorry {name} you are not allowed to play this game")
"""

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

ppls_favourite_numbers = {
    "Patryk": [3,5],
    "Jack": [8,3],
    "Stuart": [15,14],
    "John": [22,25],
    "Paul": [45, 85]
}

for name, numbers in ppls_favourite_numbers.items():
    print(f"{name} likes the following numbers:")
    for number in numbers:
        print("- " + str(number))

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information
# about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s
# dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    "Szczecin": ["Poland", "400k", "old Stetin"],
    "London": ["UK", "10mln", "where the wimbledon takes place"],
    "Hatfield": ["UK", "60k", "Ocado's headquarters"]
}

for name, infos in cities.items():
    print(f"{name}:")
    for info in infos:
        print("- " + info)


