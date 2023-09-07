class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    head = None
    tail = None
    length = 0

    def printList(self):
        if(self.head==None):
            print("The List is Empty!")
            return
        else:
            headCopy = self.head
            while(headCopy):
                print(headCopy.data, end=" ")
                headCopy = headCopy.next
    
    def append(self, data):
        newNode = Node(data=data)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = None
        self.length += 1
    
    def prepend(self, data):
        newNode = Node(data=data)
        if(self.head == None):
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return
        newNode.next = self.head
        self.head = newNode
    
    def reverse(self):
        if(self.head == None):
            print("The list is Empty!")
            return
        prev = None
        currHead = self.head
        while(currHead):
            new = currHead.next
            currHead.next = prev
            prev = currHead
            currHead = new
        self.head = prev
            
ll = SinglyLinkedList();

ll.append(5)
ll.append(6)
ll.append(1)
ll.append(10)
ll.prepend(11)
ll.reverse()
ll.printList()



        