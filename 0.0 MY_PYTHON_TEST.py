class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class TreeBuilder:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(data, node.right)

    def remove_empty_nodes(self):
        if self.root:
            self._remove_empty_nodes(self.root)

    def _remove_empty_nodes(self, node):
        if node:
            if node.left:
                if not (node.left.left or node.left.right):
                    node.left = None
                else:
                    self._remove_empty_nodes(node.left)
            if node.right:
                if not (node.right.left or node.right.right):
                    node.right = None
                else:
                    self._remove_empty_nodes(node.right)    
                    
                    
tr = TreeBuilder()


tr.add(8)

tr.add(2)


tr.add(3)


print(tr.root.data)