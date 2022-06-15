"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for i in range(len(string)):
    s.push(string[i])

while not s.is_empty():
    reversed_string += s.pop()
print(reversed_string)
