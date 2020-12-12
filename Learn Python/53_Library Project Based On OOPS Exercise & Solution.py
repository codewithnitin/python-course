class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_data = {}

    def display_book(self):
        return(f"{self.library_name} have following books : {self.list_of_books}")

    def add_book(self):
        Book_name = input("Enter the book name which you wish to donate")
        self.list_of_books.append(Book_name)
        return("Successfully added the donated book")

    def lend_book(self):
        book = input("Enter the book name which you wish to lend")
        customer = input("Enter the name of the customer")
        if book in self.list_of_books:
            if book not in self.lend_data.keys():
                self.lend_data[book] = customer
                return(f"You can lend this book {book}")
            else:
                return(f"Sorry this book is owned by {self.lend_data[book]}")
        else:
            return(f"Sorry this book is not available in {self.library_name}")

    def return_book(self):
        book = input("Enter the book name which you wish to return")
        customer = input("Enter the name of the customer")
        if book in self.lend_data.keys() and customer in self.lend_data.values():
            del[self.lend_data[book]]
            return("Successfully returned the book and cleared the entry from the dictionary")
        else:
            return("Sorry you have not lent this book")


Nitin = Library(["C++","Python","Java"], "Nitin_Library")
while(True):
    print("Welcome to the Library of Nitin")
    n = int(input("Type option :\n1 for Display \n2 for Add \n3 for Lend \n4 for Return\n"))
    if n == 1:
        print(Nitin.display_book())
    elif n ==2:
        print(Nitin.add_book())
    elif n == 3:
        print(Nitin.lend_book())
    elif n == 4:
        print(Nitin.return_book())
    else:
        print("Please enter the correct input")




