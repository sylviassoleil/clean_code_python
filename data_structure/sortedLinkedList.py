class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

if __name__ == '__main__':
    pass




