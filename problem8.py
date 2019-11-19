"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)
Implement car and cdr."""


def cons(a, b):
    return lambda f: f(a, b)


def car(f):
    def z(x, y):
        return x
    return(f(z))


def cdr(f):
    def z(x, y):
        return y
    return f(z)


assert car(cons(1, 2)) == 1
print(cons(4, 3))
