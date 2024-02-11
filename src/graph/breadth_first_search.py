from collections import deque


# def bfs(rg, query):
#     visited = set()
#     queue = deque()
#     i = True

#     while queue or i:
#         if i:
#             neighbours = rg.roots()
#             i = False
#         else:
#             vertex = queue.popleft()
#             neighbours = rg.neighbours(vertex)


#         for neighbour in neighbours:
#             if neighbour not in visited:
#                 if query(neighbour):
#                     return neighbour, visited
#                 visited.add(neighbour)
#                 queue.append(neighbour)
#     return None, visited

def bfs(rg, query):
    visited = set(rg.roots())
    queue = deque(rg.roots())

    for root in rg.roots():
        if query(root):
            return (root, visited)

    while queue:
        vertex = queue.popleft()
        for neighbour in rg.neighbours(vertex):
            if neighbour not in visited:
                if query(neighbour):
                    return (neighbour, visited)
                visited.add(neighbour)
                queue.append(neighbour)

    return (None, visited)
