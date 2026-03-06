class Book:
 def __init__(self,book_id,title,author,price,copies_available):
  self.book_id=book_id
  self.title=title
  self.author=author
  self.price=price
  self.copies_available=copies_available

 def display_book(self):
  print("Book ID:",self.book_id)
  print("Title:",self.title)
  print("Author:",self.author)
  print("Price:",self.price)
  print("Copies Available:",self.copies_available)

 def issue_book(self,quantity):
  if quantity<=self.copies_available:
   self.copies_available=self.copies_available-quantity
   print("Book issued")
  else:
   print("Not enough copies available")

 def add_copies(self,quantity):
  self.copies_available=self.copies_available+quantity

 def book_value(self):
  return self.price*self.copies_available


library=[]

b1=Book(101,"Python Programming","Mark Lutz",750,5)
b2=Book(102,"Data Structures and Algorithms","Thomas H. Cormen",1200,3)
b3=Book(103,"Machine Learning Basics","Andrew Ng",950,4)

library.append(b1)
library.append(b2)
library.append(b3)

print("Library Books")

for book in library:
 book.display_book()
 print()

print("Issue 2 copies of Python Programming")
library[0].issue_book(2)

print("Add 3 copies to Machine Learning Basics")
library[2].add_copies(3)

print("\nTotal value of books in library")
total=0

for book in library:
 total=total+book.book_value()

print("Total Value:",total)