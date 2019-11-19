import json


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def serialize(root):
    serialized_tree_map = dict()
    serialized_tree_map['data'] = root.data
    if root.left is not None:
        serialized_tree_map['left'] = serialize(root.left)
    if root.right is not None:
        serialized_tree_map['right'] = serialize(root.right)
    return serialized_tree_map


def deserialise(s):
    root = Node(s['data'])
    if 'left' in s:
        root.left = deserialise(s['left'])
    if 'right' in s:
        root.right = deserialise(s['right'])
    return root


node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

serialized_a = serialize(node_a)
print(serialized_a)
