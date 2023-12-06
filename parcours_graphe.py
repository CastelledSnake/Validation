def read_graph(graph: list):
    """
    Reads a graph, which is supposed to be a list of lists of ...
    The value of a node must be integer, float or string.
    :param graph: The graph.
    :return: A string explicating the graph.
    """
    if not graph:  # Empty graph.
        return "()"

    elif type(graph) is not list:  # The graph is a single leaf.
        return f"{graph}"

    elif len(graph) == 1:  # The graph is a branch with a single leaf.
        return f"node({graph[0]})"

    else:  # The graph is more complex...
        output = ""

        if type(graph[0]) in [int, float, str]:  # Each node must have a value.
            output += f"node({graph[0]}), "
        else:
            raise TypeError(f"The value of node {graph[0]} must be integer, float or string, not {type(graph[0])}")

        for branch in graph[1:]:  # Parsing each branch until the end of the graph.
            if type(branch) in [int, float, str]:  # The branch was a leaf.
                output += f"node({branch}), "
            elif type(branch) is list:  # The branch has leaves.
                output += f"children[{read_graph(branch)}], "
            else:
                raise TypeError(f"{type(branch)} is not a proper type for this graph.")

        return output[:-2]  # We erase the last ", " characters in the output.


def nice_graph(graph: list, result: str = "", indent: int = 0):
    """
    Reads a graph, which is supposed to be a list of lists of ...
    The value of a node must be integer, float or string.
    :param graph: The graph.
    :param result: The string which prints the graph.
    :param indent: The number of periods to insert before each node, to return a proper graph.
    :return: A nice print of the graph.
    """
    if not graph:  # Empty graph.
        result += "¤"

    elif type(graph) is not list:  # The graph is a single leaf.
        result += f"{graph}"

    elif len(graph) == 1:  # The graph is a branch with a single leaf.
        result += f"{graph[0]}"

    else:  # The graph is more complex...
        output = ""

        if type(graph[0]) in [int, float, str]:  # Each node must have a value.
            output += f"{graph[0]}|\n"
            indent += len(str(graph[0]))
        else:
            raise TypeError(f"The value of node {graph[0]} must be integer, float or string, not {type(graph[0])}")

        for k in range(indent):
            output += ' '
        output += "|\n"
        for k in range(indent):
            output += ' '

        for branch in graph[1:]:  # Parsing each branch until the end of the graph.
            if type(branch) in [int, float, str]:  # The branch was a leaf.
                output += f"{branch}-"
            elif type(branch) is list:  # The branch has leaves.
                output += f"{nice_graph(branch, result, indent)}-"
            else:
                raise TypeError(f"{type(branch)} is not a proper type for this graph.")

        result += output  # We erase the last ", " characters in the output.
    return result


if __name__ == "__main__":
    graphe_vide = []
    graphe_0 = [0]
    graphe_1 = [0, [1, [2]]]
    graphe_2 = [0, [1, 2, 3]]
    graphe_3 = ["bla", [], ["bleble", ["bliblibli", "bloblo"], "blu"]]

    print(read_graph(graphe_vide))
    print(read_graph(graphe_0))
    print(read_graph(graphe_1))
    print(read_graph(graphe_2))
    print(read_graph(graphe_3))

    print(nice_graph(graphe_3))
