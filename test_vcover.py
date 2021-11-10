from vcover import *
import networkx as nx

def test_validate_vcover():
    assert validate_vcover([1,2,3], [(1,2)], [False, True, True], 3, 2) == True

def test_find_vcovers():
    # assert find_vcover([1,2,3], [(1,2)], [False, False, False], n=3, i=0, k=2)
    assert len(find_vcovers([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False for _ in range(4)], 4, 0, 3, lambda _ : 0)) == 4
    assert len(find_vcovers([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False for _ in range(4)], 4, 0, 2, lambda _ : 0)) == 1
    assert len(find_vcovers([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False for _ in range(4)], 4, 0, 1, lambda _ : 0)) == 0

