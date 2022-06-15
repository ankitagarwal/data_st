"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack


def dfs(maze, start, goal):
    s = Stack()
    predecessors = {start: None}
    if not (is_legal_pos(maze, start) and is_legal_pos(maze, goal)):
        raise Exception("Invalid start or goal provided.")
    s.push(start)
    while not s.is_empty():
        cur = s.pop()
        if cur == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "left", "right", "down"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (cur[0] + row_offset, cur[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                s.push(neighbour)
                predecessors[neighbour] = cur


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
