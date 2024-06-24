from classes import Author, User, Book
import re
from collections import defaultdict
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________

def export_library(x):

    with open("library.txt", "w") as file:
        for author, books in x.items():
            for book, details in books.items():
                file.write(f"{author}-:-{book}-:-{details['Genre']}-:-{details['Published']}-:-{details['Available']}\n")

#________________________________________________________________________________________________________________________________________________


def import_library(x):
    library_dict = {}

    with open(x, "r") as file:
        for line in file:
            line = line.strip()
            data = re.search(r"^(.+?)-:-(.+?)-:-(.+?)-:-([\w\/ ]+)-:-(True|False)$", line)

            if data:
                name = data.group(1).strip()
                book = data.group(2).strip()
                genre = data.group(3).strip()
                published = data.group(4).strip()
                available = data.group(5).strip()

                if name not in library_dict:
                    library_dict[name] = {book: {"Genre": genre, "Published": published, "Available": available}}
                else:
                    library_dict[name].update({book: {"Genre": genre, "Published": published, "Available": available}})
            else:
                print(f"No match found for line: {line}")

    return library_dict
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________

def export_users(y):

    with open("users.txt", "w") as file:
        for user, info in y.items():    
            file.write(f"{user}-:-{info['ID']}-:-{info['Balance']}-:-{info['Books Borrowed']}\n")

#________________________________________________________________________________________________________________________________________________


def import_users(y):
    user_dict = {}

    with open(y, "r") as file:
        for line in file:
            line = line.strip()
            # Adjust the regex pattern to match the expected format
            data = re.search(r"([\w\s]+)-:-(\d+)-:-(\d+ [Dd]ollars)-:-\[(.*)\]", line, re.IGNORECASE)

            if data:
                user = data.group(1)
                id = int(data.group(2))
                balance = data.group(3)
                books_borrowed_raw = data.group(4)

                # Parse the books_borrowed field
                if books_borrowed_raw:
                    
                    books_borrowed = re.findall(r"\('([^']+)',\s*'([^']+)'\)", books_borrowed_raw)
                    books_borrowed = [(book.strip(), author.strip()) for book, author in books_borrowed]
                else:
                    books_borrowed = []

                user_dict[user] = {
                    "ID": id,
                    "Balance": balance,
                    "Books Borrowed": books_borrowed
                }
            else:
                print(f"No match found for line: {line}")

    return user_dict
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________


def export_authors(x):
    with open("authors.txt", "w") as file:
        for author, details in x.items():
            bio = details["Bio"]
            books = details["Books"]
            books_str = ", ".join([f"'{book}'" for book in books])  # Format books list as a string

            file.write(f"{author}-:-{bio}-:-[{books_str}]\n")

#________________________________________________________________________________________________________________________________________________   


def extract_authors_data(z):
    authors = {}

    with open(z, 'r') as file:
        for line in file:
            line = line.strip()
            # Adjust the regex pattern to match the expected format
            data = re.search(r"([\w\s]+)-:-(.+)-:-(\[.*\])", line)

            if data:
                author_name = data.group(1).strip()
                bio = data.group(2).strip()
                books_str = data.group(3).strip()

                # Convert the books list from string to Python list
                books = re.findall(r"'([^']+)'", books_str)

                # Store the data in the authors dictionary
                authors[author_name] = {
                    "Bio": bio,
                    "Books": books
                }
            else:
                print(f"No match found for line: {line}")
    return authors

#________________________________________________________________________________________________________________________________________________   
#________________________________________________________________________________________________________________________________________________   

def export_genres(s):

    with open("genres.txt", "w") as file:
        for genre, description in s.items():
            file.write(f"{genre}-:-{description}\n")

#________________________________________________________________________________________________________________________________________________   

def import_genres(s):
    genres = {}

    with open(s, "r") as file:
        for line in file:
            line = line.strip()
            data = re.search(r"([\w\s]+)-:-(.+)", line)
            if data:
                genre = data.group(1)
                description = data.group(2)

                genres[genre] = description
            
            else:
                print(f"No match found for line: {line}")

    return genres

#________________________________________________________________________________________________________________________________________________   
#________________________________________________________________________________________________________________________________________________   

def display_books(): 
    
    lib_data = import_library("library.txt")
    book_counter = 1

    for key, value in lib_data.items():
            
            print()
            print(f"{key.upper()}:")
            print("~" * len(key))
            print()
    
            for key1, value1 in lib_data[key].items():
                print(f"{book_counter}) {key1} {value1}")
                print()
                book_counter += 1
            book_counter = 1
            print("-" * 80)

    
#________________________________________________________________________________________________________________________________________________

