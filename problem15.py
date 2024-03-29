"""This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. 
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. 
In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class."""
d={
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}
m=[
    [1,2,3,4],[7,8,6]
]
def find(n , m):
    for l in m :
        if n in l :
            return (m.index(l) ,l.index(n))
    return (-1,-1)

print(find(9,m))
def fetch_friends(d):
    f=dict()
    s=list()
    for key,values in d:
        if find(key,s) ==(-1,-1):
            



