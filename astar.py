import heapq
from timer import timer_decorator
from grid import Grid
from node import Node

class AStar:
    def __init__(self, grid: Grid) -> None:
        self.__grid = grid

    def set_node_distances(self, end_node: Node) -> None:
        for x in range(self.__grid.width):
            for y in range(self.__grid.height):
                node = self.__grid.get_node_at(x, y)
                if node is None: continue
                node.reset() # cleanup the node

                node.H = node.manhattan(target_node=end_node)

    def find_node_with_lowest_cost(self, nodes: list[Node]) -> Node | None:
        return heapq.heappop(nodes) if nodes else None

    def make_path(self, end_node: Node) -> list[Node]:
        path: list[Node] = [end_node]
        current_node = end_node

        while current_node.parent is not None:
            current_node = current_node.parent
            path.append(current_node)
        
        return path[::-1]
    
    @timer_decorator
    def find(self, 
             start_node: Node, 
             end_node: Node) -> tuple[list[Node], list[Node], list[Node]]:

        not_processed: list[Node] = []
        processed: list[Node] = []

        if (start_node == end_node) or \
            not end_node.walkable:
            return ([], [], [])
        
        heapq.heappush(not_processed, start_node)
        self.set_node_distances(end_node=end_node)

        while len(not_processed) > 0:

            current_node = self.find_node_with_lowest_cost(not_processed)

            if current_node is None:
                return ([], [], [])
            
            if current_node == end_node:
                return (self.make_path(end_node=end_node), processed, not_processed)
            
            neighbors = self.__grid.get_neighbors(current=current_node)

            current_node.has_been_processed = True
            processed.append(current_node)

            for neighbor in neighbors:
                next_g = current_node.G + 1

                if not neighbor.has_been_processed or next_g < neighbor.G:
                    neighbor.G = next_g
                    neighbor.parent = current_node

                    if not neighbor.has_been_processed:
                        heapq.heappush(not_processed, neighbor)
                
            # self.__grid.draw([], processed=processed+not_processed)

        return ([], [], [])
