#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called 
#increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the
#value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts
#to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, sex, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.job_title = job_title
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old. Sex: {self.sex} with profession {self.job_title}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Patryk", "Petryszen", 28, "male", "Network Engineer")
user1.describe_user()
user1.greet_user()
user2 = User("Jan", "Kowalski", 50, "male", "Civil Engineer")
user2.describe_user()
user2.greet_user()
user3 = User("Magda", "Matkowksa", 25, "female", "receptionist")
user3.describe_user()
user3.greet_user()

user1.increment_login_attempts()
print(user1.increment_login_attempts())
user1.reset_login_attempts()
print(user1.increment_login_attempts())