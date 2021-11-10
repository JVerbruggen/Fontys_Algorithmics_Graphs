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

def test_kernalize_vertices_isolation():
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (4,7)],
        remove_isolated=True) == [1,2,3,4,5,7]
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (5,6), (6,7), (4,7)],
        remove_isolated=True) == [1,2,3,4,5,6,7]

def test_kernalize_vertices_pendant():
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (5,6), (6,7), (4,7)],
        remove_pendant=True) == [2,3,4,5,6,7,8]
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (5,6), (5,7)],
        remove_pendant=True) == [2,3,5,8]

def test_kernalize_vertices_pendant_and_isolated():
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (5,6), (6,7), (4,7)],
        remove_pendant=True, remove_isolated=True) == [2,3,4,5,6,7]
    assert kernalize_vertices(
        [1,2,3,4,5,6,7,8],
        [(1,2), (2,3), (3,4), (2,5), (5,6), (5,7)],
        remove_pendant=True, remove_isolated=True) == [2,3,5]