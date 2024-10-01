import numpy as np
import math

from node import *

class Aestrela():
    
    def __init__(self) -> None:
        self.grid = []
        self.open = []
        self.closed = []
        self.robot_pos = []
        self.goal = []

    # calcula a heuristica
    def h(self, x, y):
        return math.sqrt((abs(x - noh_final.posicao[0]))**2 + (abs(y - noh_final.posicao[1]))**2)

    # calcula distancia de locomoçcao
    def g(self, x, y):
        return math.sqrt((abs(x - noh[0]))**2 + (abs(y - self.robot_pos[1]))**2)

    def gera_caminho(self, inicio, fim, grid):
        self.grid = grid
        
        noh_inicial = Node(None, inicio[0], inicio[1])
        noh_final = Node(None, fim[0], fim[1])

        while noh_inicial.posicao != noh_final.posicao:

            lista = [[self.robot_pos[0], self.robot_pos[1]+1], [self.robot_pos[0], self.robot_pos[1]-1],
                     [self.robot_pos[0]+1, self.robot_pos[1]], [self.robot_pos[0]-1, self.robot_pos[1]],
                     [self.robot_pos[0]+1, self.robot_pos[1]+1], [self.robot_pos[0]-1, self.robot_pos[1]-1],
                     [self.robot_pos[0]+1, self.robot_pos[1]-1], [self.robot_pos[0]-1, self.robot_pos[1]+1]]

            for vizinho in lista:
                # restringe à grid
                if vizinho[0] in range(0, 10) and vizinho[1] in range(0, 10):
                    if self.grid[vizinho[0], vizinho[1]] != 1:  # pula os obstaculos
                        self.open.append(vizinho)

            menor = 1000

            for position in self.open:
                if self.h(position[0], position[1]) + self.g(position[0], position[1]) < menor:
                    menor = self.h(position[0], position[1]) + \
                        self.g(position[0], position[1])
                    self.robot_pos = position
                    
            #adiciona a csa ao caminhos que o robo vai passar
            self.caminho.append(self.robot_pos)
            #limpa os a lisat de possiveis casa adjasentes.
            #self.open.clear()
            
