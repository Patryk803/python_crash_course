alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Dictionaries are mutable
#We can add new values for our already created dictionary:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#We can remove key value pair from the dictionary
del alien_0['points']
print(alien_0)

#If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation.
alien_0 = {'color': 'green', 'points': 5}

print(alien_0.get("error")) #error doesn't exist so python will print None instead of giving an error

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items(): #the .items method 
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys(): #The keys() method isn’t just for looping: it actually returns a list of all the keys
   print(name.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
   print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }

print("The following languages have been mentioned:")
for language in favorite_languages.values(): #same for .values
   print(language.title())



print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set means that each value needs to be unique
   print(language.title())

#We build sets using curly braces
languages = {'python', 'ruby', 'python', 'c'}

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
   print(alien)

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
   print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# It’s common to store a number of dictionaries in a list when each
# dictionary contains many kinds of information about one object.



# Rather than putting a dictionary inside a list, it’s sometimes useful
# to put a list inside a dictionary.
# Store information about a pizza being ordered.
pizza = {
   'crust': 'thick',
   'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")

for topping in pizza['toppings']:
   print(f"\t{topping}")
