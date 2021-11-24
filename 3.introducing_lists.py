bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].upper())

# Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, 
# Python always returns the last item in the list:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

cars = ["Honda", "Ford", "BMW"]
cars[0] = "Mercedes"  # Lists are mutable
print(cars[0]) 


motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati') #insert we can choose the position of the instertion
motorcycles.append("Volvo") #append always at the end
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print(motorcycles.pop()) #prints only what has been deleted
print(motorcycles)

# If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an 
# item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove,
#  you can use the remove() method.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# The remove() method deletes only the first occurrence of the value you specify. With remove you can specify a value such as "grandma"

# The sort() method changes the order of the list permanently to be in alphabetical order.

# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # if you want to change the order permanently you would use: cars.sort() 

cars.reverse()
print(cars)
print(len(cars))