def display_users(): 
    
    user_data = import_users("users.txt")
    sorted_keys = sorted(user_data.keys())

    for key in sorted_keys:
        print(f"{key}:")
        print()
        print(user_data[key])
        
        print("-" * 80)

#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________   

def book_operations(x):
    
    while True:

        a = input(""" 
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

                Book Operations:
             
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                6. Go back
             
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
             """)
        
        if a == "1":
            
            book_counter = 1
            book = input("What is the name of the new book? ")
            author = input("Who is the author? ")
            genre = input("What is the genre? ")
            publish = input("When was it published? ")

    #__  ______Checking existence of author, adding to inventory, creating book object_____________________
            if author in x:
                author.update({book :{"Genre": genre, "Published": publish, "Available": True}})               
                globals()[book.lower()] = Book(book, author, genre, publish)

            else:
                x.update({author : {book : {"Genre": genre, "Published": publish, "Available": True}}})

    #__  __  __Creating author, book objects in else statement___________________________________________
                author = author.lower()
                globals()[author] = Author(author.capitalize(), input("Please enter a bio for this author, as we do not have them in our library "))
                globals()[author].books.append(book)
                
                globals()[book.lower()] = Book(book, author, genre, publish)
                print("-" * 80)

            export_library(x)

    #_____    Iterating over inventory by author, and their books___________________________________            
            for key, value in x.items():
                print(f"{key}:")
                print()
        
                for key1, value1 in x[key].items():
                    print(f"{book_counter}) {key1} {value1}")
                    book_counter += 1
                book_counter = 1
                print("-" * 80)
            
#______  ___________________________________________________________________________________________


        if a == "2":
            a = input("Who is the author? ")   
            b = input("What is the name of your book? ")
            for writer, books in x.items():
                for novel, items in books.items():
                    if a == writer and b == novel:
                        x[writer][novel]["Available"] = False
                        print(f"{x[writer][novel]} - Available = {x[writer][novel]["Available"]}")
                    else:
                        continue     
                export_library(x)             #### Add for loop to look for user id, and add book to user book list


        if a == "3":
            a = input("Who is the author? ")   
            b = input("What is the name of your book? ")
            for writer, books in x.items():
                for novel, items in books.items():
                    if a == writer and b == novel:
                        x[writer][novel]["Available"] = True
                        print(f"{x[writer][novel]} - Available = {x[writer][novel]["Available"]}")
                    else:
                        continue
                export_library(x)              #### Add for loop to look for user id, and return book


        if a == "4":
            search = import_library("library.txt")
            w = input("What book would you like to search for? ")
            v = input("Who is the author? ")
            print("-" * 80)
            

            book_found = False
            for aut, novels in search.items():
                if v == aut:
                    if w in novels:
                        print("Book found!")
                        print()
                        print()
                        print(f"{aut} - {w}")
                        print()
                        
                        print(search[aut][w])
                        book_found = True
                        break  

            if not book_found:
                print("Book not found")

            print("-" * 80)

        if a == "5":
            display_books()

        if a == "6":
            break


#________________________________________________________________________________________________________________________________________________


def user_operations(y):
    search_dict = import_users("users.txt")

    while True:

        a = input("""
                  
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                User Operations:
                  
                1. Add a new user
                2. View user details
                3. Display all users
                4. Go back

                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
                  
                  """)
        
        if a == "1":
            lastkey, lastvalue = list(search_dict.items())[-1]
            lastid = lastvalue["ID"]

            name = input("What is the new user's name? ")
            id = lastid + 1

            if name in y.keys():
                print("User already exists")
            else:
                y.update({name : {"ID": id, "Balance": "0 Dollars", "Books Borrowed":[]}})
                name = name.lower()
                globals()[name] = User(name, id)
            export_users(y)


        if a == "2":
            name = input("What is the new user's name? ")
            search_dict = import_users("users.txt")

            for user, info in search_dict.items():
                if user in search_dict and user == name:
                    print("-" * 80)
                    print(f"{user} info:")
                    print()
                    print(info)
                    print("-" * 80)
                    
                else:
                    continue


        if a == "3":
            display_users()

        if a == "4":
            break


#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________

