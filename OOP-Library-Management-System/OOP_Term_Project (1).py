#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os  # Importing the os module for file handling
import csv  # Importing the csv module to handle CSV files
from datetime import datetime, timedelta  # Importing datetime and timedelta to handle dates and calculate overdue days

# UserAccount Class to manage user data and borrowed books
class UserAccount:
    def __init__(self, user_id, name):  # Constructor to initialize user ID and name
        self.user_id = user_id  # Setting the user ID
        self.name = name  # Setting the user name
        self.borrowed_books = []  # List to store borrowed books
    
    def borrow_book(self, book_title):  # Method to add a book to the borrowed list
        self.borrowed_books.append(book_title)  # Adding the book title to the list
    
    def return_book(self, book_title):  # Method to remove a book from the borrowed list
        if book_title in self.borrowed_books:  # Check if the book is in the borrowed list
            self.borrowed_books.remove(book_title)  # Remove the book from the list
        else:
            raise ValueError("Book not found in borrowed list.")  # Raise an error if the book is not found

# Librarian class inherits from UserAccount and manages book additions and removals
class Librarian(UserAccount):
    def __init__(self, user_id, name):  # Constructor to iitialize librarian's user ID and name
        super().__init__(user_id, name)  # Call the parent cnonstructor
    
    def add_book(self, book_manager, book_title):  # Method to add a new book to the system
        book_manager.books[book_title] = 'available'  # Add the book with status 'available'
        book_manager.save_books()  # Save the updated books list to the file
    
    def remove_book(self, book_manager, book_title):  # Method to remove a book from the system
        if book_title in book_manager.books:  # Check if the book exists in the system
            del book_manager.books[book_title]  # Delete the book from the books list
            book_manager.save_books()  # Save the updated books list to the file
        else:
            raise ValueError("Book not found in the system.")  # Raise an error if the book is not found

# ManageBookLending class handles book lending and file operations
class ManageBookLending:
    def __init__(self, file_path='books.csv'):  # Constructor to initialize file path for books
        self.file_path = file_path  # Set the file path to load and save books
        self.books = self.load_books()  # Load books from the file into a dictionary
    
    def load_books(self):  # Method to load books from the CSV file
        books = {}  # Initialize an empty dictionary to store books
        if os.path.exists(self.file_path):  # Check if the file exists
            with open(self.file_path, mode='r') as file:  # Open the file in read mode
                reader = csv.reader(file)  # Create a CSV reader object
                for row in reader:  # Loop through each row in the file
                    books[row[0]] = row[1]  # Add the book title and status to the dictionary
        return books  # Return the dictionary of books
    
    def save_books(self):  # Method to save the books dictionary to the CSV file
        with open(self.file_path, mode='w', newline='') as file:  # Open the file in write mode
            writer = csv.writer(file)  # Create a CSV writer object
            for title, status in self.books.items():  # Loop through each book in the dictionary
                writer.writerow([title, status])  # Write the book title and status to the file
    
    def lend_book(self, user, book_title):  # Method to lend a book to a user
        if book_title in self.books and self.books[book_title] == 'available':  # Check if the book is available
            self.books[book_title] = 'borrowed'  # Change the status of the book to 'borrowed'
            user.borrow_book(book_title)  # Add the book to the user's borrowed list
            self.save_books()  # Save the updated books list to the file
        else:
            raise ValueError("Book is not available.")  # Raise an error if the book is not available

# ReturnsAndOverduePenalties class handles book returns and calculates penalties
class ReturnsAndOverduePenalties:
    def __init__(self):  # Constructor to initialize return records
        self.return_records = {}  # Dictionary to store return records
    
    def return_book(self, user, book_title, borrow_date):  # Method to handle book returns and calculate penalties
        try:
            user.return_book(book_title)  # Try to return the book
            return_date = datetime.now()  # Get the current date as the return date
            self.return_records[user.user_id] = return_date  # Store the return date in the records
            overdue_penalty = self.calculate_penalty(borrow_date)  # Calculate the overdue penalty
            if overdue_penalty > 0:  # Check if there is any overdue penalty
                print(f"Overdue penalty for '{book_title}': ${overdue_penalty}")  # Display the overdue penalty
            else:
                print(f"Book '{book_title}' returned successfully.")  # Display success message
        except ValueError as e:
            print(f"Error: {e}")  # Show error if book not found in borrowed list
    
    def calculate_penalty(self, borrow_date):  # Method to calculate overdue penalty
        due_date = borrow_date + timedelta(days=14)  # Books are due after 14 days
        overdue_days = (datetime.now() - due_date).days  # Calculate the number of overdue days
        penalty_rate = 1  # Define the penalty rate per overdue day
        return max(0, overdue_days * penalty_rate)  # Return the penalty amount (0 if no penalty)

