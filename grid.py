import enum
import random
from node import Node


class Grid:
    def __init__(self, 
                 width: int = 0, 
                 height: int = 0) -> None:
        self.width = width
        self.height = height
        self.__matrix: list[list[Node]] = []
    
    def make(self) -> None:
        for x in range(self.width):
            y_line = []
            for y in range(self.height):
                node = Node(x=x, y=y)
                chance = random.random()

                if chance <= .25:
                    node.walkable = False

                y_line.append(node)

            self.__matrix.append(y_line)

    def get_node_at(self, x: int = 0, y: int = 0) -> Node | None:
        if x > self.width - 1 or x < 0 or y > self.height - 1 or y < 0:
            return None
        
        return self.__matrix[x][y]

    def get_neighbors(self, current: Node) -> list[Node]:
        up = (current.x, current.y + 1)
        right = (current.x + 1, current.y)
        down = (current.x, current.y - 1)
        left = (current.x - 1, current.y)

        neighbors = [up, right, down, left]
        valid_nodes: list[Node] = []

        for x, y in neighbors:
            if x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1: continue
            node = self.get_node_at(x=x, y=y)
            
            if node is None: continue

            if node.has_been_processed or not node.walkable: continue
            valid_nodes.append(node)

        return valid_nodes
