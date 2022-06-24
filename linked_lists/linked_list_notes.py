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