"""This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle."""


class Node:
    def __init__(self, value):
        self.value = value
        self.adj_nodes = set()

    def __repr__(self):
        return self.value

    def __str__(self):
        return "value : {0} ; adj_nodes : {1} ".format(self.value, self.adj_nodes)

    def is_adj(self,node):
        if node in self.adj_nodes:
            return True
        return False
    

class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.unseen_nodes=None 
    def has_cycle_helper(self,node,path=list()):
        if node in self.unseen_nodes:
            self.unseen_nodes.remove(node)
        for adj_node in node.adj_nodes:
            if adj_node in path and adj_node != path[-1]:
                return True
            if self.unseen_nodes:
                return self.has_cycle_helper(adj_node,path + [node])
        return False
    def has_cycle(self):
        start_node = next(iter(self.nodes))
        self.unseen_nodes=self.nodes.copy()
        return self.has_cycle_helper(start_node)




   

    
        


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
a.adj_nodes = (b, c)
b.adj_nodes = (d, e, a)
c.adj_nodes = (a, f)
d.adj_nodes = (b, e)
e.adj_nodes = (b, d)
print(str(a))
print(str(b))
print(str(c))
print(str(d))
print(str(e))
print(str(f))
print(a.is_adj(g))

