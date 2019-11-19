"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""
import re
qstring = input("enter you query sting : ")

l = ["dog", "deer", "deal"]
for e in l:
    match = re.search(qstring, e)
    if(match is not None):
        if(match.start() == 0):
            print(e)
