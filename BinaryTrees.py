#python class that represents a node in a Binary Tree

class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
    
#To print Inorder traversal of a tree
def printInorder(root):
    if root:
        printInorder(root.left)
        print root.value,
        printInorder(root.right)

#To print Preorder traversal of a tree
def printPreorder(root):
    if root:
        print root.value,
        printPreorder(root.left)
        printPreorder(root.right)    
        
def iterativePreorder(root): #TODO
    if root:
        stack = []
        stack.push(root)
        
#To print Postorder traversal of a tree
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print root.value,

def height(root):
    if not(root):
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))       

def diameter(root):
    if not(root):
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        
        left_diameter = diameter(root.left)
        right_diameter = diameter(root.right)
    
        return max(max(left_diameter, right_diameter), left_height+right_height+1)

def nodeKDistance(root, k):
    if not(root):
        return
    elif (k == 0):
        print root.value,
    else:
        nodeKDistance(root.left, k-1)
        nodeKDistance(root.right, k-1)

def isLeaf(root):
    if not(root):
        return False
    elif (root.left == None and root.right == None):
        return True
    return False

def sumLeftLeaves(root):
    sum = 0
    if root is not None:
        if isLeaf(root.left):
            sum += root.left.value
        else:
            sum += sumLeftLeaves(root.left)
        sum += sumLeftLeaves(root.right)
    return sum

def findMax(root):
    if root is None:
        return
    current_data = root.value
    left_max = findMax(root.left)
    right_max = findMax(root.right)
    return max(current_data, left_max, right_max)

def levelOrder1(root):
    h = height(root)
    for i in range(1, h+1):
        levelOrderTraversalPrint(root, i)
        print "\n"
        
def levelOrderTraversalPrint(root, level):
    if root is None:
        return
    elif(level == 1):
        print root.value,
    elif (level > 1):
        levelOrderTraversalPrint(root.left, level-1)
        levelOrderTraversalPrint(root.right, level-1)
        
    
def levelOrderQueue(root):
    if root is None:
        return
    else:
        queue = []
        queue.append(root)
        while (1):
            node_count = len(queue)
            if ((node_count) == 0):
                break
            while(node_count > 0):
                #Print front of queue and remove it from queue
                print queue[0].value,
                current_node = queue.pop(0)
                
                #Enqueue left child
                if current_node.left is not None:
                    queue.append(current_node.left)
                #Enqueue right child
                if current_node.right is not None:
                    queue.append(current_node.right)
                node_count -= 1
            print "\n"
    
def iterativeSearch(root, key):
    if root is None:
        return False
    else:
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            current_node = queue.pop(0)
            if(key == current_node.value):
                return True
            if(current_node.left is not None):
                queue.append(current_node.left)
            if(current_node.right is not None):
                queue.append(current_node.right)    
    return False            
    
def hasPathSum(root, sum):
    if root is None:
        if (sum == 0):
            return True
        else:
            return False
        
    else:
        answer = False
        subSum = sum - root.value
        
        if(subSum == 0 and root.left == None and root.right == None):
            return True
        if(root.left is not None):
            answer = answer or hasPathSum(root.left, subSum)
        if(root.right is not None):
            answer = answer or hasPathSum(root.right, subSum)
        return answer        

if __name__ == '__main__':
    
    #create root
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(5)

    '''
        #Tree created is
             1
           /   \
          2      3
        /   \   /  \
       4    5 None None
      /  \
    None None
    '''
    print "Inorder"
    printInorder(root)
    print "\n\nPreorder"
    printPreorder(root)
    print "\n\nPostorder"
    printPostorder(root)
    
    print "\n\nHeight of tree is : "  + str(height(root)) #O(n)
    print "\nDiameter of tree is : " + str(diameter(root)) #O(n^2) TODO -> O(n)
    
    root.right.left = Node(8)
    '''
        #Now Tree is
             1
           /   \
          2      3
        /   \   /  \
       4    5 8 None
      /  \
    None None
    '''
    print "\nNodes at distance 2 from root is : " 
    nodeKDistance(root, 2) #O(n)
    
    print "\n\nSum of left leaves is : " + str(sumLeftLeaves(root)) #O(n)
    
    print "\nMaximum value of a node in the tree is : " + str(findMax(root))
    
    root.right.left.left = Node(7)
    '''
        #Now Tree is
             1
           /   \
          2      3
        /   \   /  \
       4    5 8 None
      /  \   /
    None    7
    '''
    print "\nLevel Order Traversal of Tree(method 1) : " 
    levelOrder1(root) #O(n^2)
    
    print "Level Order Traversal of Tree(method 2 using queue) : "
    levelOrderQueue(root) #O(n)
    
    print "Iterative search for value 3 in tree : " + str(iterativeSearch(root, 3))
    print "Iterative search for value 9 in tree : " + str(iterativeSearch(root, 9))
    
    print "There exists a path Root to leaf whose sum is 7 : " + str(hasPathSum(root, 7)) #O(n)