"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def is_empty(self):
        return not self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(10)
    s.push(-20)
    print(s.is_empty())
    print(s)
    print(s.peek())
    s.pop()
    print(s)
