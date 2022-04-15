class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

def depth_nodes(root):
  if root == None:
    return 0
  else:
    vis_left  = depth_nodes(root.left)
    vis_right = depth_nodes(root.right)
    
    if vis_left > vis_right:
      return vis_left + 1
    else:
      return vis_right + 1 

def visible_nodes(root):  
  return depth_nodes(root)

root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right = TreeNode(10)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)

a = visible_nodes(root_1)
print(a)