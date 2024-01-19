from collections import deque


def bfs(rg, query):
    visited = set()
    queue = deque()
    i = True

    while queue or i:
        if i:
            neighbours = rg.roots()
            i = False
        else:
            vertex = queue.popleft()
            neighbours = rg.neighbours(vertex)

        for neighbour in neighbours:
            if neighbour not in visited:
                if query(neighbour):
                    return neighbour, visited
                visited.add(neighbour)
                queue.append(neighbour)
    return None, visited
