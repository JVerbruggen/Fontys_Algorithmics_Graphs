from graph import LabGraph
import random

class GraphFactory:
    def generate_networkx_matrix(n: int, p: float) -> LabGraph:
        G = LabGraph()

        for i in range(n):
            G.add_node(i)

        nodes = G.nodes()
        nodes_len = len(nodes)
        for i in range(nodes_len):
            edges = [(i, j) for j in range(i+1, nodes_len) if random.random() <= p]
            G.add_edges_from(edges)

        return G
