from vcover import *
import networkx as nx

def test_validate_vcover():
    assert validate_vcover([1,2,3], [(1,2)], [False, True, True], 3, 2) == True

def test_find_vcovers():
    assert len(find_vcovers_brute([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 3, lambda _,x : None, lambda _ : None)) == 4
    assert len(find_vcovers_brute([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 2, lambda _,x : None, lambda _ : None)) == 1
    assert len(find_vcovers_brute([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], 4, 1, lambda _,x : None, lambda _ : None)) == 0

def test_find_vcovers_enhanced():
    assert find_vcovers_brute([0,1,2,3,4,5,6],[(0,2),(0,3),(0,6),(0,1),(1,2),(1,3),(1,6),(1,4),(1,5),(2,3),(2,6),(3,6),(4,6),(5,6)],
        7, 4, lambda _,x : None, lambda _ : None)[0] == [0,1,2,6]

    assert find_vcovers_enhanced([0,1,2,3,4,5,6],[(0,2),(0,3),(0,6),(0,1),(1,2),(1,3),(1,6),(1,4),(1,5),(2,3),(2,6),(3,6),(4,6),(5,6)],
        7, 4, lambda _,x : None, lambda _ : None)[0] == [0,1,2,6]
