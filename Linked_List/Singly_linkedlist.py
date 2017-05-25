#Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData():
        return self.data
#linkedlist
class linkedlist:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next

    def getLength(self):
        temp = self.head
        count = 0
        while(temp):
            count = count + 1
            temp = temp.next
        return count
    
    def insertAtStart(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self,data):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = Node(data)

    def insertAfter(self,prevNode,data):
        if prevNode is None:
            print("empty previous node")
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def deleteAtStart(self):
        if (self.head == None):
            print("linked list is empty")
            return
        else:
            temp = self.head.next
            self.head = temp

    def deleteAtEnd(self):
        if(self.head == None):
            print("linked list is empty")
            return
        else:
            temp = self.head
            while((temp.next).next):
                temp = temp.next
            temp.next = None

if __name__ == '__main__':
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.insertAtStart(0)
    llist.insertAtEnd(4)
    
    llist.insertAtEnd(5)
    llist.deleteAtStart()
    llist.insertAfter(third,3.5)
    llist.deleteAtEnd()
    llist.printLinkedList()
    
    
    
    print("length of linked list is ",llist.getLength())
