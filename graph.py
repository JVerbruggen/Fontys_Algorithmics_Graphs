import networkx as nx
import random
from vertex_manipulations import *
from graph_factory import *

class LabGraph(nx.Graph):
    def print_matrix(self):
        nodes = [n for n in self.nodes()]
        matrix = []

        for node in nodes:
            adjacent = 0
            neighbors = [n for n in self.neighbors(node)]

            row = []
            for adjacentNode in nodes:
                score = 0
                if adjacentNode in neighbors:
                    if adjacentNode == node:
                        score += 2
                    else:
                        score += 1
                row += [score] 
            
            matrix += [row]
        

        matrix_str = '\n'.join(['{:3}'.format(nodes[i]) + '| ' + ''.join(['{:3}'.format(item) for item in matrix[i]]) for i in range(len(matrix))])
        header_str = '     ' + ''.join(['{:3}'.format(item) for item in nodes]) + "\n      " + ''.join(['---' for _ in nodes])

        return 'ADJACENCY MATRIX\n\n' + header_str + "\n" + matrix_str
    
    def get_color_map(self, k: int) -> list[str]:
        nodes = list(self.nodes())
        edges = list(self.edges())

        isolated = find_isolated_nodes(nodes, edges)
        pendant = find_pendant_nodes(nodes, edges)
        tops = find_tops_nodes(nodes, edges, k)

        color_map = []
        for node in nodes:
            if node in isolated:
                color_map += ['#cccccc']
            elif node in pendant:
                color_map += ['#00bb00']
            elif node in tops:
                color_map += ['#cc0000']
            else:
                color_map += ['#5555dd']
        return color_map

    def add_pendant(self):
        nodes = list(self.nodes())
        random.shuffle(nodes)
        edges = list(self.edges())

        for node in nodes:
            adjacent_nodes = find_adjacent_nodes(node, edges)
            deg = len(adjacent_nodes)
            if deg == 0:
                self.add_edge(node, random_node(nodes))
            elif deg > 1:
                to_remove = deg - 1
                for i in range(to_remove):
                    self.remove_edge(node, adjacent_nodes[i])
            else: continue
            break

    def remove_pendant(self):
        nodes = list(self.nodes())
        random.shuffle(nodes)
        edges = list(self.edges())

        for node in nodes:
            deg = degree(node, edges)
            if deg == 1:
                self.add_edge(node, random_node(nodes, not_in=[node]))
                break

    def add_tops(self):
        nodes = list(self.nodes())
        random.shuffle(nodes)
        edges = list(self.edges())

        k = k_vcover_input.value

        for node in nodes:
            adjacent_nodes = find_adjacent_nodes(node, edges)
            deg = len(adjacent_nodes)
            if deg < k:
                to_add = (k+1) - deg

                nodes_pickfrom = [n for n in nodes if n not in adjacent_nodes and n != node]
                random.shuffle(nodes_pickfrom)
                for i in range(to_add):
                    self.add_edge(node, nodes_pickfrom[i])
                break

    def remove_tops(self):
        nodes = list(self.nodes())
        random.shuffle(nodes)
        edges = list(self.edges())

        k = k_vcover_input.value

        for node in nodes:
            adjacent_nodes = find_adjacent_nodes(node, edges)
            deg = len(adjacent_nodes)
            if deg > k:
                removing = int(random.random() * deg)
                for i in range(removing):
                    self.remove_edge(node, adjacent_nodes[i])
                break

    def find_subgraphs(self) -> list[list[int]]:
        subgraphs = []
        processed = []

        to_check = [i for i in self.nodes()]
        stack = []
        
        while True:
            cur_check = to_check[0] if len(to_check) > 0 else None
            if len(stack) == 0:
                if cur_check is None:
                    break

                stack += [cur_check]
                processed += [cur_check]
                to_check.remove(cur_check)

                subgraphs += [[]]
            else:
                cur_check = stack.pop()
                if cur_check not in subgraphs[-1]: # prevent cycles from occuring twice
                    subgraphs[-1] += [cur_check]
                    processed += [cur_check]

                    adding = [n for n in self.neighbors(cur_check) if n not in processed]
                    stack += adding
                    to_check = [n for n in to_check if n not in adding]
            
        return subgraphs

    def connect(self):
        subgraphs = self.find_subgraphs()

        first = None
        for sg in subgraphs:
            if first is None:
                first = sg[0]
            else:
                self.add_edge(first, sg[0])