name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name ="ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

print("\tPython")
print("\nPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

fav = "     python    "
new_fav = fav.lstrip() #left strip, removes the whitespaces on the left
print(new_fav)

# When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:

# >>> universe_age = 14_000_000_000

# When you print a number that was defined using underscores, Python prints only the digits:

# >>> print(universe_age)
# 14000000000




# Constants
# A constant is like a variable whose value stays the same throughout the life of a program. Python doesn’t have built-in constant types, 
# but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:

# MAX_CONNECTIONS = 5000

# When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.



