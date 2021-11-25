from vcover_algorithms import *
import networkx as nx


def test_binary_algorithms():
    nodes = [0,1,2,3]
    edges = [(0,2),(0,3),(2,3),(1,2),(1,3)]
    n = 4
    cover = [False for _ in range(n)]
    k = 3

    assert len(BinaryVCoverAlgorithm().find_vcovers_binary(nodes, nodes, edges, edges, cover, n, 0, k, lambda _ : None, lambda _ : None)) == 4

def test_find_vcovers_brute():
    assert len(VCoverBruteForce([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 3, lambda _ : None, lambda _ : None).find_vcovers()) == 4
    assert len(VCoverBruteForce([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 2, lambda _ : None, lambda _ : None).find_vcovers()) == 1
    assert len(VCoverBruteForce([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 1, lambda _ : None, lambda _ : None).find_vcovers()) == 0

def test_find_vcovers_enhanced():
    vcovers = VCoverEnhanced([0,1,2,3,4,5,6],[(0,2),(0,3),(0,6),(0,1),(1,2),(1,3),(1,6),(1,4),(1,5),(2,3),(2,6),(3,6),(4,6),(5,6)],
        4, lambda _ : None, lambda _ : None).find_vcovers()
    assert vcovers[0] == [0,1,2,6]

    vcovers = VCoverEnhanced([0,1,2,3,4,5,6],[(0,2),(0,3),(0,6),(0,1),(1,2),(1,3),(1,6),(1,4),(1,5),(2,3),(2,6),(3,6),(4,6),(5,6)],
        4, lambda _ : None, lambda _ : None).find_vcovers()
    assert vcovers[0] == [0,1,2,6]

def test_find_vcovers_take2():
    vcovers = VCoverTakeTwo([(0,2),(0,3),(1,3),(1,2),(4,0)]).find_vcovers()
    assert len(vcovers) == 1
    assert len(vcovers[0]) == 6

def test_find_vcovers_greedy():
    vcovers = VCoverGreedy([(0,2),(0,3),(1,3),(1,2),(4,0)]).find_vcovers()
    assert vcovers[0] == [0, 1]