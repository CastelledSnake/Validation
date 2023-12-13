class RootedGraph:
    def __init__(self, graph: dict):
        self.racine = 1
        self.struct: dict = graph

    def root(self):
        return self.racine

    def neighbours(self, node):
        return self.struct[node]

    def parents_graph(self):
        parents_graph = RootedGraph({})
        for node in self.struct:
            if node not in parents_graph.struct:
                parents_graph.struct[node] = []
            children = self.neighbours(node)
            for child in children:
                if child in parents_graph.struct:
                    parents_graph.struct[child].append(node)
                else:
                    parents_graph.struct[child] = [node]
        return parents_graph


def bfs_traversal(rg, query=0):
    i = True  # Variable de commencement
    f = []  # Frontière : liste des nœuds connus, mais pas explorés.
    k = ()  # Ensemble des nœuds déjà parcourus.
    while f != [] or i:
        if i:
            node = rg.root()
            f = rg.neighbours(node)
            k = k + (node,)
            i = False
        else:
            node = f.pop(0)
        for voisin in rg.neighbours(node):
            if voisin not in k:
                k = k + (voisin,)
                if voisin == query:
                    return k
    return k


# Pour les tours de Hanoï, la situation peut être représentée par un graphe.
# Chaque nœud est une disposition possible du plateau. Pour un jeu à N disques de taille variant de 1 à N (u.a.) :
#   Un nœud a pour nom (clé primaire) un ensemble de N lettres entre A, B et C tel que :
#       la lettre en position n in range(1, N+1) est la colonne du disque de taille n.
# En tentant de relier les nœuds entre eux, on obtiendra la forme d'un triangle de Pascal.
# Condition pour passer d'un état à un autre ⇔ changer la lettre du nom qui est en position n de X à Y :
#   Aucun disque n'est présent au-dessus du disque n ⇔ aucune lettre d'indice <n ne vaut X.
#   S'il existe un disque sur la position cible, il doit être plus grand que n ⇔ aucune lettre d'indice <n ne vaut Y.
# Il y a au maximum 3 possibilités :
#   déplacer le disque le plus petit d'une tour vers une des deux autres (2 possibilités);
#   si l'un au moins l'une des deux autres colonnes supporte un disque :
#       déplacer le disque surfacique le plus léger (après LE plue léger) sur la colonne dont le disque surfacique est
#       plus lourd (ou qui est vide).


class HanoiConfig:
    def __init__(self, string: str):
        for char in string:
            if char not in ['A', 'B', 'C']:
                raise TypeError("There are 3 positions in Hanoi Towers : A, B and C.")
        self.configuration = string

    def __repr__(self):
        return self.configuration


class HanoiRGraph:
    def __init__(self, n: int):
        root, final = "", ""
        for k in range(n):
            root += "A"
            final += "C"
        self.root = HanoiConfig(root)
        self.final = HanoiConfig(final)
        self.graph = {self.root: []}

    def neighbours(self, state: str):
        previous_discs = [False, False, False]
        new_solutions = []
        for disc in state:
            if disc == 'A':
                previous_discs[0] = True
                if not previous_discs[1]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'B' + state[state.index(disc)+1:])
                if not previous_discs[2]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'C' + state[state.index(disc) + 1:])
            elif disc == 'B':
                previous_discs[1] = True
                if not previous_discs[0]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'A' + state[state.index(disc)+1:])
                if not previous_discs[2]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'C' + state[state.index(disc)+1:])
            else:
                previous_discs[2] = True
                if not previous_discs[0]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'A' + state[state.index(disc)+1:])
                if not previous_discs[1]:
                    new_solutions.append(
                        state[:state.index(disc)] + 'B' + state[state.index(disc)+1:])
            if len(new_solutions) == 3:
                break
        return list(set(new_solutions))

    def is_solution(self, n: int):
        new_confs = [self.root]
        iter_limit = 0
        self.graph = {}
        while (self.final.configuration not in self.graph) and (iter_limit < n) :
            studied_conf = new_confs.pop(0)
            if studied_conf.configuration not in self.graph:
                self.graph[studied_conf.configuration] = []
                new_sols = self.neighbours(studied_conf.configuration)
                for k in range(len(new_sols)):
                    new_neighbour = HanoiConfig(new_sols[k])
                    new_confs.append(new_neighbour)
                    self.graph[studied_conf.configuration].append(new_neighbour.configuration)
                    if new_neighbour.configuration in self.graph:
                        if studied_conf.configuration not in self.graph[new_neighbour.configuration]:
                            self.graph[studied_conf.configuration].append(new_neighbour.configuration)
                        # else:
                        #    print(f"{self.graph[new_neighbour.configuration]} possède déjà {studied_conf}")
            iter_limit += 1
        return self.graph


if __name__ == "__main__":
    struct_graph_1 = {1: [2, 3], 2: [3, 4], 3: [1], 4: []}
    rooted_graph_1 = RootedGraph(struct_graph_1)

    print(bfs_traversal(rooted_graph_1))
    print(rooted_graph_1)
    print(bfs_traversal(rooted_graph_1.parents_graph()))
    #hg_init = HanoiRGraph(3)
    #print(hg_init.is_solution(100))
