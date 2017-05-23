class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData():
        return self.data


class linkedlist:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next


if __name__ == '__main__':
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.printLinkedList()
