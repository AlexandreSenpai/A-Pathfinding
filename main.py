import pygame
import sys
from astar import AStar

from grid import Grid
from node import Node

# Inicializa o Pygame
pygame.init()

# Tamanho da tela e das células
grid = Grid(width=100,
            height=100)
grid.make()
cell_size = 15
screen_w = grid.width * cell_size 
screen_h = grid.height * cell_size 
screen = pygame.display.set_mode((screen_w, screen_h))

finder = AStar(grid=grid)

start_node = grid.get_node_at(0, 0)
end_node = grid.get_node_at(5, 4)

path = []
found = False

# Cores
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 128, 255)
black = (0, 0, 0)
gray = (64, 64, 64)
white = (255, 255, 255)

# Fonte para o texto
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 24)

class GridNode(pygame.Rect):
    def __init__(self, 
                 left: float, 
                 top: float, 
                 width: float, 
                 height: float, 
                 node: Node) -> None:
        super().__init__(left, top, width, height)
        self.node = node
    
    def is_mouse_over(self) -> bool:
        return self.collidepoint(pygame.mouse.get_pos())

    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    
    if start_node is not None and end_node is not None and found == False:
        path, processed, not_processed = finder.find(start_node=start_node, end_node=end_node)
        found = True

    for x in range(grid.width):
        for y in range(grid.height):

            node = grid.get_node_at(x, y)
            
            if node is None: continue

            if path:
                selected_color = yellow if node in not_processed else white
                selected_color = blue if node in processed else selected_color
                selected_color = green if node in path else selected_color
            else:
                selected_color = white

            selected_color = black if not node.walkable else selected_color

            rect = GridNode(x * cell_size, 
                            y * cell_size, 
                            cell_size, 
                            cell_size,
                            node)
            
            pygame.draw.rect(screen, selected_color, rect, 0)
            pygame.draw.rect(screen, black, rect, 1)  # Contorno

            # f_text = font.render(f'F={node.F}', True, black)
            # g_text = font2.render(f'G={node.G}', True, black)
            # h_text = font2.render(f'H={node.H}', True, black)


            # screen.blit(f_text, (node.x * cell_size + ((cell_size / 2) - 20), node.y * cell_size + ((cell_size / 2) - 10)))
            # screen.blit(g_text, (node.x * cell_size + 8, node.y * cell_size + 10))
            # screen.blit(h_text, (node.x * cell_size + ((cell_size / 2) + 10), node.y * cell_size + 10))

            if rect.is_mouse_over():
                hovering_node = rect.node
                if hovering_node != end_node:
                    found = False
                    end_node = hovering_node 


    pygame.display.flip()

pygame.quit()