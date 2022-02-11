# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call 
# describe_restaurant() for each instance.

class Restaurant:
      def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type

      def describe_restaurant(self):
            print(self.name + " is an " + self.cuisine_type + " restaurant")

      def open_restaurant(self):
            print(f"The {self.name} is open")

restaurant1 = Restaurant("Bollywod", "Indian")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("KFC", "American")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Mekong", "Chinese")
restaurant3.describe_restaurant()