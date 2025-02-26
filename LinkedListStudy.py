class Node:
    # fundamental structucture of single linked list (The Node, which contains the value/data and an address to the next Node)
    def __init__(self, value: int):
        self.value = value # Space in the memory reservated to the data
        self.next = None # Pointer/Address to the next Node

class SingleLinkedList:
    # the whole structure of Single Linked List where all of the operations will occur thus it is the place where we will implement some
    # essential algorithms for operations.
    def __init__(self):
        self.head = None

    def push(self, value: int) -> None:
        # This function appends the value in the beggining of the list
        new_node = Node(value)# New instance of a Node

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head# The current element will become the second in the list, cause the new node is pointing to the head.

        self.head = new_node# the new node will become then the head of the node
    
    def end_push(self, value:int) -> None:
        new_node = Node(value)
        current = self.head
        previous = None

        if current is not None:
            while current and current.next:
                previous = current

                current = current.next
            
            previous.next = new_node
            return
        
        current = new_node
        return

    def pop(self) -> None:
        # function that removes the last element in the list by changing the pointer which will point to None
        current = self.head # Current Node
        previous = None # penultimate node int the list

        while current and current.next:
            # Travese the list until reach the penultimate node
            previous = current

            current = current.next
        
        if previous is not None:
            previous.next = None # The penultimate node will then piont to None.


    def search(self, value: int) -> None:
        if self.head is not None:
            current = self.head

            while current is not None:
                if current.value == value:
                    print(f"Value Found: {value}")
                    return
                current = current.next
        print(f"The value: {value} do not exist in the list.")
        return

    def show(self) -> None:
        # Function for traversing forward the values in the Nodes
        if self.head is None:
            print('Lista vazia')
            return
    
        current = self.head # Current Node, it will change during the execution

        while current is not None:
        # This block of code will print each element/value of each node while it is not None
            print(f"{current.value} -> ", end= " ")# print of the content of the Node

            current = current.next # Next Node
        print("None")

if __name__ == "__main__":
    sll = SingleLinkedList()

    sll.push(12)
    sll.push(23)
    sll.push(56)
    sll.push(90)
    sll.push(34)
    sll.push(67)

    sll.show()
    sll.search(90)
    sll.search(24)

    sll.pop()
    sll.show()
    sll.pop()
    sll.show()
    sll.push(100)
    sll.show()
    sll.end_push(900)
    sll.show()
