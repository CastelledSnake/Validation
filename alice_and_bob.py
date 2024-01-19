from graphs import RootedGraph
from semantics import Semantics


class ABNode:
    def __init__(self, name, guards, actions):
        self.name: str = name
        self.guards = guards
        self.actions = actions


class AliceAndBob(RootedGraph):
    def __init__(self):
        # Initially, nobody is in the garden.
        self.turn = 0
        # Alice and Bob don't want to go in the garden, initially.
        self.fa = False
        self.fb = False
        # Initialising all nodes
        """
        self.init_a = ABNode("Initial_Alice", "", "fA = True, turn = 2")
        self.wait_a = ABNode("Alice_Wait", "turn == 1 || fB == False", "")
        self.critic_a = ABNode("Critical_Alice", "", "fA = False")
        self.init_b = ABNode("Initial_Bob", "", "fB = True, turn = 1")
        self.wait_b = ABNode("Alice_Bob", "turn == 2 || fA == False", "")
        self.critic_b = ABNode("Critical_Bob", "", "fB = False")
        """
        self.init_a = ABNode("Initial_Alice", [True], "fA = True, turn = 2")
        self.wait_a = ABNode("Alice_Wait", [self.turn == 1 and self.fb == False], "")
        self.critic_a = ABNode("Critical_Alice", [True], "fA = False")
        self.init_b = ABNode("Initial_Bob", [True], "fB = True, turn = 1")
        self.wait_b = ABNode("Alice_Bob", [self.turn == 2 and self.fa == False], "")
        self.critic_b = ABNode("Critical_Bob", [True], "fB = False")
        # The protagonists (or their dog, or their cat, or whatever dangerous thing that should not be in a garden.
        self.alice = {self.init_a}
        self.bob = {self.init_b}

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
        if node == self.ab_graph.init_a and self.ab_graph.init_a.guards:
            return [self.ab_graph.wait_a]
        elif node == self.ab_graph.wait_a and self.ab_graph.wait_a.guards:
            return [self.ab_graph.critic_a]
        elif node == self.ab_graph.critic_a and self.ab_graph.critic_a.guards:
            return [self.ab_graph.init_a]
        elif node == self.ab_graph.init_b and self.ab_graph.init_b.guards:
            return [self.ab_graph.wait_a]
        elif node == self.ab_graph.wait_b and self.ab_graph.wait_b.guards:
            return [self.ab_graph.critic_b]
        elif node == self.ab_graph.critic_b and self.ab_graph.critic_b.guards:
            return [self.ab_graph.init_b]
        else:
            return []

    def execute(self, action, node):
        if action == self.ab_graph.wait_a:
            self.ab_graph.fa = True
            self.ab_graph.turn = 2
            self.ab_graph.alice = {action}
        elif action == self.ab_graph.critic_a:
            self.ab_graph.alice = {action}
        elif action == self.ab_graph.init_a:
            self.ab_graph.fa = False
            self.ab_graph.turn = 1
            self.ab_graph.alice = {action}
        elif action == self.ab_graph.wait_b:
            self.ab_graph.fb = True
            self.ab_graph.turn = 1
            self.ab_graph.bob = {action}
        elif action == self.ab_graph.critic_b:
            self.ab_graph.bob = {action}
        elif action == self.ab_graph.init_b:
            self.ab_graph.fb = False
            self.ab_graph.turn = 2
            self.ab_graph.bob = {action}
        else:
            return ValueError
