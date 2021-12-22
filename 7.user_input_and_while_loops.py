"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
"""

# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder
"""
if number % 2 == 0:
   print(f"\nThe number {number} is even.")
else:
   print(f"\nThe number {number} is odd.")
"""


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#    message = input(prompt)
#    print(message)

# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:  # A loop that starts with while True will run forever unless it reaches a break statement.
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of
# the loop based on the result of a conditional test.

# Code to print odd numbers using a while loop below
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track
# of the items in the list. To modify a list as you work through it, use a while loop.

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#    print(f"Verifying user: {current_user.title()}")
#    confirmed_users.append(current_user)

# # Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#    print(confirmed_user.title())


# Say you have a list of pets with the value 'cat' repeated several times. To remove all instances of that value, you can run a while
# loop until 'cat' is no longer in the list, as shown here:
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# You can prompt for as much input as you need in each pass through a while loop. Let’s make a polling program in which each pass through the
# loop prompts for the participant’s name and response.

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
   # Prompt for the person's name and response.
   name = input("\nWhat is your name? ")
   response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary.
   responses[name] = response

# Find out if anyone else is going to take the poll.
   repeat = input("Would you like to let another person respond? (yes/ no) ")
   if repeat == 'no':
      polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
   print(f"{name} would like to climb {response}.")
