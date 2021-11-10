from random import randrange

def degree(node: int, edges: list[(int, int)]) -> int:
    deg = 0
    for (ea, eb) in edges:
        if ea == node:
            deg += 1
        if eb == node:
            deg += 1
    return deg

def find_adjacent_nodes(node: int, edges: list[(int, int)]) -> list[int]:
    nodes = []

    for (ea, eb) in edges:
        if ea == node:
            nodes += [eb]
        if eb == node:
            nodes += [ea]

    return nodes

def find_isolated_nodes(nodes: list[int], edges: list[(int, int)]) -> list[int]:
    isolated = []
    for node in nodes:
        if degree(node, edges) == 0:
            isolated += [node]
    return isolated

def find_pendant_nodes(nodes: list[int], edges: list[(int, int)]) -> list[int]:
    pendant = []
    for node in nodes:
        if degree(node, edges) == 1:
            pendant += [node]
    return pendant

def find_tops_nodes(nodes: list[int], edges: list[(int, int)], k: int) -> list[int]:
    tops = []
    for node in nodes:
        if degree(node, edges) > k:
            tops += [node]
            k -= 1
    return tops

def random_node(nodes: list[int], not_in: list[int] = []) -> int:
    working = [n for n in nodes if n not in not_in]
    return working[randrange(len(working))]

def remove_edges_for(node: int, edges: list[(int, int)]) -> list[(int, int)]:
    return [(ea, eb) for (ea, eb) in edges if ea != node and eb != node]

def kernalize_vertices(nodes: list[int], edges: list[(int, int)], k, rlog=False) -> (list[int], list[(int, int)]):
    result_nodes = nodes[:]
    result_edges = edges[:]
    nodes_surely_in_cover = []

    i = 0
    len_nodes = len(nodes)
    looping = True
    log = ""

    while looping:
        log += str(result_nodes) + f"; k={k}\n"
        looping = False
        for node in result_nodes:
            deg = degree(node, result_edges)
            if k > 0 and deg > k:
                k -= 1
                nodes_surely_in_cover += [node]
                result_nodes.remove(node)
                result_edges = remove_edges_for(node, result_edges)
                looping = True
            elif deg == 0:
                result_nodes.remove(node)
                looping = True
        if looping == False and len(result_edges) > k ** 2:
            result_nodes = result_edges = nodes_surely_in_cover = None
            break
    if rlog: return log

    if result_nodes is None:
        return (None, None, None)

    return (result_nodes, result_edges, sorted(nodes_surely_in_cover))