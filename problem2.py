"""
Given a list of numbers, return whether any two sums to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def check(l, k):

    for e in l:
        if (k - e) in l:
            return True
    return False


listsize = int(input('enter list size : '))
l = []
for i in range(listsize):
    n = int(input("enter an integer : "))
    l.append(n)

k = int(input("enter k : "))
print(check(l, k))
