# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that
# are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another
# method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, sex, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.job_title = job_title

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old. Sex: {self.sex} with occupation {self.job_title}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

user1 = User("Patryk", "Petryszen", 28, "male", "Network Engineer")
user1.describe_user()
user1.greet_user()
user2 = User("Jan", "Kowalski", 50, "male", "Civil Engineer")
user2.describe_user()
user2.greet_user()
user3 = User("Magda", "Matkowksa", 25, "female", "receptionist")
user3.describe_user()
user3.greet_user()