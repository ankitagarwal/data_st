"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos2, read_maze
from stack import Stack


def dfs(maze, start, goal):
    s = Stack()
    predecessors = {start: None}
    if not (is_legal_pos2(maze, start) and is_legal_pos2(maze, goal)):
        return 0
    s.push(start)
    while not s.is_empty():
        cur = s.pop()
        if cur == goal:
            return 1
        for direction in ["up", "left", "right", "down"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (cur[0] + row_offset, cur[1] + col_offset)
            if is_legal_pos2(maze, neighbour) and neighbour not in predecessors:
                s.push(neighbour)
                predecessors[neighbour] = cur
    return 0


if __name__ == "__main__":

    # Test 2
    maze = read_maze("mazes/maze_meta1.txt")
    for row in maze:
        print(row)

    n_cols = len(maze[0])
    n_rows = len(maze) - 1
    total = 0
    # print((0, 1), (3, 2), dfs(maze, (0, 1), (3, 2)))
    for i in range(n_cols):
        for j in range(n_cols):
            start = (0, i)
            goal = (n_rows, j)
            total += int(dfs(maze, start, goal))
            print(start, goal, dfs(maze, start, goal))
    print("Number of total paths - ", total)