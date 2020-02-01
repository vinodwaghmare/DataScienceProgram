#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:53:40 2020

@author: vinod
"""
from Book import Book
class search:
    def search_by_title(self,title):
        if title in Book.titles:
            print( "\n title {} and Book item's are {} \n".format(title,Book.titles[title]))
        else:
            print("\n No such book title {} exist in the library \n ".format(title))
        return None
    
    def search_by_author(self,author):
        if author in Book.authors:
            print( " \n author {} and title {} and book items are {} \n".format(author,Book.authors[author],Book.titles[Book.authors[author]]))
        else:
            print("\n No such author {} book exist in the library \n ".format(author))
        return None
    
#    def search_by_subject(self,subject):
#        if subject in Book.subjects:
#            print( "\n subject {} and title  {} book items are {} \n".format(subject,Book.subjects[subject],Book.titles[Book.subjects[subject]]))
#        else:
#            print("\n No such subject  {} book exist in the library \n ".format(subject))
#        return None
    
    def search_by_publication_date(self,publication_date):
        if publication_date in Book.publication_dates:
            print( "\n {} publication date of the book title  {} with book items {} \n ".format(publication_date,Book.publication_dates[publication_date],Book.titles[Book.publication_dates[publication_date]] ))
        else:
            print("\n No such publication date {} book exist in the library \n".format(publication_date))
        return None
    
        
        
    
