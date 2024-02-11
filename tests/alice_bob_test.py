"""
    3 premières versions du TD vérification
"""
import sys

sys.path.append("src")
from alice_and_bob import AliceAndBob, AliceBobV1_Semantics
from graph.breadth_first_search import bfs
from graph.parent_tracer import ParentTracer
from old_code.semantics import SemToRG


class TestAliceBobV1:
    def setup(self):
        self.alice_and_bob = AliceAndBob()

    def test_alice_bob_graph(self):
        pass

    def test_alice_bob_semantics(self):
        alice_and_bob = SemToRG(AliceBobV1_Semantics())

        parents = ParentTracer(alice_and_bob)
        target, visited = bfs(parents, lambda config: config == ("C", "C"))
        print("SEARCH target found", target)
        print("SEARCH visited", visited)
        if target is not None:
            print("TRACE", parents.get_trace(target))
        else:
            print("TRACE target is None")

    def test_alice_bob_soup(self):
        pass


class TestAliceBobV2:
    def test_alice_bob_graph(self):
        pass

    def test_alice_bob_semantics(self):
        pass

    def test_alice_bob_soup(self):
        pass


class TestAliceBobV3:
    def test_alice_bob_graph(self):
        pass

    def test_alice_bob_semantics(self):
        pass

    def test_alice_bob_soup(self):
        pass
