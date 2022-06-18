"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.is_empty())
    print(q)
    q.dequeue()
    print(q)
