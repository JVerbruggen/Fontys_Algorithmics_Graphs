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
    return tops

def random_node(nodes: list[int], not_in: list[int] = []) -> int:
    working = [n for n in nodes if n not in not_in]
    return working[randrange(len(working))]

def kernalize_vertices(nodes: list[int], edges: list[(int, int)], remove_isolated = False, remove_pendant = False, remove_tops_k = -1) -> list[int]:
    result_nodes = []

    node_degrees = dict([(node, 0) for node in nodes])
    for (ea, eb) in edges:
        node_degrees[ea] += 1
        node_degrees[eb] += 1
    
    i = 0
    len_nodes= len(nodes)
    for node, degree in node_degrees.items():
        if degree == 0 and remove_isolated:
            pass
        elif degree == 1 and remove_pendant:
            pass
        elif remove_tops_k > 0 and degree > remove_tops_k:
            remove_tops_k -= 1
            pass
        elif remove_tops_k >= 0 and remove_tops_k ** 2 < len_nodes-i:
            result_nodes += ['not possible']
            break
        else:
            result_nodes += [node]

    return result_nodes