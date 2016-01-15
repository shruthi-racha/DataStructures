# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
        
#Stack class contains a Node object
class Stack:
    # Function to initialize root
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if (self.root is None):
            return 1
        else:
            return 0    
        
    def pushStack(self, item):
        temp = Node(item)
        temp.next = self.root
        self.root = temp
        
    def popStack(self):
        if (self.root is None):
            return "Underflow"
        else:
            temp = self.root.next
            popped = self.root.data
            self.root = temp
            del temp
            return popped
        
    def peekStack(self):
        if (self.root is None):
            return "Stack is empty"
        else:
            return self.root.data
            
    def displayStack(self):
        temp = self.root
        while(temp):
            print temp.data,
            temp = temp.next
            
if __name__ == '__main__' :
    stack = Stack()
    #print stack.isEmpty()
    stack.root = Node(10)
    #print stack.isEmpty()
    stack.pushStack(20)
    stack.pushStack(30)
    stack.displayStack()
    
    print "\n" + str(stack.popStack()) + " item is popped"
    print str(stack.popStack()) + " item is popped"
    print str(stack.popStack()) + " item is popped"
    print str(stack.popStack()) + " item is popped"
    
    stack.pushStack(1)
    stack.pushStack(2)
    stack.pushStack(3)
    
    stack.displayStack()
    print "\n" + str(stack.peekStack()) + " is the top item in the stack"
    stack.displayStack()


