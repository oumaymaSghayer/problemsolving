"""This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. 
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2 + b^2 = c^2."""
l=[4,5,6,8,9,6,1,2,7]

def findpythagor(l):
    result =list(map(lambda x :  x**2, l))
    for e1 in l :
        l.remove(e1)
        for e2 in l:
            if e1**2 + e2**2 in result:
                return True
    return False

print(findpythagor(l))
