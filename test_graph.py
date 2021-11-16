from graph import *
from graph_factory import *

def test_print_matrix():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.print_matrix() != ""