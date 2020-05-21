# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:17:41 2020

@author: Tyler H
"""

#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(filename):
    file = open(filename, "r")
    x = file.read()
    c = 'coffee'
    y = c in x
    file.close()
    return y


#You can test your function with the provided files named 
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))




