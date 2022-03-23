import typing as ty
import unittest
from collections import deque


def is_route_dfs(graph: ty.Dict[str, list], start: str, end: str) -> bool:
    visited = set()
    # using a stack
    st = [start]
    while len(st) > 0:
        node = st.pop()
        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                if adj == end:
                    return True
                st.append(adj)
    return False


def is_route_bfs(graph: ty.Dict[str, list], start: str, end: str) -> bool:
    visited = set()
    # using a queue
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                if adj == end:
                    return True
                queue.append(adj)
    return False


class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route_dfs(self.graph, start, end)
            assert actual == expected

    def test_is_route_bfs(self):
        for i, (start, end, expected) in enumerate(self.tests):
            with self.subTest(f"start = {start}, end = {end}", i=i):
                actual = is_route_bfs(self.graph, start, end)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
