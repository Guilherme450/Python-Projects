class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, new_data: int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head:
            removed_head = self.head
            self.head = self.head.next

            return removed_head.data
        
        return None

    def is_empty(self):
        return self.head is None
    
    def top(self):
        return self.head.data
    
    def show_stack(self):
        current = self.head

        if  self.is_empty():
           return None

        while current is not None:
            print(f'{current.data} -> ', end='')

            current = current.next

        print('NULL')
        return 

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(45)
    stack.push(67)
    stack.push(23)
    stack.push(84)
    stack.push(12)

    stack.show_stack()

    stack.pop()
    stack.show_stack()