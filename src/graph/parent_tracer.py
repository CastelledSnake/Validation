from graph.rooted_graph import RootedGraph


class ParentTracer(RootedGraph):
    def __init__(self, rg: RootedGraph):
        self.rg = rg
        self.parents = {}

    def roots(self):
        roots = self.rg.roots()
        for node in roots:
            self.parents[node] = None
        return roots

    def neighbours(self, node):
        neighbours = self.rg.neighbours(node)
        for neighbour in neighbours:
            if neighbour not in self.parents:
                self.parents[neighbour] = [node]
        return neighbours

    def get_trace(self, solution):
        trace = [solution]
        parent = self.parents.get(solution)
        while parent is not None and len(parent) > 0:
            parent = parent[0]
            trace.append(parent)
            parent = self.parents[parent]
        return trace
