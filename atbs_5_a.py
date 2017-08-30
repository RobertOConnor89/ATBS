# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 17:36:37 2016

@author: Jeff and Ashley
"""
import pprint
done = False

inventory = {}

while done == False:
    print 'Enter a type of item and amount to add to your inventory.'
    item = raw_input('>')
    print 'Please enter the amount'
    amount = raw_input('>')
    inventory[item] = amount
    print 'Are you done?'
    dec = raw_input('>')
    if dec == 'yes':
        done = True
    if done == True:
        print 'Would you like to print the dictionary\'s contents?'
        dec = raw_input('>')
        if dec=='no':
            done = True
            break
        else:
            pprint.pprint(inventory)

raw_input()
