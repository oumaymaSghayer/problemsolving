"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def missingpositive(arr):
    minimum = min(arr)
    while (minimum <= 0):
        arr.remove(minimum)
        minimum = min(arr)
    if (minimum != 1):
        return 1
    for i in range(minimum, max(arr)):
        if i not in arr:
            return i
    return max(arr) + 1


print(min([-1, 1, 8, 6]))
print(missingpositive([-1, 0, 1, 2, 3]))
