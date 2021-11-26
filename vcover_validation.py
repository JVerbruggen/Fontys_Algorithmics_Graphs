class VCoverValidator:
    def __init__(self, nodes: list[int], edges: list[(int, int)], cover: list[bool], k: int):
        self.nodes = nodes
        self.edges = edges
        self.cover = cover
        self.k = k

    def validate(self) -> bool:
        raise NotImplementedError

class DefaultVCoverValidator(VCoverValidator):
    def validate(self):
        vertices_used = sum(self.cover)
        if vertices_used != self.k:
            return False
        
        covered_nodes = [self.nodes[i] for i in range(len(self.nodes)) if self.cover[i]]

        this_edges = self.edges[:]

        for node in covered_nodes:
            edges_covered = [(va, vb) for (va, vb) in this_edges if va == node or vb == node]
            this_edges = [e for e in this_edges if e not in edges_covered]

        return len(this_edges) == 0

class VCoverValidatorFactory:
    def get_validator(nodes: list[int], edges: list[(int, int)], cover: list[bool], k: int) -> VCoverValidator:
        return DefaultVCoverValidator(nodes, edges, cover, k)