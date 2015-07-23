ass Tree:

    root = None
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if(self.root is None):
            self.root = Node(key)
            return node
        if(node is None):
            return Node(key)
        elif(key <= node.key):
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node

    def deleteNode(self, node, key):
        if(node is None):
            return node
        elif(key < node.key):
            node.left = self.deleteNode(node.left, key)
            return node
        elif(key > node.key):
            node.right = self.deleteNode(node.right, key)
            return node
        else: #found the node to delete
            #case 1: leaf node no children
            if(node.left is None and node.right is None):
                del node
                node = None
                return node
            #case 2: One child
            elif(node.left is None):
                temp = node
                node = node.right
                del temp
                return node
            elif(node.right is None):
                temp = node
                node = node.left
                del temp
                return node
            #case 3: 2 children
            else:
                temp = node.right
                node.key = temp.key
                node.right = self.deleteNode(node.right, temp.key)
                return node
        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def levelorder(self, node, more):
        if node is not None:
            if more is None:
                more = []
            more.append(node.left)
            more.append(node.right)
            print(node.key)
        if more:
            self.levelorder(more[0], more[1:])



class Node:
    left = None
    right = None
    def __init__(self, key):
        self.key = key

t = Tree()
t.insert(t.root, 15)
t.insert(t.root, 10)
t.insert(t.root, 20)
t.insert(t.root, 19)
t.insert(t.root, 25)
#t.insert(t.root, 32)
t.inorder(t.root)
print("---------")
t.deleteNode(t.root, 20)
#t.inorder(t.root)
print("-levelorder-")
t.levelorder(t.root, None)

