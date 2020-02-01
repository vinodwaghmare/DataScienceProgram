#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:53:30 2020

@author: vinod
"""

class Book:
    members = {}
    titles = {}
    authors = {}
    subjects = {}
    ISBN = {}
    publication_dates = {}
    reserved_books = {}
    available_books = {}
    return_books = {}
    member_id_dict = {}
    

    
    def __init__(self,title,subject,author,publication_date,ISBN,book_item = 0) :
        self.title = title
        self.subject = subject
        self.author = author
        self.publication_date = publication_date
        self.ISBN = ISBN
        self.book_item = book_item 
        Book.titles.setdefault(title ,book_item )
        Book.authors.setdefault(author,title  )
        Book.publication_dates.setdefault(publication_date ,title )
        Book.ISBN.setdefault( ISBN ,title )
        Book.subjects.setdefault(subject ,title)
        
        
        
        
class reserveBook:
    def reservation_of_book(self,book,book_item):
        if book in Book.titles.keys() and Book.titles[book] >= 0  and book_item < Book.titles[book]:
            Book.titles[book] -= book_item
            Book.reserved_books.setdefault(book,book_item)
        else:
            print("No such book title {} available in the library inorder to reserve".format(book))
        
class checkoutBook:
    def checking_out_Book(self,book,book_item):   
        if book in Book.reserved_books.keys() and book_item < Book.titles[book]:  
            Book.reserved_books[book] = Book.reserved_books[book] - book_item    
            print("\n Borrowed book {} from library and no. of copies {} \n".format(book,book_item))
            
        else:
            print( " \n title {} copies are not available \n".format(book))
  

class renewBook:
    def __init__(self,book,days):
        pass
        
      
class returnBook:
    def return_book(self,book,book_item):
        if book in Book.titles.keys():
            Book.titles[book] += book_item
            print("book title {} returned ".format(book))
            Book.return_books.setdefault(book,book_item)
        else:
            print("No such book title {} is Borrowed inorder to return".format(book))

        
        
#class checkfine:
#    def __init__(self,member_id,date_of_issue,due_date):
#        pass 

            
        