# Main function to interact with the user through the console
def main():
    # Initialize user, librarian, and book manager
    user = UserAccount("U001", "Alice")  # Create a user account for Alice
    librarian = Librarian("L001", "Admin")  # Create a librarian account
    book_manager = ManageBookLending()  # Create a book manager object to manage books
    return_manager = ReturnsAndOverduePenalties()  # Create a return manager object to handle returns and penalties

    while True:  # Start an infinite loop to display the menu
        # Display menu for user interaction
        print("\n****Library Management System****")  # Display system title
        print("1. View Available Books")  # Option to view available books
        print("2. Borrow Book")  # Option to borrow a book
        print("3. Return Book")  # Option to return a book
        print("4. View Borrowed Books")  # Option to view borrowed books
        print("5. Add Book (Librarian)")  # Option for librarian to add a book
        print("6. Remove Book (Librarian)")  # Option for librarian to remove a book
        print("7. Exit")  # Option to exit the program
        
        choice = input("Enter your choice: ")  # Prompt user to enter their choice
        
        if choice == '1':  # If user chooses to view available books
            # View available books
            books = "\n".join([f"{title} ({status})" for title, status in book_manager.books.items()])  # Create a string of available books
            print(f"\nAvailable Books:\n{books if books else 'No books available'}")  # Display available books or a message if none
    
        elif choice == '2':  # If user chooses to borrow a book
            # Borrow a book
            book_title = input("Enter the book title to borrow: ")  # Prompt user for book title
            try:
                book_manager.lend_book(user, book_title)  # Attempt to lend the book
                print(f"You borrowed '{book_title}'")  # Display success message
            except ValueError as e:
                print(f"Error: {e}")  # Display error message if book is not available
        
        elif choice == '3':  # If user chooses to return a book
            # Return a book
            book_title = input("Enter the book title to return: ")  # Prompt user for book title
            borrow_date = datetime.now()  # Set the borrow date to the current date for simplicity
            return_manager.return_book(user, book_title, borrow_date)  # Call return method
        
        elif choice == '4':  # If user chooses to view borrowed books
            # View borrowed books
            books = "\n".join(user.borrowed_books)  # Create a string of borrowed books
            print(f"\nBorrowed Books:\n{books if books else 'No books borrowed'}")  # Display borrowed books or a message if none
        
        elif choice == '5':  # If librarian chooses to add a book
            # Add a book (Librarian)
            book_title = input("Enter the book title to add: ")  # Prompt librarian for book title
            librarian.add_book(book_manager, book_title)  # Call the method to add the book
            print(f"Book '{book_title}' added")  # Display success message
        
        elif choice == '6':  # If librarian chooses to remove a book
            # Remove a book (Librarian)
            book_title = input("Enter the book title to remove: ")  # Prompt librarian for book title
            try:
                librarian.remove_book(book_manager, book_title)  # Attempt to remove the book
                print(f"Book '{book_title}' removed")  # Display success message
            except ValueError as e:
                print(f"Error: {e}")  # Display error message if book is not found
        
        elif choice == '7':  # If user chooses to exit
            # Exit the program
            print("Exiting the Library Management System.")  # Display exit message
            break  # Break the loop and exit the program
        
        else:  # If the user enters an invalid option
            print("Invalid choice. Please try again.")  # Display an error message

# Run the main function
if __name__ == "__main__":  # If this script is run directly
    main()  # Call the main function to start the program


# In[ ]:





# In[ ]:




