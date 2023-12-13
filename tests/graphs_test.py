import pytest
from graphs import HanoiNode, HanoiGraph


class TestGraphs:
    @pytest.fixture
    def setup(self):
        root = HanoiNode()  # Initialize this as per your implementation
        disks = 5
        graph = HanoiGraph(disks, root)
        return disks, root, graph

    def test_init(self, setup):
        disks, root, graph = setup
        assert graph.disks == disks
        assert graph.root == root
        assert graph.solution == tuple(2 for i in range(disks))

        # Check if graph is a dictionary
        assert isinstance(graph.graph, dict)
