# A stack is a linear data structure that follows the principle of Last In First Out (LIFO). 
# This means the last element inserted inside the stack is removed first.

class Stack:

    # init data list
    def __init__(self, data: list) -> None:
        self.__data = data

    # Add an element to the top of a stack
    def push(self, element) -> bool:
        if self.isFull():
            return False
        
        self.__data.append(element)
        return True

    # Remove an element from the top of a stack
    def pop(self):
        if self.isEmpty():
            return False
        
        return self.__data.pop()

    # Check if the stack is empty
    def isEmpty(self):
        return not self.__data

    # Check if the stack is full
    def isFull(self) -> bool:
        return False

    # Get the value of the top element without removing it
    def peek(self):
        if self.isEmpty():
            return None
        
        return self.__data[len(self.__data) - 1]

    # Return all elements  
    def all(self):
        return self.__data
    
# checking code
stack = Stack([])
print("isEmpty:", stack.isEmpty())
print("isFull:", stack.isFull())
stack.push(12)
stack.push(13)
stack.push(14)
print("peek:", stack.peek())
print("all:", stack.all())
print("pop:", stack.pop())
stack.push(33)
print("all:", stack.all())

# The most common uses of a stack are:
# 1. To reverse a word - 
#       Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
# 2. In browsers - 
#       The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
# 3. In compilers - 
#       Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.