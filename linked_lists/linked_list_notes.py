"""A linked list is a series of connected nodes.
It has a multiple nodes, which each node has a value and pointer/next
Pros:
Ease of Insertion and Deletion
Not set size

Con:
Have to start from the head node
Extra memory is needed
Not cache friendly

"""

class Node:
    def __init__(self, value):
        self.value = value # Assign data/value
        self.next = None # next starts off as null

#class for linked list
class LinkedList:
    def __init__(self):
        self.head=None

    #function for traversing through linked list
    def PrintList(self):
        # initially I think that this is starting at 1
        temp = self.head

        # while temp is true (as long as it is not empty) continue printing the value
        while (temp):
            print(temp.value)
            # go to the next Node
            temp=temp.next

        """
3 ways to insert a new node
1. in the front - push
2. after give node
3. at the end"""
    #function to push new node in the front

    def push(self, new_value):
        # make a new node with a value
        new_node = Node(new_value)

        # make next of Node as head
        new_node.next = self.head

        # move head to point to new node
        self.head= new_node
# Time complexity is O(1)

    #function to add a node after a given node
    def insertAfter(self,prev_node, new_value):

        # check if the prev_node exists
        if prev_node is None:
            print("The previous node is not in the linked list.")
            return
        #make a node with a value
        new_node = Node(new_value)

        # make next of new node as next of prev_node
        new_node.next = prev_node.next

        # make next of prev_node as new_node
        prev_node.next = new_node

        # Time Complexity is O(n) because it depends on the size of list
        # Space Complexity: O(1) constant space to modify pointers

    # function to add node at the end
    def append(self, new_value):

        #make a node with a value
        new_node = Node(new_value)

        # check if linked list is empty then make new node as head
        if self.head is None:
            self.head=new_node
            return

        # traverse until the last node
        # temporarily making the last variable the first node
        last = self.head
        while (last.next):
            last = last.next

        # change the next of last node
        last.next = new_node

        # Time complexity is O(n) since it is a loop from head to end
        # Space is O(1) by keeping extra pointer to the tail
"""
3 ways to delete
1. delete from beginning
    a. point head to the next node
2. delete from middle
    a. traverse to the element before the element that needs
    to be deleted
    b. change next pointer to exclude the node from the chain

3. delete from the end
    a. point head to the second to the last element
    b. change next pointer to null
"""
def deleteNode(self, key):
        # store head node temporarily
        temp = self.head

        # if head node holds the key to be deleted
        if temp.data == key:
            # make head node the temp's next node
            self.head = temp.next
            temp = None
            return

        # search for key to be deleted
        # keep track of the previous node as we need to
        # change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            return

        # unlink the node from linked list
        prev.next = temp.next

        temp = None


        """
        Questions:
        How to calculate time and space complexity?
        """










if __name__=="main":

    # Creating and empty list
    llist= LinkedList()

    # creating the three Nodes
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)

    # link first node with the second
    llist.head.next = second

    # link second node with the third
    second.next = third

    llist.append(5)
    llist.push(7)
    llist.insertAfter(llist.head.next, 5)
    llist.PrintList()
    print("x")