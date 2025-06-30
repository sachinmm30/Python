#INHERITANCE
#1
class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

child = Child("Gowda", "Ajay")
print(f"{child.name} {child.surname}")  # Inherits surname from Family

#2
class User:
    def __init__(self, username, ):
        self.username = username
        #self.__password = password

    def login(self):
        print(f"{self.username} logged in....")

class Admin(User):
    def delete_user(self):
        print(f"{self.username} deleted the user")

a = Admin("sachin")
#print(a.username)
#a.login()
a.delete_user()


#POLYMORPHISM
#1
class Animal:
    def make_sound(self):
        print()

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()

#2

class Notification:
    def send(self):
        print("notification sent")

class EmailNotification(Notification):
    def send(self):
        print("Email sent")

class SMSNotification(Notification):
    def send(self):
        print("Sms Sent")

