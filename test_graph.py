from graph import *
from graph_factory import *

# Very good tests kappa

def test_print_matrix():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.print_matrix() != ""

def test_connect():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.connect() == None

def test_find_subgraphs():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert len(graph.find_subgraphs()) > 0

def test_remove_tops():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.remove_tops(3) == None

def test_add_tops():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.add_tops(3) == None

def test_add_pendant():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.add_pendant() == None

def test_remove_pendant():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert graph.remove_pendant() == None

def test_get_color_map():
    graph = GraphFactory.generate_networkx_matrix(3, 0.8)

    assert len(graph.get_color_map(2)) == 3