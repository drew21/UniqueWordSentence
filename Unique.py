We are given two sentences A and B. (A sentence is a string of space separated words. Each word consists only of lowercase letters.) 
A word is unique if it appears exactly once in one of the sentences, 
and does not appear in the other sentence. 
Return a list of all unique words. You may return the list in any order.
 Example 1: Input: A = "this apple is sweet", B = "this apple 
is sour" Output: ["sweet","sour"] Example 2: Input: A = "apple apple", B = "banana" Output: ["banana"]

brian.m.sipe@boeing.com

# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online
from collections import Counter

print("Try programiz.pro")
sentence_1 = input()
sentence_2 = input()

for word in sentence_1.split():
    a = sentence_1.split()
    dict = Counter(a)
    for key in a: 
        if dict[key]<=1: 
            if word not in sentence_2.split():
                print(word) 
                break

for word in sentence_2.split():
    a = sentence_2.split()
    dict = Counter(a)
    for key in a: 
        if dict[key]<=1:
            if word not in sentence_1.split():
                print(word)
                break
