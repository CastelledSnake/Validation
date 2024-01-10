from graphs import *
from semantics import *


class ABNode:
    def __init__(self, name, guards, actions):
        self.name: str = name
        self.guards = guards
        self.actions = actions


class AliceAndBob(RootedGraph):
    def __init__(self):
        # The protagonists (or their dog, or their cat, or whatever dangerous thing that should not be in a garden.
        self.alice = {}
        self.bob = {}
        # Initially, nobody is in the garden.
        self.turn = 0
        # Alice and Bob don't want to go in the garden, initially.
        self.fa = False
        self.fb = False
        # Initialising all nodes
        self.init_a = ABNode("Initial_Alice", "", "fA = True, turn = 2")
        self.wait_a = ABNode("Alice_Wait", "turn == 1 || fB == False", "")
        self.critic_a = ABNode("Critical_Alice", "", "fA = False")
        self.init_b = ABNode("Initial_Bob", "", "fB = True, turn = 1")
        self.wait_b = ABNode("Alice_Bob", "turn == 2 || fA == False", "")
        self.critic_b = ABNode("Critical_Bob", "", "fB = False")

    def filling(self):
        """
        Fills alice and bob
        :return: None
        """
        self.alice = {
            self.init_a: [self.wait_a],
            self.wait_a: [self.critic_a],
            self.critic_a: [self.init_a]
        }
        self.bob = {
            self.init_b: [self.wait_b],
            self.wait_b: [self.critic_b],
            self.critic_b: [self.init_b]}

    def roots(self):
        return [self.init_a, self.init_b]

    def neighbours(self, node):
        if node in self.alice:
            return self.alice[node]
        elif node in self.bob:
            return self.bob[node]
        else:
            raise ValueError(f"Node {node} is not in alice or bob")
    # IDEA : Define one function per action to perform, and per guard to test (8 of them in total).


class AliceAndBobExecution(Semantics):
    def __init__(self):
        self.ab_graph = AliceAndBob()

    def initial(self):
        return [self.ab_graph.init_a, self.ab_graph.init_b]

    def actions(self, node):
        return node.actions

    def execute(self, action, node):
        pass
