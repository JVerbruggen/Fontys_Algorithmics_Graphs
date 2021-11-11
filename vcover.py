from vertex_manipulations import *

def validate_vcover(nodes: list[int], edges: list[(int, int)], cover: list[bool], n: int, k: int) -> bool:
    vertices_used = sum(cover)
    if vertices_used != k:
        return False
    
    covered_nodes = [nodes[i] for i in range(len(nodes)) if cover[i]]

    for node in covered_nodes:
        edges_covered = [(va, vb) for (va, vb) in edges if va == node or vb == node]
        edges = [e for e in edges if e not in edges_covered]

    return len(edges) == 0

def find_vcovers_brute(nodes: list[int], edges: list[(int, int)], n: int, k: int, pbar_incr, pbar_desc):
    cover = [False for _ in range(n)]
    i=0
    pbar_desc("Calculating cover... (Brute)")
    return find_vcovers(nodes, nodes, edges, edges, cover, n,i, k, pbar_incr)

def find_vcovers_enhanced(nodes: list[int], edges: list[(int, int)], n: int, k: int, pbar_incr, pbar_desc):
    pbar_desc("Kernalizing... (Enhanced)")
    (ns, es, nodes_in_cover, k) = kernalize_vertices(nodes, edges, k=k)
    if ns == None:
        return None
    
    i=0
    n = len(ns)
    cover = [False for _ in range(n)]

    pbar_desc("Calculating cover... (Enhanced)")
    vcovers = find_vcovers(ns, nodes, es, edges, cover, n, i, k, pbar_incr)

    for i in range(len(vcovers)):
        vcover = vcovers[i]
        vcover += nodes_in_cover
        vcovers[i] = sorted(vcover)

    return vcovers

def find_vcovers(nodes: list[int], nodes_to_cover: list[int], edges: list[(int, int)], edges_to_cover: list[(int, int)], cover: list[bool], n: int, i: int, k: int, pbar_incr): 
    pbar_incr(1)
    if n == i:
        valid = validate_vcover(nodes[:], edges[:], cover, n, k)
        if valid:
            vc = [[nodes[j] for j in range(len(nodes)) if cover[j]]]
            return vc
        return None
    else:
        vertices_used = sum(cover)
        if vertices_used > k:
            return None

        possible_covers = []

        cover[i] = False
        cover_false = find_vcovers(nodes, nodes_to_cover, edges, edges_to_cover, cover[:], n, i+1, k, pbar_incr)
        if cover_false != None:
            possible_covers += cover_false

        cover[i] = True
        cover_true = find_vcovers(nodes, nodes_to_cover, edges, edges_to_cover, cover[:], n, i+1, k, pbar_incr)
        if cover_true != None:
            possible_covers += cover_true

        return sorted(possible_covers)

