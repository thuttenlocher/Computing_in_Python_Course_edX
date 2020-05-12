# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:43:21 2020

@author: Tyler H
"""

#Write a function called "steps" that should return a string 
#that, if printed, looks like this:
#
#111
#	222
#		333
#
#Note that the characters at the beginning of the second and
#third lines must be tabs, not spaces. There should be one
#tab on the second line and two on the third line.
#
#You may only declare ONE string in your function.
#
#Hint: Don't overthink this! We're literally just asking you
#to return one single string that just holds the above text.
#You don't have to build the string dynamically or anything.


#Write your function here!
def steps():
    one = "1"*3
    two = "2"*3
    three = "3"*3
    return one + "\n\t" + two + "\n\t\t" + three
    
    
#The line below will test your function.
print(steps())



