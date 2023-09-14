# A queue is a useful data structure in programming. It is similar to the ticket 
# queue outside a cinema hall, where the first person entering the queue is the first person 
# who gets the ticket.
# Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

class Queque:

    # init list data
    def __init__(self, data: list) -> None:
        self.__data = data

    # Add an element to the end of the queue
    def enqueque(self, element) -> bool:
        if self.isFull():
            return False
        
        self.__data.append(element)
        return True

    # Remove an element from the front of the queue
    def dequeque(self):
        if self.isEmpty():
            return None
            
        return self.__data.pop(0)

    # Check if the queue is empty
    def isEmpty(self) -> bool:
        return not self.__data
    
    # Check if the stack is full
    def isFull(self) -> bool:
        return False
    
    # Get the value of the front of the queue without removing it
    def peek(self):
        if self.isEmpty():
            return None
        
        return self.__data[0]
    
    # Return all elements  
    def all(self):
        return self.__data
    

# checking code
queque = Queque([])
print("isEmpty:", queque.isEmpty())
print("isFull:", queque.isFull())
queque.enqueque(1)
queque.enqueque(2)
queque.enqueque(3)
print("peek:", queque.peek())
print("all:", queque.all())
print("dequeque:", queque.dequeque())
print("dequeque:", queque.dequeque())
queque.enqueque(10)
queque.enqueque(11)
queque.enqueque(12)
print("all:", queque.all())