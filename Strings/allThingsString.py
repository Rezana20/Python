# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:17:45 2017

@author: rezana.ganie
"""

testMe = 'rgdshshsfhs'

"""Get the legth of the string"""
print(len(testMe))

""" Change case of the string"""
print(testMe.lower())
print(testMe.upper())

"""Append more to the string """
print(testMe + ' here is more')

"""Get a letter in a position """
print(testMe[5]) 

""" Parse a number as a string """
myID = 326589785
print(str(myID))

""" Parse a string as a number """
myAge = '15'
yourAge = '12'

print(int(myAge)+int(yourAge))

""" Formating """
formatMe = 'this\t\n and that'
print(formatMe)

""" Replace a string with another"""
print formatMe.replace('a','p')

""" Create array with each word"""
print formatMe.split()