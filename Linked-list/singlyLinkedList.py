class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    head = None
    tail = None
    length = 0

    def printList(self, head):
        if(head==None):
            print("The List is Empty!")
            return
        else:
            headCopy = head
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
    #Iterative way
    def reverse(self):
        if(self.head == None):
            print("The list is Empty!")
            return
        #Iterative way
        prev = None
        currHead = self.head
        while(currHead):
            new = currHead.next
            currHead.next = prev
            prev = currHead
            currHead = new
        self.head = prev

    #convertion of orientation l0 -> L1 -> ... Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 
    def reorder(self):
        slow = self.head
        fast = self.head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        secondHead = slow.next
        slow.next = None

        prev = None
        while(secondHead):
            temp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = temp
        
        firstHead, secondHead = self.head, prev
        while(secondHead):
            tmp1, tmp2 = firstHead.next, secondHead.next
            firstHead.next = secondHead
            secondHead.next = tmp1
            firstHead, secondHead = tmp1, tmp2
        
    def removeElements(self, val):
        dummy = Node(next=self.head)
        prev, curr = dummy, self.head
        while(curr):
            if(curr.data == val):
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        self.printList(dummy.next)

ll = SinglyLinkedList();

ll.append(5)
ll.append(6)
ll.append(1)
ll.append(10)
ll.append(10)
ll.append(3)
ll.append(7)
ll.append(9)
ll.removeElements(5)

# ll.prepend(11)
# ll.reverse()
# ll.reorder()

# ll.printList(ll.head)



        