"""Implement an efficient string matching algorithm.
That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
If the pattern is found, return the start index of its location. If not, return False"""
import re

s = input("enter a sting : ")
pattern = input("enter the patter you're looking for : ")
print("you're looking for {0} in {1}".format(pattern, s))
match = re.search(pattern, s)
if (match is not None):
    pass
else:
    print("does not exist")

print(match.start())
