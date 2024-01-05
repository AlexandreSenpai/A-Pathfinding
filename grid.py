import enum
from node import Node


class Grid:
    def __init__(self, 
                 width: int = 0, 
                 height: int = 0) -> None:
        self.width = width
        self.height = height
        self.__matrix: list[list[Node]] = []

    def draw(self, selected_nodes: list[Node], processed: list[Node], done=False) -> None:
        class COLORS(enum.Enum):
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'

        for x in range(self.width):
            line = ''
            for y in range(self.height):
                node = self.get_node_at(x, y)

                if done and selected_nodes:
                    if node in selected_nodes:
                        line += f'{COLORS.BOLD.value}{COLORS.OKGREEN.value}[{str(node)}]{COLORS.ENDC.value}'
                    else:
                        line += f'{COLORS.BOLD.value}{COLORS.WARNING.value}[{str(node)}]{COLORS.ENDC.value}'
                    continue

                if node is not None and node not in processed and node not in selected_nodes:
                    line += f'[{COLORS.WARNING.value}F={node.F}{COLORS.ENDC.value} G={node.G} H={node.H}]'
                
                if node in processed:
                    line += f'{COLORS.OKBLUE.value}[F={node.F} G={node.G} H={node.H}]{COLORS.ENDC.value}'
                
                if node in selected_nodes:
                    line += f'{COLORS.OKGREEN.value}[F={node.F} G={node.G} H={node.H}]{COLORS.ENDC.value}'
                
            print(line, flush=True)
        print('\n')
    
    def make(self) -> None:
        for x in range(self.width):
            y_line = []
            for y in range(self.height):
                y_line.append(Node(x=x, y=y))

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
