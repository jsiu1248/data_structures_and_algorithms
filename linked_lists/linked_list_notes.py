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