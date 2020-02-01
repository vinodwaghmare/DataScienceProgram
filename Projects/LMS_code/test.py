#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:54:03 2020

@author: vinod
"""

from Book import Book
#from Catalog import search
from System import  librarian, member

book1 = Book('Nineteen Eighty-Four','Novel','George Orwell','1949','324244',2)
book2 = Book('To Kill a Mockingbird','Novel','Harper Lee','1960','323244',4)
book3 = Book('Pride and Prejudice','Novel of manners','Jane Austin','1982','325244',5)


#print(book1.__dict__)
#print(book2.__dict__)
#print(book3.__dict__)


# which tasks the Librarian can perform


lib = librarian('Ron','4321','9140378291','abc@gmail.com',)
lib.addBookItem('Nineteen Eighty-Four',5)

print(Book.titles,"\n")



lib.removeBookItem('Pride and Prejudice',2)

print(Book.titles)

lib.removeBookItem('The Great Gatsby ',2)

print(Book.titles,"\n")


member1 = member('Ashish','332','9178473341','ashish@gmail.com')
print(member1.__dict__,"\n")

member1.addmembertolibrary()
print(Book.members)

member1.getLibraryCard()
print(member1.__dict__)
print(Book.member_id_dict)

# Search By title
member1.searchCatalog('title','Nineteen Eighty-Four') # vaild Input
member1.searchCatalog('title','Invisible man') # Invalid Input

# Search by author
member1.searchCatalog('author','Harper Lee') # vaild Input
member1.searchCatalog('author','Ralph Ellison') # Invalid Input

# Search by publication date
member1.searchCatalog('publication_date','1982') # vaild Input
member1.searchCatalog('publication_date','1919') # Invalid Input

member1.reserve_Book('Nineteen Eighty-Four',1) # Valid Input
member1.reserve_Book('Wings of fire',2) # Invalid Input

member1.checkout_book("Nineteen Eighty-Four",1) #Valid Input
member1.checkout_book('Wings of fire',2) # Invalid Input


member1.return_book('Nineteen Eighty-Four',1) # Valid Input
member1.return_book('Half Boyfriend',1) #Invalid Input



#print(member1.__dict__)
#member1.getLibraryCard()
#print(member1.__dict__)




#b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
#catalog.addBookItem(b, '123hg','H1B2')
#catalog.addBookItem(b, '124hg','H1B4')
#catalog.addBookItem(b, '125hg','H1B5')
#
#b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
#catalog.addBookItem(b, '463hg','K1B2')
#
#catalog.displayAllBooks()
#
#m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
#
#librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
#print (m1)
#print (librarian)
#
#b = catalog.searchByName('Shoe Dog')
#print (b)
#
#
#catalog.removeBookItem('Shoe Dog','124hg')
#catalog.displayAllBooks()
#m1.issueBook