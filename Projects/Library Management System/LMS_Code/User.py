#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:53:53 2020

@author: vinod
"""
import random
from Book import Book,reserveBook,checkoutBook
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
        return Book.reserved_books
        
        
               
    def checkout_book(self,book,book_item):
        return checkoutBook.checking_out_Book(self,book,book_item)
    
    def renew_book(self,book,book_item):
        None  
    
    def removeBook(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookitem(isbn)
        book.removeBookItem(book_item)
    
        
        
        
    

class librarian(User):
    def __init__(self,name,password,contact,email):
        super().__init__(name,password,contact,email)
        
    def issueLibraryCard(self):
        member_id = random.randint(1,100)
        return member_id
        
        
        
    def addBook(self,book,book_item):
        if book in Book.titles.keys():
            Book.titles[book] = Book.titles[book] + book_item
            
        else:
            Book.titles[book] = book_item
        return Book.titles[book]    
    
    def removeBook(self,book,book_item):
        if book in Book.titles.keys():
            Book.titles[book] = Book.titles[book] - book_item
            
        return Book.titles[book]
    
    def removeMember(self,name):
        for member in Book.members:       
            if name in Book.member.keys():  
                return Book.members.remove(member)
        
    
        
    
    
    
        
    

    
    