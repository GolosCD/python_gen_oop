class TreeBuilder:
    level = -1
    tree = []

    def __init__(self):
        self.tmp = dict()

    def __enter__(self):
        __class__.level += 1
        self.tmp[__class__.level] = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.tmp[__class__.level]:
            del self.tmp[__class__.level]
        if __class__.level > 0:
            try:
                self.tmp[__class__.level - 1].append(self.tmp[__class__.level])
            except:
                pass
        else:
            __class__.tree.append(self.tmp[__class__.level])
        __class__.level -= 1

    def add(self, obj):
        if self.level < 0:
            __class__.tree.append(obj)
        else:
            self.tmp[__class__.level].append(obj)

    def structure(self):
        return __class__.tree

        
        
        
'''        
# class Node:
    # def __init__(self, data):
        # self.left = None
        # self.right = None
        # self.data = data

# class TreeBuilder:
    # def __init__(self):
        # self.root = None

    # def add(self, data):
        # if self.root is None:
            # self.root = Node(data)
        # else:
            # self._add(data, self.root)

    # def _add(self, data, node):
        # if data < node.data:
            # if node.left is None:
                # node.left = Node(data)
            # else:
                # self._add(data, node.left)
        # elif data > node.data:
            # if node.right is None:
                # node.right = Node(data)
            # else:
                # self._add(data, node.right)

    # def remove_empty_nodes(self):
        # if self.root:
            # self._remove_empty_nodes(self.root)

    # def _remove_empty_nodes(self, node):
        # if node:
            # if node.left:
                # if not (node.left.left or node.left.right):
                    # node.left = None
                # else:
                    # self._remove_empty_nodes(node.left)
            # if node.right:
                # if not (node.right.left or node.right.right):
                    # node.right = None
                # else:
                    # self._remove_empty_nodes(node.right)    '''    
        
        
tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
        
print(tree.structure())       