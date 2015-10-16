#!/usr/bin/python

# This program takes in a word, scrambles it, and prints one such version

from random import *
from itertools import *

def scrambler(unscrambled_word):

	"""
	>>> scrambler('hello')
	Possible scrambled word:
	ohlle
	>>> scrambler('computer')
	Possible scrambled word:
	etmcrupo
	"""

	i = 0
	some_word = list(unscrambled_word)
	perm_list = list(permutations(some_word))
	while i < len(perm_list):
		perm_list[i] = ''.join(perm_list[i])
		i += 1
	print('Possible scrambled word:')

	#making sure program doesn't return the original word
	x = randint(0,(len(perm_list)-1))
	if perm_list[x] == unscrambled_word:
		x += 1
	print(perm_list[x])

scrambler('car')
