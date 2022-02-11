# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("In this chapter we're learning about functions")
display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One
# of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Python Crash course")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text on it is as follows: {text}")

make_shirt("M", "Hello shirt")

make_shirt(text = "Hello shirt vol 2", size = "S")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt
# and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = "L", text = "I love Python"):
    print(f"The size of the shirt is {size} and the text on it is as follows: {text}")

make_shirt()
make_shirt("M")
make_shirt("S", "Python is easy")


# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,
# such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of
# which is not in the default country.

def describe_city(city, country = "Iceland"):
    print(f"{city} is in {country}")

describe_city("Reykjavik")
describe_city("Szczecin", "Poland")
describe_city("Barcelona", "Spain")


# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted
# like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    print(f"{city}, {country}")

city_country("Szczecin", "Poland")
city_country("London", "UK")
city_country("N.Y", "US")

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are storing the album information correctly. Use None to add an optional
# parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs,
# add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, year=None):
    music_album = {
        "artist_name":  artist_name,
        "album_title": album_title
    }
    if year:
        music_album["year"] = year
    return music_album

print(make_album("Michael Jackson", "Thriller"))
print(make_album("Shakira", "She wolf"))
print(make_album("Jlo", "Love?", 2011))

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, year=None):
    music_album = {
        "artist_name":  artist_name,
        "album_title": album_title
    }
    if year:
        music_album["year"] = year
    return music_album

while True:
    artist_name = (input("Provide the artist name"))
    if artist_name == "quit":
        break
    album_title = (input("Provide the album title"))
    if album_title == "quit":
        break
    print(make_album(artist_name, album_title))

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

short_msges = ["hello", "yo", "hi", "morning"]
show_messages(short_msges)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the 
# messages were moved correctly.

def show_messages(messages):
    for message in messages:
        print(message)

short_msges = ["hello", "yo", "hi", "morning"]
# show_messages(short_msges)
sent_messages = []

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"The current message is {current_message}")
        sent_messages.append(current_message)

send_messages(short_msges)

print(sent_messages)
print(short_msges)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

def show_messages(messages):
    for message in messages:
        print(message)

short_msges = ["hello", "yo", "hi", "morning"]
sent_messages = []

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"The current message is {current_message}")
        sent_messages.append(current_message)

send_messages(short_msges[:]) #Function call is making a copy of the list to send to the function. 

print(sent_messages) #sent messages appear other way around because of the .pop() method
print(short_msges)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as
# many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.

def order(*sandwiches):
   print("You've ordered the following sandwiches:")
   for sandwich in sandwiches:
      print(f"- {sandwich}")

order("Ham & Bacon", "Cheese & Bacon", "Mushrooms & Mustard")

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and
# last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
   """Build a dictionary containing everything we know about a user."""
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

my_profile = build_profile('Patryk', 'Petryszen', location='Hatfield', field='IT')
print(my_profile)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as
# a color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.

def car_info(manufacturer, model_name, **kwargs):
   kwargs['manufacturer'] = manufacturer
   kwargs['model_name'] = model_name
   # return kwargs
   for k,v in kwargs.items():
      print(k + ":", v)

car = car_info('subaru', 'outback', color='blue', tow_package=True)

# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement
# at the top of printing_models.py, and modify the file to use the imported functions.

import printing_functions

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_completed_models(unprinted_designs, completed_models)

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main
# program file, and call the function using each of these approaches:

from printing_functions import print_completed_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_completed_models(unprinted_designs, completed_models)

from printing_functions import print_completed_models as fn
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
fn(unprinted_designs, completed_models)

import printing_functions as mn
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
mn.print_completed_models(unprinted_designs, completed_models)

from printing_functions import *
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_completed_models(unprinted_designs, completed_models)



