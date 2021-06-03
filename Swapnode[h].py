# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import sys
sys.setrecursionlimit(15000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, indexes):
        self.root = Node(1)
        self.deps = []

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


    def swapnodes(self, swapdeps):
        for i in swapdeps:
            self.deps = []
            self.Depthnodes(self.root, 1, i)
            for i in self.deps:
                #print(i.data)
                i.left, i.right = i.right, i.left
            self.Inorderprint(self.root)
            print('')


    def Depthnodes(self, root, curDepth, sDepth):
        if sDepth == curDepth or curDepth % sDepth == 0:
            self.deps.append(root)

        if root.left != None:
            self.Depthnodes(root.left, curDepth+1, sDepth)
        if root.right != None:
            self.Depthnodes(root.right, curDepth+1, sDepth)


    def Inorderprint(self, temproot):
        if temproot.left != None:
            self.Inorderprint(temproot.left)

        print(temproot.data, end=" ")

        if temproot.right != None:
            self.Inorderprint(temproot.right)


if __name__ == '__main__':

    tree = []
    depths = []

    f = open(r'C:\Users\lma10ur\Desktop\input\input03.txt')

    for _ in range(int(f.readline())):
        tree.append(list(map(int, f.readline().split())))

    for _ in range(int(f.readline())):
        depths.append(int(f.readline()))


    BT = BinaryTree(tree)
    BT.swapnodes(depths)


# print(round((((1+(5**0.5))/2)**int(input()))/(5**0.5)))
