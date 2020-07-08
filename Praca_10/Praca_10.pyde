import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
     
def setup():
    size(220,100)
    global library, Kasia, Gruza
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Lalka"]
    library = Library(books) 
    Kasia = Customer()
    Gruza = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Kasia.requestBook("Naocznosc"))
            library.lendBook(Gruza.requestBook("Lalka")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Kasia.returnBook())
            library.addBook(Gruza.returnBook())
            
            
class requestten(unittest.TestCase):

    def test_BarteG(self): # nazwy testów nie mogą się powtarzać i powinny zaczynać się od 'test'
        Gruza = Customer() # testy powinny być od siebie niezależne, a więc obiekty definiowane w nich bezpośrednio
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books) # self wskazuje na klasę w której jesteśmy, teraz jesteśmy w kalsie testów, więc używanie self jako wskazania napole wewnętrzne obecnej klasy przy klasach customer i library jest błędne
        library.lendBook(Gruza.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], library.availableBooks)
        self.assertEqual(Gruza.book, "Harry Potter")
        self.assertTrue(Gruza.haveBook)

    def test_Bartek(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Lalka"]
        library = Library(books)
        library.addBook("Marsjanin")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Lalka", "Marsjanin"], library.availableBooks)
        
if __name__ == '__main__':
    unittest.main()
    
# 1,5pkt
