import pytest
import sys

sys.path.append("src")
from src.graph.breadth_first_search import bfs
from src.graph.parent_tracer import ParentTracer
from src.hanoi import HanoiGraph


class TestHanoiGraph:
    @pytest.fixture
    def setup(self):
        self.hanoi_graph = HanoiGraph(3, (0, 0, 0))
        self.parent_tracer = ParentTracer(self.hanoi_graph)

    def test_roots(self, setup):
        assert self.hanoi_graph.roots() == [(0, 0, 0)]

    def test_is_solution(self, setup):
        assert self.hanoi_graph.is_solution((2, 2, 2)) is True
        assert self.hanoi_graph.is_solution((0, 0, 0)) is False

    def test_neighbours(self, setup):
        neighbours = self.hanoi_graph.neighbours((0, 0, 0))
        expected_neighbours = [(1, 0, 0), (2, 0, 0)]
        assert set(neighbours) == set(expected_neighbours)

    def test_graph(self, setup):
        t, k = bfs(self.parent_tracer, self.hanoi_graph.is_solution)
        trace = self.parent_tracer.get_trace(t)
        assert trace[0] == (2, 2, 2)  # The last state should be the solution state


class TestHanoiSemantics:
    def test_semantics(self):
        raise NotImplementedError


class TestHanoiSoup:
    def test_soup(self):
        raise NotImplementedError
