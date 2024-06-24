from classes import Library, Object, Author, Book, User
from functions import book_operations, user_operations, author_operations, genre_operations, import_library, import_users, extract_authors_data, create_author_objects, create_book_objects, create_user_objects
import re

library = Library(import_library("library.txt"), import_users("users.txt"), extract_authors_data("authors.txt"))
objects = Object(create_user_objects(), create_book_objects(), create_author_objects())





def app():

    while True:

        a = input(""" 
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Welcome to the Library Management System!

                  
                  
                Main Menu:
                  
            1. Book Operations
            2. User Operations
            3. Author Operations
            4. Genre Operations
            5. Programmer Operations
            6. Quit
            
                  
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

        if a == "1":
          book_operations(library.inventory)
        if a == "2":
           user_operations(library.users)
        if a == "3":
           author_operations(library.inventory, library.authors)
        if a == "4":
           genre_operations()
        if a == "5":
            while True:

               password = input("""

      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              
           What is best practice for printing the following list item?
                              

            l = [vanilla, chocolate, strawberry, coffee, cookie dough]
                                                         ^^^^^^^^^^^^

                          (enter, "exit" to go back)
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              
   """)
               if password == "print(l[-1])":
                  while True:
                     a = input("""

   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   __          __  _                            _____                                                         _ 
   \ \        / / | |                          |  __ \                                                       | |
   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |__) | __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___   ___ _ __| |
      \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__| |
      \  /\  /  __/ | (_| (_) | | | | | |  __/ | |   | | | (_) | (_| | | | (_| | | | | | | | | | | |  __/ |  |_|
      \/  \/ \___|_|\___\___/|_| |_| |_|\___| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|\___|_|  (_)
                                                                  __/ |                                          
                                                               |___/                                           
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                              
                                       Programmer Operations:

                              1. view all Book() object variable names
                              2. view all Author() object variable names
                              3. view all User() object variable names
                              4. go back

                           -----------------select a number-------------------
   """)
                     if a == "1":
                        for x in objects.books:
                           print(x[0])
                     elif a == "2":
                        for y in objects.authors:
                           print(y[0])
                     elif a == "3":
                        for z in objects.users:
                           print(z[0])
                     elif a == "4":
                        break

               elif password == "exit":
                  break
               else:
                  print("ACCESS DENIED")
                  break
        

        if a == "6":
            break


objects.users_who_owe_money()
app()