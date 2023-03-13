class Node:
    def __init__(self, data):
        self.data = data
        self._next = None
        self._prev = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def addElementHead(self, data):
        baru = Node(data)
        if self._head is None:
            self._head = baru
            self._tail = baru
        else:
            baru._next = self._head
            self._head._prev = baru
            self._head = baru
    
    def addElementTail(self, data):
        baru = Node(data)
        if self._tail is None:
            self._tail = baru
            self._head = baru
        else:
            baru._prev = self._tail
            self._tail._next = baru
            self._tail = baru
    
    def maju(self, n):
        c = self._head
        for i in range(n):
            if c is None:
                break
            c = c._next
        if c is not None:
            print(c.data)
            self._head = c
    
    def mundur(self, n):
        c = self._head
        for i in range(n):
            if c is None:
                break
            c = c._prev
        if c is not None:
            print(c.data)
            self._head = c


# Contoh input & output program:

linkedlist = LinkedList()
linkedlist.addElementHead("Jogja") #Jogja
linkedlist.addElementHead("Jakarta") #Jakarta - Jogja
linkedlist.addElementTail("Bali") #Jakarta - Jogja - Bali
linkedlist.addElementTail("Bandung") #Jakarta - Jogja - Bali - Bandung

linkedlist.maju(2) #output: Bali
linkedlist.mundur(1) #output: Jogja
linkedlist.maju(1) #output: Bali
linkedlist.mundur(3) #output: Bandung