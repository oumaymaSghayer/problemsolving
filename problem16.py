"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A regular number in mathematics is defined as one which evenly divides some power of 60. 
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.
Given an integer N, write a program that returns, in order, the first N regular numbers.

"""
def devidedbytwo(N):
    return N%2==0
def devidedbythree(N):
    return N%3==0
def devidedbyfive(N):
    return N%5==0
def regular(N):
    i=1
    j=1
    l=[]
    
    while i<N:
        if 60 % i == 0:
            l.append(i)
        i+=1
    return l
print(regular(40))
