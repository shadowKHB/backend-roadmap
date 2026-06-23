books = []
borrowed_books = set()
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography")


while True:
    print("===== MAIN MENU LOOP =====")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all books")
    print("6. View available genres")
    print("7. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        title = input("Enter a title to add: ")
        if title in books :
            print("This book already exists")
        else:
            books.append(title)  
            print("Book added !")  
    elif choice == 2:
        title = input("Enter a title to remove: ")
        if title in borrowed_books:
            print("Can't remove,this book is currently borrowed")
        elif title in books:
            books.remove(title)
            print(f"Book '{title}' removed ")
        else:
            print("Book not found")        
    elif choice == 3:
        title = input("Enter a title to borrow: ")
        if title in borrowed_books:
            print("Already borrowed")
        elif title in books:
            borrowed_books.add(title)
            print("Book borrowed !")
        else:
            print("Book not found")
    elif choice == 4:
        title = input("Enter a title to return it: ")
        if title in borrowed_books:
            borrowed_books.remove(title)
            print(f"Book '{title}' returned")
        elif title in books:
            print("This book wasn't borrowed")
        else:
            print("Book not found")    
    elif choice == 5:
        if len(books) == 0:
            print("The library is empty.")
        else:    
            for title in books:
                if title in borrowed_books:
                    print(f"{title} [BORROWED] , ",end=' ')            
                else : 
                    print(f"{title} , ", end=' ')
            print()        
    elif choice == 6:
        for genre in genres:
            print(genre, end=' , ')
        print()    
    elif choice == 7:
        print("GoodBye !")
        break
    else:
        print("Choice INVALID !")                       