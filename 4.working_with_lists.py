magicians = ['alice', 'david', 'carolina']
for magician in magicians:
     print(magician)

for value in range(0, 10):
    print(value)

for value in range(5): #by default the start is 0
    print(value)

# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.
numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), 
# Python uses that value as a step size when generating numbers.
# For example, here’s how to list the even numbers between 1 and 10:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squared_numbers = []
for number in range(1,11):
    squared_numbers.append(number**2)
print(squared_numbers)

numbers = [1,23,4,5,5,7,5,45]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#List comprehension
squares = [value**2 for value in range(1,11)]

#tuples 
# Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to
#  define a tuple with one element, you need to include a trailing comma:
#     my_t = (3,)
# It doesn’t often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.

# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple. So if we wanted to change our dimensions,
#  we could redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# PEP 8 recommends that you use four spaces per indentation level.
# Mixing tabs and spaces in your file can cause problems that are very difficult to diagnose. If you think you have a mix of tabs and spaces,
#  you can convert all tabs in a file to spaces in most editors.



