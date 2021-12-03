# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you
#  should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or 
# more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas = ["tartufo", "margerita", "crudo"]

for pizza in pizzas: 
    print(f"I like {pizza} pizza")
print("I really love pizza")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then
# use a for loop to print out the name of each animal. Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a 
# great pet!

animals = ["jaguar", "puma", "lion"]

for animal in animals:
    print(f"This {animal} would be a great home pet")
print("That was a joke")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range(1,21):
    print(number)

numbers = list(range(1,21))
print(numbers)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long,
#stop it by pressing CTRL-C or by closing the output window.)

# numbers = list(range(1,1000001))

# for number in numbers:
#     print(number)

# squares = [print(value) for value in range(1,1000001)]

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at 
# one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))
#or
# numbers = []
# for number in range(1,1000001):
#     numbers.append(number)
  
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

print(list(range(1, 21, 2)))

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

lista = []

for number in range(3, 31, 3):
    lista.append(number)
print(lista)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10
#  cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

for number in range(1, 11):
    print(number**3)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [value**3 for value in range(1,11)]
print(cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

cubes = [value**3 for value in range(1,11)]

print(f"The first three numbers are: {cubes[0:3]}")
print(f"Three items from the middle of the lists are: {cubes[5:8]}")
print(f"The last three items in the list are: {cubes[-3:]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
#  Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message
#  My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

pizzas = ["tartufo", "margerita", "crudo"]

for pizza in pizzas: 
    print(f"I like {pizza} pizza")
print("I really love pizza")

friend_pizzas = pizzas[0:]

pizzas.append("Hawai")
friend_pizzas.append("Prosciuto")

for pizza in pizzas: 
    print(f"My favorite pizzas are {pizza}")

for pizza in friend_pizzas: 
    print(f"My friend’s favorite pizzas are {pizza}")

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version
#  of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']

for food in my_foods:
    print(food)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use
# a for loop to print each of the items on the revised menu.

menu = ("potatoes", "fries", "hamburger", "coke", "ice-cream")
for dish in menu:
    print(dish)

#menu[0]= "soup"
menu = ("potatoes", "fries", "hamburger", "pizza", "soup")
for dish in menu:
    print(dish)
