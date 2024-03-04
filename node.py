from typing import Self


class Node:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self.has_been_processed: bool = False
        self.walkable: bool = True

        self.parent: Self | None = None

        self.__f = 0
        self.__g = 0
        self.__h = 0

    def __repr__(self) -> str:
        return f'Node(x={self.x}, y={self.y})'
    
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other: Self) -> bool:
        if self.F == other.F:
            return self.H < other.H
        return self.F < other.F
    
    def manhattan(self, target_node: Self) -> int:
        return abs(self.x - target_node.x) + abs(self.y - target_node.y)
    
    def reset(self) -> None:
        self.has_been_processed: bool = False
        self.parent = None

        self.__f = 0
        self.__g = 0
        self.__h = 0

    @property
    def F(self) -> int:
        return self.__f
    
    @property
    def G(self) -> int:
        return self.__g
    
    @property
    def H(self) -> int:
        return self.__h
    
    @G.setter
    def G(self, new_g: int) -> None:
        self.__g = new_g
        self.__f = self.__g + self.__h

    @H.setter
    def H(self, new_h: int) -> None:
        self.__h = new_h
        self.__f = self.__g + self.__h