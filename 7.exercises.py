# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such
# as “Let me see if I can find you a Subaru.”

"""
car = input("What's the brand of the car you want to buy?\n").title()
print(f"Let me see if I can find you a {car}")
"""

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
# print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
dinner_group = input("How many people are in your dinner group?\n")
if int(dinner_group) > 8:
    print("You will need to wait for the table")
else:
    print("Come, the table is ready for you")
"""

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

# number = input("Please provide the number:\n")
# if int(number) & 10 == 0:
#     print("the number is multiple of 10")
# else:
#     print("The number is not multiple of 10")


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

# prompt = "Add your pizza's topping\n"
# prompt += "to quit submit quit\n"
# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(f"Adding {message}")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is 
# free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# and then tell them the cost of their movie ticket.


# while True:
#     age = int(input("How old are you?"))
#     if 3 <= age <= 12:
#         print("The ticket for your age is $10")
#     elif age > 12:
#         print("The ticket for you is 15$")
#     elif age < 3:
#         print("You have a free ticket")
#     else:
#         break


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it
# to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


# sandwich_orders = ["Baja Chicken & Bacon", "Chicken & Bacon Ranch", "Baja Steak & Jack", "Buffalo Chicken"]
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made you a {current_sandwich} ")
#     finished_sandwiches.append(current_sandwich)
# print("The following sandwiches have been done: ")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich}")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ["pastrami", "Baja Chicken & Bacon", "pastrami", "Chicken & Bacon Ranch", "Baja Steak & Jack", "pastrami", "Buffalo Chicken"]
# finished_sandwiches = []

# print("Sorry, the deli run out of pastrami")

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made you a {current_sandwich} ")
#     finished_sandwiches.append(current_sandwich)
# print("The following sandwiches have been done: ")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich}")

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in
# the world, where would you go? Include a block of code that prints the results of the poll.

favourite_places = {}
polling_active = True
while polling_active:
   name = input("What's your name?\n").title()
   place = input("If you could visit one place in the world, where would you go?\n")

   favourite_places[name] = place #store the information in the dictionary as a key, value pairs. name: place

   add_another = input("Do you want to add somebody else?")
   if add_another != "yes":
       polling_active = False

print("Answers: \n")
for name, place in favourite_places.items():
    print(name + " wants to visit " + place)

