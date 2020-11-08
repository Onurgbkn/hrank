class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:


    def __init__(self, indexes):
        self.root = Node(1)

        nodestack = [self.root]

        for i in indexes:
            itr = nodestack[0]
            if i[0] != -1:
                itr.left = Node(i[0])
                nodestack.append(itr.left)
            if i[1] != -1:
                itr.right = Node(i[1])
                nodestack.append(itr.right)

            nodestack.pop(0)


    def swapnodes(self):
        # TO DO
        pass


    def Printree(self):
        print(self.root.data)
        print(self.root.left.data)
        print(self.root.left.left.data)
        print(self.root.left.left.left.data)


    def Inorderprint(self, temproot):
        itr = temproot
        if itr.left != None:
            self.Inorderprint(itr.left)

        print(itr.data)

        if itr.right != None:
            self.Inorderprint(itr.right)




tre = BinaryTree([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]])

tre.Inorderprint(tre.root)