def author_operations(z,x):
    while True:
        
        a = input("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    Author Operations:

                    1. Add a new author
                    2. View author details
                    3. Display all authors
                    4. Go back
                
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                """)
        

        if a == "1":
            name = input("What is the name of the author you would like to add? ")

            if name in z.keys():
                print("Author is already in our library ")
            
            else:
                bio = input("Would you like to add a bio for this author? If no put 'None' ")

                while True:
                    inventory_update = input("Would you like to add a book by this author to the library inventory? y/n ")

                    if inventory_update == "y":
                        b = input("What is the name of the book? ")
                        c = input("What is the genre? ")
                        d = input("When was it published? ")
                        z.update({name : {b: {"Genre": c, "Published": d, "Available" : True}}})
                        

                    elif inventory_update == "n":
                        break
                

                x[name] = {
                        "Bio": bio,
                        "Books": list(z[name].keys())
                    }
            export_library(z)
            export_authors(x)

        if a == "2":
            extractbio = extract_authors_data("authors.txt")
            name = input("What is the name of the author you would like to view? ")

            found_author = False

            for author, info in z.items():
                if author == name:
                    found_author = True
                    print("-" * 100)
                    print()
                    print(f"{author.upper()}:")
                    print("~" * len(author))
                    
                    print()
                    print(extractbio.get(name, {}).get("Bio", "Bio not found"))
                    print()
                    print()
                    print(f"Books by {author} we have in stock:")
                    print()
                    for book, details in info.items():
                        print(f"- {book}: {details}")
                        print()
                        # for key, value in details.items():
                        #     print(f"- {book} -  {key}: {value}")
                    print("-" * 100)

            if not found_author:
                print("Author not found")

        if a == "3":
            print("-" * 80)
            print()
            print("Here is our list of authors:")
            print()       
            for keys in z.keys():
                print(f"- {keys}")
                print()
            print("-" * 80)
        
        if a == "4":
            break


#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________


def genre_operations():
    while True:
        genre_import = import_genres("genres.txt")

        a = input("""

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            Genre Operations:
            
            1. Add a new genre with genre details.
            2. View genre details.
            3. Display a list of all genres.
            4. Sort books by genre
            5. Go back
            
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
        
        if a == "1":
            while True:
               confirm = input("Confirm add genre. y/n")
               if confirm == "y":
                   name = input("What is the name of the new genre? ")
                   if name in genre_import:
                       print("That genre already exists in our library")
                   else:
                       description = input("Please give a description of the genre")
                       genre_import.update({name:description})
                       export_genres(genre_import)
                       break
               else:
                   break

        if a == "2":
             n = input("What genre would you like to view? ")
             if n in genre_import.keys():
                    for genre, description in genre_import.items():
                            if n == genre:
                                print("-" * 100)
                                print()
                                print(f"{genre}:")
                                print("~" * len(genre))
                                print()
                                print(description)
                                print()
                                print("-" * 100)
                            else:
                                continue
        if a == "3":
            for genre in genre_import.keys():
                print(f"- {genre}")
                print()
          
        if a == "4":                                            
            inventory = import_library("library.txt")
            # Dictionary to hold books grouped by genre and author
            books_by_genre = defaultdict(lambda: defaultdict(list))

            # Populate the dictionary with books grouped by genre and author
            for author, books in inventory.items():
                for book_name, book_details in books.items():
                    genre = book_details["Genre"]
                    books_by_genre[genre][author].append((book_name, book_details))

            # Print the sorted library with genre categories as headers
            for genre, authors_books in books_by_genre.items():
                print(f"--- {genre} ---")
                for author, books_list in authors_books.items():
                    print(f"{author}:")
                    for book_name, book_details in books_list:
                        print(f"\t{book_name}")
                        for key, value in book_details.items():
                            if key != "Genre":
                                print(f"\t\t{key}: {value}")
                    print()  # Print an empty line for separation between authors


        if a == "5":
            break


#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________


# Create 3 functions to make objects out of all library items by importing data from text files


def create_user_objects():      # User(self, name, id, balance = 0, borrowed={})
    
    user_list = []
    user_dict = import_users("users.txt")
    for user, details in user_dict.items():
        # for info, items in user.items():
            x = user.replace(" ", "_")
            x = x.lower()
            globals()[x] = User(user, details["ID"], details["Balance"], details["Books Borrowed"])
            user_list.append((x, globals()[x])) # appends list with tuples of (variable_name, object)


    return user_list

#______________________________________________________________________________________________________________


def create_book_objects():       # Book(self, title, author, genre, published, available = True)
    
    book_list = []
    library_dict = import_library("library.txt")

    for author, books in library_dict.items():
        for book_title, info in books.items():
            var_name = f"{book_title}_{author}".replace(" ", "_").lower()
            globals()[var_name] = Book(book_title, author, info["Genre"], info["Published"], info["Available"])
            book_list.append((var_name, globals()[var_name]))

    return book_list

#______________________________________________________________________________________________________________


def create_author_objects():      # Author(self, name, bio, books=[])
    
    author_list = []
    author_dict = extract_authors_data("authors.txt")
    for author, info in author_dict.items():

        var_name = f"{author}".replace(" ", "_").lower()
        globals()[var_name] = Author(author, info["Bio"], info["Books"])
        author_list.append((var_name, globals()[var_name]))

  
    return author_list
    

#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________
