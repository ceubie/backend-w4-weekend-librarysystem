import os
# os.system('cls' if os.name == 'nt' else 'clear')

# Extra classes I have created for increased functionality, possibilities, and integration.

class Library():

    def __init__(self, inventory={}, users={}, authors={}):
        self.inventory = inventory
        self.users = users
        self.authors = authors
        

class Object():

    def __init__(self, users=[], books=[], authors=[]):
        self.users = users
        self.books = books
        self.authors = authors

    def users_who_owe_money(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for user_var_name, user_obj in self.users:
            # Remove the " Dollars" part from the balance string
            balance_str = user_obj._balance.replace(" Dollars", "")
            
            # Convert the remaining string to an integer
            try:
                balance = int(balance_str)
            except ValueError:
                print(f"Error: Unable to convert balance '{balance_str}' to integer.")
                continue
            # Check if the balance is greater than 0
            if balance > 0:
                
                print(f"{user_obj.name}, ID: {user_obj._id}, owes {user_obj._balance}!")
# Author: A class representing book authors with attributes like name and biography.


class Author():

    def __init__(self, name, bio, books=[]):
        self._name = name
        self._bio = bio
        self.books = books


    def get_info(self):
        counter = 1
        print("-" *50)
        print(self._name)
        print()
        print(self._bio)
        print()
        print("Here are the authors books:")
        for book in self.books:
            print(counter, " - ", book)
            counter += 1
        print("-" *50)

        
# Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.

class Book():

    def __init__(self, title, author, genre, published, available = True):
        self._title = title
        self._author = author
        self._genre = genre
        self._published = published
        self.available = available

    def get_info(self):
        print("-" *50)
        print(self._title)
        print(self._author)
        print(self._published)
        print(self.available)
        print("-" *50)


# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.


class User():

    def __init__(self, name, id, balance = 0, borrowed={}):
        self.name = name
        self._id = id
        self._balance = balance
        self.borrowed = borrowed
        

    def get_info(self):
        counter = 1
        print("-" *50)
        print(self.name)
        print(self._id)
        print(self._balance)
        for book in self.borrowed:
            print(counter, " - ", book)
            counter += 1
        print("-" *50)