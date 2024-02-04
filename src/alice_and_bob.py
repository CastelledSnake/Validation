from typing import Iterable
from graph.rooted_graph import RootedGraph
from old_code.semantics import Semantics


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
        # Defining all nodes
        self.init_a = ABNode("Initial_Alice", self.guard_i_a, self.action_i_a)
        self.wait_a = ABNode("Alice_Wait", self.guard_w_a, self.action_w_a)
        self.critic_a = ABNode("Critical_Alice", self.guard_c_a, self.action_c_a)
        self.init_b = ABNode("Initial_Bob", self.guard_i_b, self.action_i_b)
        self.wait_b = ABNode("Alice_Bob", self.guard_w_b, self.action_w_b)
        self.critic_b = ABNode("Critical_Bob", self.guard_c_b, self.action_c_b)
        # The protagonists (or their dog, or their cat, or whatever dangerous thing that should not be in a garden.
        self.alice, self.bob = self.filling()

    # Set of guards
    def guard_i_a(self):
        return True

    def guard_w_a(self):
        return self.turn == 1 and self.fa is False

    def guard_c_a(self):
        return True

    def guard_i_b(self):
        return True

    def guard_w_b(self):
        return self.turn == 2 and self.fb is False

    def guard_c_b(self):
        return True

    # Set of actions
    def action_i_a(self):
        self.fa = True
        self.turn = 2

    def action_w_a(self):
        pass

    def action_c_a(self):
        self.fa = False

    def action_i_b(self):
        self.fb = True
        self.turn = 1

    def action_w_b(self):
        pass

    def action_c_b(self):
        self.fb = False

    def filling(self):
        """
        Fills alice and bob
        """
        alice = {
            self.init_a: [self.wait_a],
            self.wait_a: [self.critic_a],
            self.critic_a: [self.init_a],
        }
        bob = {
            self.init_b: [self.wait_b],
            self.wait_b: [self.critic_b],
            self.critic_b: [self.init_b],
        }
        return alice, bob

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


class AliceBobV1_Graph(RootedGraph):
    def __init__(self) -> None:
        pass

    def roots(self):
        return []

    def neighbours(self, node) -> Iterable:
        return []


class AliceBobV1_Semantics(Semantics):
    def initial(self):
        return [("I", "I")]

    def actions(self, configuration):
        actions = []
        if configuration[0] == "I":
            actions.append(lambda c: [("W", configuration[1])])
