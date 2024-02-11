from alice_and_bob import AliceBobV1_Semantics, AliceBobV2_Semantics, AliceBobV3_Semantics
from graph.breadth_first_search import bfs
from graph.parent_tracer import ParentTracer
from graphs import bfs_search
from hanoi import HanoiGraph
from old_code.semantics import SemToRG

def alice_et_bob_semantics_execution(a_and_b):
    parents = ParentTracer(a_and_b)
    target, visited = bfs(parents, lambda config: config == ("C", "C"))
    print("SEARCH target found", target)
    print("SEARCH visited", visited)
    if target is not None:
        print("TRACE", parents.get_trace(target))
    else:
        print("TRACE target is None")

if __name__ == "__main__":
    # rg = RootedGraph({1: [2, 3], 2: [3, 4], 3: [], 4: []}, 1)
    # def a(n: Node) -> bool:
    #     return n == 2

    # def b(n: Node) -> bool:
    #     return n == 5

    # print(bfs_search(rg, a))
    # print(bfs_search(rg, b))

    ##### Hanoi #####
    #hanoi = HanoiGraph(2, (0, 0))
    hanoi = HanoiGraph(3, (0, 0, 0))
    parent_tracer = ParentTracer(hanoi)
    t, k = bfs_search(parent_tracer, hanoi.is_solution)
    print("t: ", t, "\nk: ", k)
    trace = parent_tracer.get_trace(t)
    print("\n trace: ", trace)
    print("neighbours: ", hanoi.neighbours((0, 0, 0)))

    # Pour prochaine fois : Alice et Bob avec un parcours jusqu'à la solution (stateA = critic and stateB = c), vérifier
    # l'absence de deadlock, mais la présence d'un livelock.

    ###### Alice Bob V1 ######
    a_and_b = SemToRG(AliceBobV1_Semantics())
    alice_et_bob_semantics_execution(a_and_b)

    ###### Alice Bob V2 ######
    a_and_b = SemToRG(AliceBobV2_Semantics())
    alice_et_bob_semantics_execution(a_and_b)

    ###### Alice Bob V3 ######
    a_and_b = SemToRG(AliceBobV3_Semantics())
    alice_et_bob_semantics_execution(a_and_b)

