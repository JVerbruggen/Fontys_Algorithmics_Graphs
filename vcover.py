def validate_vcover(nodes: list[int], edges: list[(int, int)], cover: list[bool], n: int, k: int) -> bool:
    vertices_used = sum(cover)
    if vertices_used != k:
        return False
    
    covered_nodes = [nodes[i] for i in range(len(nodes)) if cover[i]]

    for node in covered_nodes:
        edges_covered = [(va, vb) for (va, vb) in edges if va == node or vb == node]
        edges = [e for e in edges if e not in edges_covered]

    return len(edges) == 0

def find_vcovers(nodes: list[int], edges: list[(int, int)], cover: list[bool], n: int, i: int, k: int, lambd_a): 
    lambd_a(1) # Progress bar increment
    if n == i:
        valid = validate_vcover(nodes[:], edges[:], cover, n, k)
        if valid:
            return [[nodes[i] for i in range(len(nodes)) if cover[i]]]
        return None
    else:
        vertices_used = sum(cover)
        if vertices_used > k:
            return None

        possible_covers = []

        cover[i] = False
        cover_false = find_vcovers(nodes, edges, cover[:], n, i+1, k, lambd_a)
        if cover_false != None:
            possible_covers += cover_false

        cover[i] = True
        cover_true = find_vcovers(nodes, edges, cover[:], n, i+1, k, lambd_a)
        if cover_true != None:
            possible_covers += cover_true

        return possible_covers

