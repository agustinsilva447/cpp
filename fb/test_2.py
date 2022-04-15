class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

def find_node(root,q):
  if root.val == q:
    return root
  elif root.children:
    for c in root.children:
      d = find_node(c,q)
      if d:
        return d

def matching(root,q,s):
  if root == None:
    return 0
  if root.children == []:
    if s[root.val-1] == q:
      return 1
    else:
      return 0
  else:
    if s[root.val-1] == q:
      match = 1
    else:
      match = 0    
    for c in root.children:
      match += matching(c,q,s)  
    return match

def count_q(root,q,s):
  root_2 = find_node(root,q[0])
  o = matching(root_2, q[1], s)
  return o

def count_of_nodes(root, queries, s):
  output = [0] * len(queries)
  for i, q in enumerate(queries):
    output[i] = count_q(root,q,s)
  return output
    
#############################################################################################################    
    
def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
      if i != 0:
          print(', ', end='')
      print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
      result = False
  for i in range(min(expected_size, output_size)):
      result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":

  # Testcase 1
  n_1 ,q_1 = 3, 1 
  s_1 = "aba"
  root_1 = Node(1) 
  root_1.children.append(Node(2)) 
  root_1.children.append(Node(3)) 
  queries_1 = [(1, 'a')]

  output_1 = count_of_nodes(root_1, queries_1, s_1)
  expected_1 = [2]
  check(expected_1, output_1)

  # Testcase 2
  n_2 ,q_2 = 7, 3 
  s_2 = "abaacab"
  root_2 = Node(1)
  root_2.children.append(Node(2))
  root_2.children.append(Node(3))
  root_2.children.append(Node(7))
  root_2.children[0].children.append(Node(4))
  root_2.children[0].children.append(Node(5))
  root_2.children[1].children.append(Node(6))
  queries_2 = [[1, 'a'],[2, 'b'],[3, 'a']]
  output_2 = count_of_nodes(root_2, queries_2, s_2)
  expected_2 = [4, 1, 2]
  check(expected_2, output_2)