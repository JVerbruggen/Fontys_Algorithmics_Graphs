from vertex_manipulations import *

def test_degree():
    assert degree(3, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == 1
    assert degree(4, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == 2
    assert degree(1, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == 3
    assert degree(6, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == 0

def test_find_adjacent_nodes():
    assert find_adjacent_nodes(3, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == [1]
    assert find_adjacent_nodes(4, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == [2,5]
    assert find_adjacent_nodes(1, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == [3,2,0]
    assert find_adjacent_nodes(6, [(3,1), (1,2), (1,0), (2,4), (4,5)]) == []

def test_random_node():
    assert random_node([1,2,3,4]) in [1,2,3,4]
    assert random_node([1,2,3,4]) in [1,2,3,4]
    assert random_node([1,2,3,4]) in [1,2,3,4]
    assert random_node([1,2,3,4]) in [1,2,3,4]

    assert random_node([1,2,3,4], not_in=[1,2]) in [3,4]
    assert random_node([1,2,3,4], not_in=[1,2]) in [3,4]
    assert random_node([1,2,3,4], not_in=[1,2]) in [3,4]
    assert random_node([1,2,3,4], not_in=[1,2]) in [3,4]

def test_kernalize_vertices():
    (kernalized_vertices, kernalized_edges, sure_in_cover, k) = kernalize_vertices(
        [1,2,3,4,5],
        [(1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,5), (3,4), (4,5)], k=3)

    assert sure_in_cover == [1,3,5]
    assert kernalized_vertices == []
    assert kernalized_edges == []
    assert k == 0

    (kernalized_vertices, kernalized_edges, sure_in_cover, k) = kernalize_vertices(
        [1,2,3,4,5],
        [(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,5), (3,4), (4,5)], k=3)

    assert sure_in_cover == None
    assert kernalized_vertices == None
    assert kernalized_edges == None
    assert k == None

    (kernalized_vertices, kernalized_edges, sure_in_cover, k) = kernalize_vertices(
        [0,1,2,3,4,5,6],[(0,2),(0,3),(0,6),(0,1),(1,2),(1,3),(1,6),(1,4),(1,5),(2,3),(2,6),(3,6),(4,6),(5,6)], k=4)

    assert sure_in_cover == [1,6]
    assert kernalized_vertices == [0,2,3]
    assert kernalized_edges == [(0,2),(0,3),(2,3)]
    assert k == 2
    
