#!/usr/bin/python

'''
Run the program with any scrambled word, and it will unscramble it for you.
    
Use this to unscramble the Word of the Day and get a free cookie at Pacific Cookie
Company in Berkeley on free cookie days!
'''

from itertools import *

def unscrambler(scrambled_word):
    i,j = 0,0
    word_list = []
    
    dict = open('EngWords.txt')
    dictionary = dict.read().split()
    some_word = list(scrambled_word)
    perm_list = list(permutations(some_word))
    
    while i < len(perm_list):
        perm_list[i] = ''.join(perm_list[i])
        if perm_list[i] in dictionary:
            word_list.append(perm_list[i])
        i += 1
    
    if not word_list:
        print('The word could not be unscrambled.')
    else:
        print('These are the possible unscrambled words:')
        while j < len(word_list):
            print(word_list[j])
            j += 1

unscrambler('htgli')
