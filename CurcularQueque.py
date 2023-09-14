# A circular queue is the extended version of a regular queue where the last element is 
# connected to the first element. Thus forming a circle-like structure.
# Circular Queue works by the process of circular increment i.e. when we try to increment 
# the pointer and we reach the end of the queue, we start from the beginning of the queue.

class CurcularQueque:

    # init data list
    def __init__(self, size: int) -> None:
        self.__front = -1
        self.__rear = -1
        self.__size = size
        self.__data = [None] * size

    def enqueque(self, element):
        if self.isFull():
            raise Exception("Curcular Queque is full")
        
        if self.__front == -1 and self.__rear == -1:
            self.__front = 0
        
        if self.__rear + 1 == self.__size:
            self.__rear = 0
        else:
            self.__rear += 1

        self.__data[self.__rear] = element

    def dequeque(self):
        if self.isEmpty():
            raise Exception("Curcular Queque is empty")
        
        temp = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front += 1

        if self.__front == self.__size and (self.__rear + 1 == self.__size):
            self.__front = -1
            self.__rear = -1

        return temp

    def isFull(self) -> bool:
        return (self.__rear + 1 == self.__front) or (self.__front == 0 and self.__rear + 1 == self.__size)
    
    def isEmpty(self) -> bool:
        return self.__rear == -1 and self.__front == -1
    
    def all(self):
        return self.__data
    

#  TESTING 1
queque = CurcularQueque(4)
print("display:", queque.all())
print("empty: ", queque.isEmpty())
print("full: ", queque.isFull())

queque.enqueque(1)
queque.enqueque(1)
queque.enqueque(1)
queque.enqueque(1)
# queque.enqueque(1) // raise exception
print("display:", queque.all())

print("dequeque:", queque.dequeque())
print("dequeque:", queque.dequeque())
print("dequeque:", queque.dequeque())
print("dequeque:", queque.dequeque())
# print("dequeque:", queque.dequeque()) // raise exception
queque.enqueque(1)
print("display:", queque.all())

# TESTING 2
queque = CurcularQueque(4)
print("display:", queque.all())
print("empty: ", queque.isEmpty())
print("full: ", queque.isFull())

queque.enqueque(1)
queque.enqueque(1)
print("display:", queque.all())

print("dequeque:", queque.dequeque())
queque.enqueque(1)
queque.enqueque(1)
queque.enqueque(1)
print("display:", queque.all())

# TESTING 3
queque = CurcularQueque(3)
print("display:", queque.all())
queque.enqueque(1)
queque.enqueque(1)
queque.enqueque(1)
print("display:", queque.all())
print("dequeque:", queque.dequeque())
print("display:", queque.all())
print("empty: ", queque.isEmpty())
print("full: ", queque.isFull())
queque.enqueque(1)
print("display:", queque.all())
print("dequeque:", queque.dequeque())
print("display:", queque.all())

