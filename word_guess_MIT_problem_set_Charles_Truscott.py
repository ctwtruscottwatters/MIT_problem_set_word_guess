# -*- coding: utf-8 -*-
import random
import sys
"""
runfile('C:/Users/user/.spyder-py3/ifnotin.py', wdir='C:/Users/user/.spyder-py3')

Pick a letter: p
Correct! p is in the word.
Correct answers:	 ['p']

__p_____

Pick a letter: e
Incorrect, e is not in the word
Correct answers:	 ['p']

__p_____

Pick a letter: a
Correct! a is in the word.
Correct answers:	 ['a', 'p']

_ap_____

Pick a letter: p
Incorrect, p is not in the word
Correct answers:	 ['a', 'p']

_ap_____

Pick a letter: c
Correct! c is in the word.
Correct answers:	 ['c', 'a', 'p', 'c']

cap__c__

Pick a letter: s
Correct! s is in the word.
Correct answers:	 ['c', 'a', 'p', 's', 'c']

caps_c__

Pick a letter: i
Correct! i is in the word.
Correct answers:	 ['c', 'a', 'p', 's', 'i', 'c']

capsic__

Pick a letter: u
Correct! u is in the word.
Correct answers:	 ['c', 'a', 'p', 's', 'i', 'c', 'u']

capsicu_

Pick a letter: m
Correct! m is in the word.
Correct answers:	 ['c', 'a', 'p', 's', 'i', 'c', 'u', 'm']

capsicum
The answer was:	 capsicum
End of Game
I love MIT. Charles Truscott
"""
def main():
    words = ["apple", "pear", "banana", "peach", "fruit salad", "potato", "pumpkin", "celery", "leek", "onion", "lettuce", "carrot", "tomato", "sweet potato", "capsicum"]
    
    
    y = words[random.randint(0, len(words) - 1)]
    p, q, r, s = 0, 0, 0, 0
    d = {}
    
    for n in y:
            d.get(s)
            d[p] = n
            p += 1
            
    copy_dict = d
    
    
    fin = False
    choices = []
    not_chosen = []
    correct_answers = []
    wrong_answers = []
    not_found_letters = []
    z = y
    z_copy = z
    not_found = True
    for n in y:
        not_chosen.append(n)
    while(not fin):
        found = False
        choice = input('Pick a letter: ')
        for n in y:
                if choice == n:
                    correct_answers.append(choice)
                    for x in not_chosen:
                        if x == choice:
                            not_chosen.remove(choice)
                            found = True
    
        if found == True:
            print("Correct! {} is in the word.".format(choice))
        elif found == False:
            print("Incorrect, {} is not in the word".format(choice))
        found = False
    
        temp = []
        for q in z:
            for r in correct_answers:
                if q == r:
                    temp.append(r)
                    break
        print('Correct answers:\t', temp, end='\n\n')
        temporary_word = z
        for letter in not_chosen:
            if temporary_word.rfind(letter):
                 temporary_word = temporary_word.replace(letter, "_")
#            for letter in correct_answers:
#               temporary_word.rindex(0)
        print(temporary_word)
        if len(not_chosen) == 0:
            print('The answer was:\t', y)
            print("End of Game")
            print('I love MIT. Charles Truscott')
            sys.exit()
        # print(not_chosen)
        
if __name__ == "__main__": main()
    
                    
             
        
                
    
                    
                
