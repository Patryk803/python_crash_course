# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing 
# each element in the list, one at a time.

names = ["Jess", "Pav", "Patryk"]
print(names[0])


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a
#  message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

names = ["Jess", "Pav", "Patryk"]

message = "Good morning"

print(f"{message} {names[0]}")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores 
# several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars = ["Honda", "Ford", "BMW"]

print(f"I would like to own an {cars[2]}")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least
#  three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guests = ["mum", "dad", "grandma"]
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[1]}")
print(f"Invitiation for a dinner for {guests[2]}")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

guests = ["mum", "dad", "grandma"]
cannot_come = guests.pop()
guests.append("grandad")
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[1]}")
print(f"Invitiation for a dinner for {guests[2]}")
print(f"{cannot_come} cannot come")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found 
# a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

guests = ["mum", "dad", "grandma"]
cannot_come = guests.pop()
guests.append("grandad")
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[1]}")
print(f"Invitiation for a dinner for {guests[2]}")
print(f"{cannot_come} cannot come")

guests.insert(0, "cousin")
guests.insert(2, "aunt")
guests.append("uncle")
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[2]}")
print(f"Invitiation for a dinner for {guests[5]}")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for
#  only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your 
# list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an 
# empty list at the end of your program.

guests = ["mum", "dad", "grandma"]
cannot_come = guests.pop()
guests.append("grandad")
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[1]}")
print(f"Invitiation for a dinner for {guests[2]}")
print(f"{cannot_come} cannot come")

guests.insert(0, "cousin")
guests.insert(2, "aunt")
guests.append("uncle")
print(f"Invitiation for a dinner for {guests[0]}")
print(f"Invitiation for a dinner for {guests[2]}")
print(f"Invitiation for a dinner for {guests[5]}")

print("Sorry, but I can only invite 2 people")
removed_1 = guests.pop()
print(f"Sorry {removed_1}, but I can only invite 2 people")
removed_2 = guests.pop()
print(f"Sorry {removed_2}, but I can only invite 2 people")
removed_3 = guests.pop()
print(f"Sorry {removed_3}, but I can only invite 2 people")
removed_4 = guests.pop()
print(f"Sorry {removed_4}, but I can only invite 2 people")
print(guests)
print(f"Hey {guests[0]} you are still invited")
print(f"Hey {guests[1]} you are still invited")
del guests[1]
del guests[0]
print(guests)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

places = ["Barcelona", "Paris", "NY", "Japan", "Venezuela"]
print(places)
print(sorted(places))
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7, use len() to print a message 
# indicating the number of people you are inviting to dinner.

print(len(guests)) 

# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, 
# rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these
# items and then uses each function introduced in this chapter at least once.

technologies = []
technologies.append("docker")
technologies.append("kubernetes")
technologies.append("jenkins")
technologies.insert(1, "terraform")
print(technologies)
print(sorted(technologies))
technologies.sort()
print(technologies)
print(len(technologies))
technologies.remove("terraform")
technologies.pop()
technologies.reverse()

