class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class MidDeque:
    def __init__(self, head=None, tail=None, mid=None):
        self.head = head
        self.tail = tail
        self.mid = mid
        self.size = 0

    def push_back(self, x):
        self.size += 1
        node = Node(x)
        if self.head is None:
            self.head = self.tail = self.mid = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        if self.size > 1 and self.size % 2 == 1:
            self.mid = self.mid.next

    def push_front(self, x):
        self.size += 1
        node = Node(x)
        if self.head is None:
            self.head = self.tail = self.mid = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        if self.size % 2 == 0:
            self.mid = self.mid.prev

    def push_mid(self, x):
        self.size += 1
        node = Node(x)
        if self.head is None:
            self.head = self.tail = self.mid = node
        else:
            if self.size == 2:
                node.next = self.mid
                self.mid.prev = node
                self.mid = self.head = node
            elif self.size % 2 == 1:
                node.next = self.mid.next
                self.mid.next = node
                node.prev = self.mid
                node.next.prev = node
                self.mid = self.mid.next
            else:
                node.next = self.mid
                node.prev = self.mid.prev
                self.mid.prev.next = node
                self.mid.prev = node
                self.mid = node

    def pop_back(self):
        self.size -= 1
        popped_node = self.tail
        if self.size == 0:
            self.tail = self.mid = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            if self.mid.prev and self.size % 2 == 0:
                self.mid = self.mid.prev
        return popped_node.value

    def pop_front(self):
        self.size -= 1
        popped_node = self.head
        if self.size == 0:
            self.tail = self.mid = self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            if self.mid.next and self.size % 2 == 1:
                self.mid = self.mid.next
        return popped_node.value

    def pop_mid(self):
        self.size -= 1
        popped_node = self.mid
        if self.size == 0:
            self.tail = self.mid = self.head = None
        else:
            if self.mid.prev:
                if self.size % 2 == 0:
                    self.mid = self.mid.prev
                else:
                    self.mid = self.mid.next
                popped_node.prev.next = popped_node.next
                popped_node.next.prev = popped_node.prev
            else:
                self.mid.next = None
                self.tail.prev = None
                self.mid = self.head = self.tail
        return popped_node.value
