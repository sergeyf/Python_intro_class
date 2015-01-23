# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 21:12:17 2015

@author: S
"""

D = {}
D['dog'] = 'Fido'
D[1] = '1 dog'

S = {}
S['455-90-9876'] = ['Sergey','Feldman','No Middle Name']

D['another dictionary'] = S

import string

the_sentences = 'The work to do is left to do, and we must do it all.'
all_the_words = the_sentences.split()
countDict = {}
for word in all_the_words:
    # first, remove punctuation
    word_no_punct = "".join(l for l in word if l not in string.punctuation)
    word_no_caps = word_no_punct.lower()
    if word_no_caps not in countDict:
        countDict[word_no_caps] = 0
    #countDict[word_no_caps] = countDict[word_no_caps] + 1
    countDict[word_no_caps]  += 1
    









# list comprehensions
counter = 0
for i in range(10):
    counter += 1
    
counter = sum([i for i in range(10)])



    

    