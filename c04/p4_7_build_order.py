from tkinter import N
import typing as ty


def main():
    projects = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # dependencies = [
    #     ("a", "d"),
    #     ("f", "b"),
    #     ("b", "d"),
    #     ("f", "a"),
    #     ("d", "c"),
    # ]
    dependencies = [
        ("f", "c"),
        ("f", "b"),
        ("f", "a"),
        ("d", "g"),
        ("c", "a"),
        ("b", "a"),
        ("b", "h"),
        ("b", "e"),
        ("a", "e")
    ]
    print(build_order(projects, dependencies))


def build_order(projects: ty.List, dependencies: ty.List[ty.Tuple]):
    """print the build order

    Args:
        projects: list of projects
        dependencies: list of tuples (first, second) -> first must be done
            first before second
    """
    graph = build_graph(projects, dependencies)
    out = []
    order_projects(graph, out)
    return out


def build_graph(projects, dependencies):
    graph = Graph(projects=projects)
    for neighbour, node in dependencies:
        graph.add_edge(node=node, neighbour=neighbour)
    return graph


def order_projects(graph: "Graph", out: ty.List):
    nodes_with_no_endges = graph.get_nodes_with_no_incoming_edges()
    print(f"nodes_with_no_endges={nodes_with_no_endges}")
    if len(nodes_with_no_endges) == 0:
        return
    out.extend(nodes_with_no_endges)
    for node in nodes_with_no_endges:
        graph.remove_from_neighbours(node)
    graph.remove_nodes(nodes_with_no_endges)
    return order_projects(graph, out)

class Graph:
    def __init__(self, projects):
        self.adjacency_list = {k: set() for k in projects}

    def add_edge(self, node, neighbour):
        neighbours = self.adjacency_list.get(node, set())
        neighbours.add(neighbour)

    def get_nodes_with_no_incoming_edges(self)-> ty.List:
        out = []
        for k, v in self.adjacency_list.items():
            if len(v) == 0:
                out.append(k)
        return out

    def remove_edge(self, node, neighbour):
        neighbours = self.adjacency_list.get(node, set())
        if neighbour in neighbours:
            neighbours.remove(neighbour)

    def remove_from_neighbours(self, neighbour):
        for _, neighbours in self.adjacency_list.items():
            if neighbour in neighbours:
                neighbours.remove(neighbour)

    def remove_nodes(self, nodes: ty.List):
        for node in nodes:
            self.adjacency_list.pop(node)

