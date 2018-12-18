#what follows is a class definition for a Node in a tree data-structure
#try to figure this one out yourself ;)
from __future__ import print_function

pwnl = lambda x: print(x, end=',') #print with comma instead of newline

class TreeNode(object):
    def __init__(self, payload=None, parent=None):
        if type(parent) != TreeNode and parent != None:
            raise TypeError
        self.parent = parent
        self.payload = payload
        self.children = []

    def __str__(self):
        return str(self.payload)

    def __iter__(self):
        return self.children.__iter__()

    def __len__(self):
        total = len(self.children)
        for child in self.children:
            total += len(child)
        return total

    def is_root(self):
        return self.parent == None

    def add_child(self, tn):
        if type(tn) == TreeNode:
            tn.parent = self
            self.children.append(tn)

    def remove_child_i(self, i):
        if i < len(self.children):
            del self.children[i]
        elif len(self.children): del self.children[-1]

    def remove_all_children(self):
        self.children = []

    #traversal algorithms...
    #more on this topic @ https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)
    def pre_order_traverse(self, func=pwnl):
        if func == None: func = print
        func(self.payload)
        for child in self.children:
            child.pre_order_traverse(func)

    def in_order_traverse(self, func=pwnl):
        if len(self.children) == 0:
            func(self.payload)
            return
        elif len(self.children) == 1:
            self.children[0].in_order_traverse(func)
            func(self.payload)
            return
        count = 0
        mid = len(self.children)/2
        for child in self.children:
            if count == mid: func(self.payload)
            child.in_order_traverse(func)
            count += 1

    def post_order_traverse(self, func=pwnl):
        for child in self.children:
            child.post_order_traverse(func)
        func(self.payload)

    def find(self, payload):
        result = []
        if self.payload == payload: result.append(self)
        else:
            for child in self.children:
                res = child.find(payload)
                if len(res) > 0: result += res
        return result

class Tree(object):
    def __init__(self, root=None):
        self.root = root
        if type(root) != TreeNode and root != None:
            raise TypeError
        if root != None: self.root.parent = None
        else: self.root = TreeNode()

    def __str__(self):
        return "Root of the tree = %s" % self.root

    def __len__(self):
        return len(self.root)

    def __iter__(self):
        return self.root.children.__iter__()

    def is_empty(self):
        return self.root.payload == None and len(self.root.children) == 0

    def add_child(self, tn):
        self.root.add_child(tn)

    def remove_child_i(self, i):
        self.root.remove_child_i(i)

    def remove_all_children(self):
        self.root.remove_all_children()

    def pre_order_traverse(self, func=pwnl):
        self.root.pre_order_traverse(func)
        if func == pwnl: print("") #to force a newline after everything's printed

    def in_order_traverse(self, func=pwnl):
        self.root.in_order_traverse(func)
        if func == pwnl: print("") #to force a newline after everything's printed

    def post_order_traverse(self, func=pwnl):
        self.root.post_order_traverse(func)
        if func == pwnl: print("") #to force a newline after everything's printed

    def find(self, payload):
        return self.root.find(payload)

#perhaps mess around some more...
if __name__ == "__main__":
    #create a tree that goes as follows:
    '''
              - None -
            /  / | \   \
          /   /  |  \   \
         0   1   2   3   4 ---
       / |  / \  |  / \  | \  \
      a  b c  d  a b  c  d  a  b
    '''
    tree = Tree()
    for i in range(5):
        tn = TreeNode(i)
        tree.add_child(tn)
    lengths = [2,2,1,2,3]
    lindex = 0
    letters = ['a','b','c','d']
    counter = 0
    for child in tree:
        for i in range(lengths[lindex]):
            child.add_child(TreeNode(letters[counter%4]))
            counter += 1
        lindex += 1
    print(tree)
    tree.pre_order_traverse()
    tree.in_order_traverse()
    tree.post_order_traverse()
    result = tree.find('a')
    print(result)
    for node in result:
        if node.parent != None:
            print("Node with payload '%s' at 0x%x & "
                "parent at 0x%x with payload %s"
                % (node, id(node), id(node.parent), node.parent.payload))
        else:
            print("Root node with payload '%s' at 0x%x" % (node, id(node)))
