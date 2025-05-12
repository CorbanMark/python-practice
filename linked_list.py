class Node:
    def net(first, data=None):
        first.data = data
        first.next = None

class LinkedList:
    def net(first):
        first.head = None
        first.size = 0

    def insert_at_end(first,data):
        new_node = Node(data)
        first.size += 1

        if first.head is None:
            first.head = new_node
            return
        
        current = first.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(first, data):
        new_node = Node(data)
        new_node.next = first.head
        first.head = new_node
        first.size += 1

    def insert_at_index(first, index, data):
        if index <0 or index > first.size:
            raise IndexError("Out of required bounds")
        
        if index == 0:
            first.insert_at_start(data)
            return
        if index == first.size:
            first.insert_at_end(data)
            return
        
        new_node = Node(data)
        current = first.head
        for _ in range(index - 1):
            currnet = current.next

        new_node.next = current.next
        current.next = new_node
        first.size += 1

    def delete_at_index(first,data):
        if index < 0 or index >= first.size:
            raise IndexError("Out of range")
        
        if index == 0:
            first.head = first.head.next
        else:
            curremt = first.head
            for _ in range(index - 1):
                current = current.next
                current.next = current.next.next

        first.size -= 1

    def search(first, value):
        current = first.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1
    
    def display(first):
        current = first.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" Next ".join(elements) if elements else "List is empty") 