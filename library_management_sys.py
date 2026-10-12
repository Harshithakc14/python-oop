"""
----------------Library Management System--------------------------
library--Manage books,users,borrowing and returning
book==Books id,title,author,availability
User==user id,name,borrowed books
loan/borrow record==connects a book and a borrower ,stores borrow date,due date and return date and late penalty

-----------what each class is responsible for----------------
book--check whether the book is available
user--track the books borrowed by the user
loan--calculate due date and late return penalty
library--Add books/users,isue books,accept returns,display available books

"""
from datetime import date,timedelta
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=True
    def display_details(self):
        print("Book ID:", self.book_id)
        print("Title: ",self.title)
        print("Author:", self.author)
        print("Available:", self.is_available)
class User:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.borrowed_books=[]
class Loan:
    def __init__(self,book,user):
        self.book=book
        self.user=user
        self.borrow_date=date.today()
        self.due_date=self.borrow_date+timedelta(days=14)
        self.return_date=None
        self.penalty=0
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
        self.loans=[]
    def add_book(self,book):
        for existing_book in self.books:
            if existing_book.book_id==book.book_id:
                print("Book ID already exists!")
                return

        self.books.append(book)
        print("Book added suceessfully!")

    def register_user(self,user):
        for existing_user in self.users:
            if existing_user.user_id==user.user_id:
                print("User ID already exists!")
                return
        self.users.append(user)
        print("User registered successfully!")
    def borrow_book(self,user_id,book_id):
        user=None
        book=None
        for existing_user in self.users:
            if existing_user.user_id==user_id:
                user=existing_user
                break
        for existing_book in self.books:
            if existing_book.book_id==book_id:
                book=existing_book
                break
        if user is None:
            print("User not found!")
            return
        if book is None:
            print("Book not found!")
            return
        if not book.is_available:
            print("Book is not available")
            return
        loan=Loan(book,user)
        self.loans.append(loan)
        user.borrowed_books.append(book)
        book.is_available=False
        print("Book borrowed successfully!")
        print("Due date:", loan.due_date)

    def return_book(self, user_id, book_id):
        for loan in self.loans:
            if (loan.user.user_id == user_id
                    and loan.book.book_id == book_id
                    and loan.return_date is None):

                loan.return_date = date.today()

                late_days = (loan.return_date - loan.due_date).days

                if late_days > 0:
                    loan.penalty = late_days * 5

                loan.book.is_available = True
                loan.user.borrowed_books.remove(loan.book)

                print("Book returned successfully!")
                print("Late days:", max(0, late_days))
                print("Penalty: ₹", loan.penalty)
                return

        print("No active loan found for this user and book!")

    def view_available_books(self):
        found = False

        for book in self.books:
            if book.is_available:
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("--------------------")
                found = True

        if not found:
            print("No books available!")
def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Available Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")

            user = User(user_id, name)
            library.register_user(user)

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))

            library.borrow_book(user_id, book_id)

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))

            library.return_book(user_id, book_id)

        elif choice == "5":
            library.view_available_books()

        elif choice == "6":
            print("Thank you for using the library!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()



