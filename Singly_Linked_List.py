# A simple Python program to introduce a linked list
import copy

# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
       
# Linked List class contains a Node object 
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next
            
    def push(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, ptr_data, newdata):
        #check if ptr_data exists in linked list
        temp = self.head
        while (temp):
            if (temp.data == ptr_data): #to find if the data is present in list
                #print str(temp.data) + " " + str(ptr_data)
                break
            else:
                temp = temp.next
                #print temp
                
        if (temp == None):
            print "Data not found in linked list"
            return
        else:
            new_node = Node(newdata) 
            new_node.next = temp.next
            temp.next = new_node
            return
    
    def append(self, newdata):
        temp = self.head
        if ( temp == None): #list is empty
            self.head = Node(newdata)
        while(temp):
            prev = temp
            temp = temp.next
        new_node = Node(newdata)
        prev.next = new_node
    
    def delete_key(self, del_data):
        temp = self.head
        while (temp):
            if (temp.data == del_data):
                #print "Data found"
                break
            else:
                prev = temp
                temp = temp.next
        if (temp == None):
            print "Key value not found in list"
            return
        else:
            prev.next = temp.next
            del temp #Doubt
    
    def delete_position(self, del_pos):
        if (del_pos == 0):
            temp = self.head.next
            self.head = temp
            return
        else :
            count = 0
            temp = self.head
            while (temp):
                if (del_pos == count):
                    break
                else:
                    prev = temp
                    temp = temp.next
                    count += 1
            if (temp == None):
                print "Position does not exist in List"
                return
            else:
                prev.next = temp.next
                del temp
                
    def length_iterative(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    def length_recursive(self, node):
        if (node == None):
            return 0
        else:
            return 1 + self.length_recursive(node.next)
    
    def search_iterative(self,search_element):
        temp = self.head
        if(self.head == None):
            return False
        else:
            flag = False
            while(temp):
                #print str(temp.data) + " " + str(search_element)
                if (temp.data == search_element):
                    flag = True
                    return flag
                else:
                    temp = temp.next
            return flag
                
    def search_recursive(self, node, search_element):
        flag = False
        if (node == None):
            return flag
        elif (node.data == search_element):
            flag = True
            return flag
        else:
            return (self.search_recursive(node.next, search_element))
            
    def swap(self, x, y):
        #Nothing to do if x and y are same
        if (x == y):
            return;
 
        #Search for x keep track of prevX and currX
        prevX = None
        currX = self.head
        while (currX and currX.data != x):
            prevX = currX;
            currX = currX.next;
   
        #Search for y keep track of prevY and currY
        prevY = None
        currY = self.head
        while (currY and currY.data != y):
            prevY = currY;
            currY = currY.next;
 
        #If either x or y is not present, nothing to do
        if (currX == None or currY == None):
            return;
 
        #If x is not head of linked list
        if (prevX != None):
            prevX.next = currY;
        else: #Else make y as new head
            self.head = currY;  
 
        #If y is not head of linked list
        if (prevY != None):
            prevY.next = currX;
        else:  # Else make x as new head
            self.head = currX;
 
        #Swap next pointers
        temp = currY.next;
        currY.next = currX.next;
        currX.next  = temp;
    
    def getNth(self, n):
        temp = self.head
        count = 0
        while(temp and count != n):
            temp = temp.next
            count += 1
        if (temp != None):
            return temp.data
        else:
            return "Index does not exist"      
    
    def delete_node(self, ptr_node):
        temp = ptr_node.next
        ptr_node.data = temp.data
        ptr_node.next = temp.next
        del temp  
    
    def printMiddle_method2(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data
    
    def printMiddle_method3(self):
        mid = self.head
        temp = self.head
        count = 0
        while (temp):
            if (count%2 != 0):
                mid = mid.next
            count += 1
            temp = temp.next
        if (mid !=  None):
            return mid.data
        
    def findNthFromEnd_method2(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        while (count <= n):
            ref_ptr = ref_ptr.next
            count += 1
        while (ref_ptr):
            main_ptr = main_ptr.next
            ref_ptr  = ref_ptr.next
        return main_ptr.data
    
    def deleteList(self):
        curr = self.head
        while (curr):
            next = curr.next
            del curr
            curr = next
           
    def count(self, value):
        count = 0
        temp = self.head
        while(temp):
            if ( temp.data == value):
                count += 1
            temp = temp.next
        return count
    
    def reverse_iterative(self):
        prev = None
        next = None
        curr = self.head
        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    def reverse_recursive(self, list):
        if(self.head == None): # list is empty
            return
        first = list.head
        rest = first.next
        if (rest == None): # list has only one node
            return
        list.reverse_recursive(rest)
        first.next.next = first
        first.next = None
        list.head = rest
        
    def detectLoopFloyd(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while (slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr):
                return True
        return False

    def compare(self, list_after_reversal):
        temp1 = self.head
        temp2 = list_after_reversal.head
        while(temp1 and temp2):
            if(temp1.data != temp2.data):
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True
        
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    llist.head  = Node(1)
    second = Node(2)
    third  = Node(3)
 
    '''
    Three nodes have been created.
    We have references to these three blocks as first,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
 
    llist.head.next = second; # Link first node with second 
 
    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
 
    second.next = third; # Link second node with the third node
 
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    
    #------To display LinkedList------
    print "Initial List"
    llist.printList()
    
    #------Insert a new node into the list------
    print "List Insertion Variations"
    #1) to add a node in the front of the list
    newdata = 0
    llist.push(newdata)
    print "1)List after inserting 0 at the beginning"
    llist.printList()
    
    #2) To add a node after a given Node
    newdata = 2.5
    llist.insertAfter(2, newdata)
    print "2)List after inserting 2.5 after 2"
    llist.printList()
    
    #3) To add a node to the end of the linked list
    newdata = 4
    #llist1 = LinkedList()
    #llist1.append(newdata)
    llist.append(newdata)
    print "3)List after inserting 4 at the end"
    llist.printList()
    
    #------Deleting a node give the key------
    print "Deleting node with value 2.5"
    del_data = 2.5
    llist.delete_key(del_data)
    llist.printList()
    
    #------Deleting a node give the position------
    print "Deleting node at the 2nd position considering first element is at position 0"
    del_pos = 4
    llist.delete_position(del_pos)
    llist.printList()
    
    #------Length of Linked List Iterative------
    length = llist.length_iterative()
    print "Length of List - Iterative : " + str(length)
    
    #------Length of Linked List Recursive------
    length = llist.length_recursive(llist.head)
    print "Length of List - Recursive : " + str(length)
    
    #------Search an element in Linked List Iterative------
    search_element = 5
    #llist = LinkedList()
    value = llist.search_iterative(search_element)
    print "Search - Iterative : Element" + str(search_element) + " -> " + str(value)
    
    #------Search an element in Linked List Recursive------
    search_element = 3
    value = llist.search_recursive(llist.head, search_element)
    print "Search - Recursive : Element" + str(search_element) + " -> " + str(value)
    
    #Increase the Linked List by adding some more elements

    llist.append(4)
    llist.append(5)
    llist.append(6)
    llist.append(7)
    llist.append(8)
    llist.append(9)
    llist.append(10)

    llist.printList()
    #------Swap nodes in a linked list without swapping data------
    print "Swap nodes in a linked list without swapping data"
    x = 6
    y = 9
    llist.swap(x, y)
    llist.printList()
    
    #------To get Nth(index) node in a Linked List------
    n = 17 #Considering index starts with 0
    print "Element at index " + str(n) + " : " + str(llist.getNth(n))
    
    #------Given only a pointer/reference to a node to be deleted in a singly linked list------
    #Difficulty here is not to use the pointer to the head of list
    llist.delete_node(second)
    llist.printList()
    
    
    #------To print middle element of list------
    #Method 1: Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2.
    #Method 2: Traverse linked list using two pointers. Move one pointer by one and other pointer by two. When the fast pointer reaches end slow pointer will reach middle of the linked list.
    #Method 3: Initialize mid element as head and initialize a counter as 0. Traverse the list from head, while traversing increment the counter and change mid to mid->next whenever the counter is odd. So the mid will move only half of the total length of the list.
    
    #Implementing method 2
    print "Middle element of list by 2 ptr strategy is : " + str(llist.printMiddle_method2())
    
    #Implementing method 3
    print "Middle element of list by 1 ptr and odd count strategy is : " + str(llist.printMiddle_method3())
    
    #------Find n'th node from the end in a linked list------
    #Method 1 - print (len-n+1) node from beginning where n is length of linked list
    #Method 2 (Use 2 ptrs) 
    #Maintain two pointers reference pointer and main pointer. 
    #Initialize both reference and main pointers to head. 
    #First move reference pointer to n nodes from head. 
    #Now move both pointers one by one until reference pointer reaches end. 
    #Now main pointer will point to nth node from the end. Return main pointer.
    
    n = 5
    print str(n) + "th node from end is : " + str(llist.findNthFromEnd_method2(n))
    
    
    #------Delete entire linked list------
    llist_to_be_deleted = copy.deepcopy(llist)
    print "List before deletion "
    llist_to_be_deleted.printList() 
    print "List after deletion"
    llist_to_be_deleted.deleteList()
    
    #------Function to count the number of times a given value occurs in a Linked List ------
    llist.append(1)
    value = 1
    print "Value " + str(value) + " occurs : " + str(llist.count(value)) + " times"
    
    
    #------Function to reverse a Linked List------
    #1) Iterate trough the linked list. In loop, change next to prev, prev to current and current to next.
    print "list before Iterative reversal"
    llist.printList()
    llist.reverse_iterative()
    print "list after Iterative reversal"
    llist.printList()
    
    '''
    #1) Recursive : #Doubt
    # Divide the list in two parts - first node and rest of the linked list.
    # Call reverse for the rest of the linked list.
    # Link rest to first.
    # Fix head pointer
    print "list before Recursive reversal"
    llist.printList()
    llist.reverse_recursive(llist)
    print "list after Recursive reversal"
    llist.printList()
    '''
    
    #------Detect loop in a linked list------
    # Variations: hashing, mark visited nodes, floyds
    # Implementation using Floyd's
    # Create a loop for testing 
    llist_for_loop_testing = copy.deepcopy(llist)
    llist_for_loop_testing.head.next.next.next = llist_for_loop_testing.head;
    #llist_for_loop_testing.printList()
    llist.printList()
    print "Presence of loop in list : " + str(llist_for_loop_testing.detectLoopFloyd())
        
    #------Check if list is palindrome------
    #Method 1 : Compare list and its reversal - O(n) time and O(n) space - Can use stack
    llist_palindrome = LinkedList()
    llist_palindrome.push(0)
    llist_palindrome.push(1)
    llist_palindrome.push(2)
    llist_palindrome.push(1)
    llist_palindrome.push(0)
    llist_palindrome.printList()
    
    llist_before_reversal = copy.deepcopy(llist_palindrome)
    llist_palindrome.reverse_iterative()
    llist_after_reversal = copy.deepcopy(llist_palindrome)
    
    #------Palindrome - By Compare list and its reversal------
    print "The list is a palindrome: " + str(llist_before_reversal.compare(llist_after_reversal))
    
    #Method 2: Get mid point, reverse 2nd half, compare both halves to be identical, reverse back the second half #TODO
    #Method 3: By recursion to check palindrome #TODO

    