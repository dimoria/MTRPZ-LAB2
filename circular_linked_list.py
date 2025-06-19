class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert(self, element, index):
        if index < 0 or index > self.length():
            raise IndexError("Invalid index")
        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                new_node.next = new_node
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                new_node.next = self.head
                current.next = new_node
                self.head = new_node
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node

    def delete(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        if index == 0:
            removed_value = self.head.value
            if self.head.next == self.head:
                self.head = None
            else:
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next
                self.head = self.head.next
                tail.next = self.head
            return removed_value
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            removed_value = prev.next.value
            prev.next = prev.next.next
            return removed_value

    def deleteAll(self, element):
        while self.length() > 0 and self.head.value == element:
            self.delete(0)
        if not self.head:
            return
        current = self.head
        while current.next != self.head:
            if current.next.value == element:
                current.next = current.next.next
            else:
                current = current.next

    def get(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def clone(self):
        new_list = CircularLinkedList()
        if not self.head:
            return new_list
        current = self.head
        new_list.append(current.value)
        while current.next != self.head:
            current = current.next
            new_list.append(current.value)
        return new_list

    def reverse(self):
        prev = None
        current = self.head
        if not current:
            return
        start = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            if next_node == self.head:
                break
            current = next_node
        self.head.next = prev
        self.head = prev

    def findFirst(self, element):
        current = self.head
        index = 0
        if not current:
            return -1
        while True:
            if current.value == element:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def findLast(self, element):
        current = self.head
        index = 0
        last_found = -1
        if not current:
            return -1
        while True:
            if current.value == element:
                last_found = index
            current = current.next
            index += 1
            if current == self.head:
                break
        return last_found

    def clear(self):
        self.head = None

    def extend(self, other):
        current = other.head
        if not current:
            return
        self.append(current.value)
        while current.next != other.head:
            current = current.next
            self.append(current.value)
