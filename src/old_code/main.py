from graph.parent_tracer import ParentTracer
from old_code.graphs import bfs_search
from old_code.hanoi import HanoiGraph


if __name__ == "__main__":
    # rg = RootedGraph({1: [2, 3], 2: [3, 4], 3: [], 4: []}, 1)
    # def a(n: Node) -> bool:
    #     return n == 2

    # def b(n: Node) -> bool:
    #     return n == 5

    # print(bfs_search(rg, a))
    # print(bfs_search(rg, b))

    # hanoi = HanoiGraph(2, (0, 0))
    hanoi = HanoiGraph(3, (0, 0, 0))
    parent_tracer = ParentTracer(hanoi)
    t, k = bfs_search(parent_tracer, hanoi.is_solution)
    print(t, k)
    trace = parent_tracer.get_trace(t)
    print(trace)

    # Pour prochaine fois : Alice et Bob avec un parcours jusqu'à la solution (stateA = critic and stateB = c), vérifier
    # l'absence de deadlock, mais la présence d'un livelock.
