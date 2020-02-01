#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:53:53 2020

@author: vinod
"""
import random
from Book import Book,reserveBook,checkoutBook,returnBook
from Catalog import search
class User:
    def __init__(self,name,password,contact,email):
        self.name = name
        self.password = password
        self.contact = contact
        self.email = email
        
        
class member(User):
    
    def addmembertolibrary(self):
        Book.members = (self)
        
    def getLibraryCard(self):
        self.member_id = librarian.issueLibraryCard(self)
        return self.member_id

    def searchCatalog(self,searchBasis,book_info):
        if searchBasis == 'title':
            return search.search_by_title(self,book_info)
        elif searchBasis == 'author':
            return search.search_by_author(self,book_info)
        elif searchBasis == 'subject':
            return search.search_by_subject(self,book_info)
        elif searchBasis == 'publication_date':
            return search.search_by_publication_date(self,book_info)
        
        
        
    def reserve_Book(self,book,book_item):
        reserveBook.reservation_of_book(self,book,book_item)
        print("\n",Book.titles,Book.reserved_books,"\n")
        return None
        
    
        
               
    def checkout_book(self,book,book_item):
        return checkoutBook.checking_out_Book(self,book,book_item)
    
    def renew_book(self,book,book_item):
        None  
    
    def return_book(self,book,book_item):
        returnBook.return_book(self,book,book_item)
        print("\n",Book.return_books,"\n")
        return None    

    

    
    
        
        
        
    

class librarian(User):
    def __init__(self,name,password,contact,email):
        super().__init__(name,password,contact,email)
        
    def issueLibraryCard(self):

        member_id = random.randint(1,100)
        if member_id not in Book.member_id_dict.values() and self not in Book.member_id_dict.keys() :
            Book.member_id_dict.setdefault(self,member_id)
            return member_id
        
        else:
            print("Member id already issued")
            return None
        
        
    def addBookItem(self,book,book_item):
        if book in Book.titles.keys():
            Book.titles[book] = Book.titles[book] + book_item
            print("\n book as title {} with {} bookItem   is added \n".format(book,book_item))
            
        else:
            print("No such book title {} exist to add".format(book))
        return None   
    
    def removeBookItem(self,book,book_item):
        if book in Book.titles.keys():
            Book.titles[book] = Book.titles[book] - book_item
            print("\n In book title {}  the  {} book item removed from our library \n ".format(book,book_item))
            
        else:
            print("\n No such book title {} exist in our library inorder to remove \n ".format(book))
            
        return None
    
    def removeMember(self,name):
        for member in Book.members:       
            if name in Book.member.keys():  
                return Book.members.remove(member)
        
    
        
    
    
    
        
    

    
    