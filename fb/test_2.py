import collections

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val       

def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while (len(nodes)!=0):
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.val,end=" ")
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if (currentCount == 0):
            print("\n")
            currentCount, nextCount = nextCount, currentCount

def trimBST(tree, minVal, maxVal):     
    if not tree: 
        return     
    tree.left  = trimBST(tree.left,  minVal, maxVal) 
    tree.right = trimBST(tree.right, minVal, maxVal)     
    if (minVal<=tree.val<=maxVal): 
        return tree     
    if (tree.val<minVal): 
        return tree.right     
    if (tree.val>maxVal): 
        return tree.left 

tree = Node(8)
tree.left = Node(3)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.left.right.left = Node(4)
tree.left.right.right = Node(7)
tree.right = Node(10)
tree.right.right = Node(14)
tree.right.right.left = Node(13)
levelOrderPrint(tree)
tree2 = trimBST(tree, 5, 13)
levelOrderPrint(tree2)