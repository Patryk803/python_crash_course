requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
       print(f"{user.title()}, is not banned.")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
   print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
   if requested_topping in available_toppings:
          print(f"Adding {requested_topping}.")
   else:
          print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

