"""
NOT DONE
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and 
the previous node. 
Implement an XOR linked list; 
    it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes 
and memory addresses.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return "data = {0}  : ({1},{2})".format(self.data, self.prev, self.next)


class XorLinkedList(Node):
    def __init__(self, node):
        self.data = node.data
        #self.both = node.next | node.prev

    def __str__(self):
        return " data = {0} ".format(self.data)


node1 = Node("a")
node2 = Node("b")
node3 = XorLinkedList("c")
node1.next = node2

print(str(node1))
print(str(node3))
print()
