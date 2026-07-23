import pytest

from Graph import Graph
from ColoredGraph import ColoredGraph
from GraphItem import GraphItem
from Vertex import Vertex


class TestVertex:
    def test_vertex_adjacency_and_degree(self):
        vertex = Vertex(vertexLabel="A", metadata={"value": 1}, labels={"group": "x"})
        assert vertex.getVertexLabel() == "A"
        assert vertex.getDegree() == 0
        assert not vertex.isAdjacent("B")

        vertex.addAdjacency("B")
        assert vertex.isAdjacent("B")
        assert vertex.getDegree() == 1
        assert vertex.getAdjacencies() == {"B"}

    def test_vertex_repr_contains_metadata_and_labels(self):
        vertex = Vertex(vertexLabel="A", metadata={"value": 7}, labels={"group": "x"})
        text = repr(vertex)
        assert "vertex A" in text
        assert "metadata:{'value': 7}" in text
        assert "labels:{'group': 'x'}" in text


class TestGraph:
    @pytest.fixture
    def items(self):
        return [
            GraphItem("A", {"value": 1}, {"group": "x"}),
            GraphItem("B", {"value": 2}, {"group": "x"}),
            GraphItem("C", {"value": 3}, {"group": "y"}),
        ]

    def test_graph_builds_vertices_and_undirected_edges(self, items):
        graph = Graph(items, connections=[("A", "B")])
        assert graph.getVertex("A").isAdjacent("B")
        assert graph.getVertex("B").isAdjacent("A")
        assert not graph.getVertex("A").isAdjacent("C")

    def test_add_directed_edge_is_not_bidirectional(self, items):
        graph = Graph(items)
        graph.addDirectedEdge("A", "C")
        assert graph.getVertex("A").isAdjacent("C")
        assert not graph.getVertex("C").isAdjacent("A")

    def test_connect_by_labels_links_vertices_with_same_label_value(self, items):
        graph = Graph(items)
        graph.connectByLabels("group")
        assert graph.getVertex("A").isAdjacent("B")
        assert graph.getVertex("B").isAdjacent("A")
        assert not graph.getVertex("A").isAdjacent("C")

    def test_get_vertex_returns_correct_vertex(self, items):
        graph = Graph(items)
        vertex = graph.getVertex("C")
        assert vertex.getVertexLabel() == "C"
        assert vertex.metadata == {"value": 3}
        assert vertex.labels == {"group": "y"}


class TestColoredGraph:
    def test_chromatic_number_defaults_to_max_degree_plus_one(self):
        items = [
            GraphItem("A", {}, {}),
            GraphItem("B", {}, {}),
            GraphItem("C", {}, {}),
        ]
        graph = ColoredGraph(items, connections=[("A", "B"), ("B", "C")])
        assert graph.numColors == 3

    def test_color_graph_assigns_valid_colors(self):
        items = [
            GraphItem("A", {}, {}),
            GraphItem("B", {}, {}),
            GraphItem("C", {}, {}),
        ]
        graph = ColoredGraph(items, connections=[("A", "B"), ("B", "C"), ("A", "C")])
        graph.colorGraph()

        colors = {v.getVertexLabel(): v.color for v in graph.vertices.values()}
        assert all(color != -1 for color in colors.values())
        assert colors["A"] != colors["B"]
        assert colors["B"] != colors["C"]
        assert colors["A"] != colors["C"]

    def test_color_graph_balanced_uses_available_colors(self):
        items = [
            GraphItem("A", {}, {}),
            GraphItem("B", {}, {}),
            GraphItem("C", {}, {}),
            GraphItem("D", {}, {}),
        ]
        graph = ColoredGraph(items, connections=[("A", "B"), ("B", "C"), ("C", "D")], numColors=2)
        graph.colorGraphBalanced()

        assert graph.colorUsage[0] + graph.colorUsage[1] == 4
        assert graph.getVertex("A").color in {0, 1}
        assert graph.getVertex("A").color != graph.getVertex("B").color
        assert graph.getVertex("B").color != graph.getVertex("C").color
        assert graph.getVertex("C").color != graph.getVertex("D").color
        assert abs(graph.colorUsage[0] - graph.colorUsage[1]) <= 1

    def test_color_groups_record_assigned_vertices(self):
        items = [
            GraphItem("A", {}, {}),
            GraphItem("B", {}, {}),
        ]
        graph = ColoredGraph(items, connections=[("A", "B")], numColors=2)
        graph.colorGraph()
        assert sorted(graph.colorGroups[graph.getVertex("A").color]) == ["A"]
        assert sorted(graph.colorGroups[graph.getVertex("B").color]) == ["B"]
