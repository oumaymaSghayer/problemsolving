"""Given an array of integers, return a new array such that each element at index i of the new 
array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
WITHOUT DIVISION"""


def newprod(array):
    rightprod = []
    product = 1
    for e in array:
        product = product*e
        rightprod.append(product)
    product = 1
    leftprod = []
    for e in array[::-1]:
        product = product*e
        leftprod.append(product)
    leftprod = leftprod[::-1]
    output = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = leftprod[i+1]
        elif i == len(array) - 1:
            num = rightprod[i-1]
        else:
            num = rightprod[i-1]*leftprod[i+1]
        output.append(num)

    return output


print(newprod([1, 2, 3, 4, 5]))
