from vcover_validation import *
from vertex_manipulations import *

class VCoverAlgorithm:
    def find_vcovers(self):
        raise NotImplementedError()

class BinaryVCoverAlgorithm(VCoverAlgorithm):
    def find_vcovers_binary(self, nodes: list[int], nodes_to_cover: list[int], edges: list[(int, int)], edges_to_cover: list[(int, int)], cover: list[bool], n: int, i: int, k: int, pbar_incr, pbar_desc): 
        pbar_incr(1)
        if n == i:
            valid = VCoverValidatorFactory.get_validator(nodes[:], edges[:], cover, k).validate()
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
            cover_false = self.find_vcovers_binary(nodes, nodes_to_cover, edges, edges_to_cover, cover[:], n, i+1, k, pbar_incr, pbar_desc)
            if cover_false != None:
                possible_covers += cover_false

            cover[i] = True
            cover_true = self.find_vcovers_binary(nodes, nodes_to_cover, edges, edges_to_cover, cover[:], n, i+1, k, pbar_incr, pbar_desc)
            if cover_true != None:
                possible_covers += cover_true

            sorted_possible_covers = sorted(possible_covers)
            return sorted_possible_covers

class VCoverBruteForce(BinaryVCoverAlgorithm):
    def __init__(self, nodes: list[int], edges: list[(int, int)], n: int, k: int, pbar_incr, pbar_desc):
        self.nodes = nodes
        self.edges = edges
        self.n = n
        self.k = k
        self.pbar_incr = pbar_incr
        self.pbar_desc = pbar_desc

    def find_vcovers(self):
        cover = [False for _ in range(self.n)]
        i=0
        self.pbar_desc("Calculating cover... (Brute)")
        return super().find_vcovers_binary(self.nodes, self.nodes, self.edges, self.edges, cover, self.n, i, self.k, self.pbar_incr, self.pbar_desc)

class VCoverEnhanced(BinaryVCoverAlgorithm):
    def __init__(self, nodes: list[int], edges: list[(int, int)], k: int, pbar_incr, pbar_desc):
        self.nodes = nodes
        self.edges = edges
        self.k = k
        self.n = -1
        self.pbar_incr = pbar_incr
        self.pbar_desc = pbar_desc

    def find_vcovers(self):
        self.pbar_desc("Kernalizing... (Enhanced)")
        (ns, es, nodes_in_cover, k) = kernalize_vertices(self.nodes, self.edges, k=self.k)
        if ns == None:
            return None
        
        i=0
        self.n = len(ns)
        cover = [False for _ in range(self.n)]

        self.pbar_desc("Calculating cover... (Enhanced)")
        vcovers = super().find_vcovers_binary(ns, self.nodes, es, self.edges, cover, self.n, i, self.k, self.pbar_incr, self.pbar_desc)

        for i in range(len(vcovers)):
            vcover = vcovers[i]
            vcover += nodes_in_cover
            vcovers[i] = sorted(vcover)

        return vcovers

class VCoverGreedy(VCoverAlgorithm):
    def __init__(self, edges):
        self.edges = edges

    def _find_vertex_with_most_edges(self, uncovered_edges: list[(int, int)]):
        vertices_most_covered = dict()

        for (node1, node2) in uncovered_edges:
            for node in [node1, node2]:
                if node in vertices_most_covered.keys():
                    vertices_most_covered[node] += 1
                else:
                    vertices_most_covered[node] = 1
        
        winning_node = vertices_most_covered.keys()[0]
        winning_node_value = vertices_most_covered.values()[0]

        for k,v in vertices_most_covered.items():
            if v > winning_node_value:
                winning_node = k
                winning_node_value = v
        
        return winning_node

    def find_vcovers(self):
        uncovered = self.edges[:]
        cover = []

        while len(uncovered) > 0:
            v = self._find_vertex_with_most_edges(uncovered)
            cover += v

            # Remove all edges on that vertex to keep uncovered up to date
            for e in uncovered:
                (e_n1, e_n2) = e
                if e_n1 == v or e_n2 == v:
                    uncovered.remove(e)

        return [cover]

class VCoverTakeTwo(VCoverAlgorithm):
    def __init__(self, edges):
        self.edges = edges

    def find_vcovers(self):
        uncovered = self.edges[:]
        cover = []

        while len(uncovered) > 0:
            (node1, node2) = uncovered[0]
            cover += [node1,node2]
            
            uncovered = uncovered[1:]
            for e in uncovered:
                (e_n1, e_n2) = e
                if e_n1 == node1 or e_n1 == node2 or e_n2 == node1 or e_n2 == node2:
                    uncovered.remove(e)
        
        return [cover]