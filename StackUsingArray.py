#Function to create stack and initialize size to 0
def createStack():
    stack = []
    return stack

#Stack is empty when size is 0
def isEmpty(stack):
    if (len(stack) == 0):
        return 1
    else:
        return 0
    
#Function to add an item to top of stack. It increases size by 1
def pushStack(stack, item):
    stack.append(item)
    print ("Pushed to stack " + item)
    
#Function to remove an item from stack. It decreases size by 1
def popStack(stack):
    if (isEmpty(stack)):
        return -1
    else:
        return stack.pop()
    
#Function to get top item from stack
def peekStack(stack):
    if (isEmpty(stack)):
        return -1
    return stack[len(stack) - 1]

if __name__ == '__main__':
    stack = createStack()
    pushStack(stack, str(10))
    pushStack(stack, str(20))
    pushStack(stack, str(30))
    print (popStack(stack) + " item popped from stack")
    print (peekStack(stack) + " is the top item of stack")
