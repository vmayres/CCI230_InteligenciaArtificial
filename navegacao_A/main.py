from A_estrela import *
from mapa import *


def main():
    
    grid = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    # inicializa o A*
    a_star = Aestrela()
    a_star.inicio(grid,0,0,9,9)

    desenha_mundo(a_star.grid)
    desenha_destino(a_star.goal)
    posiciona_tartaruga(a_star.robot_pos)
    
    #executa algoritmo de busca A*
    a_star.gera_caminho()
    
    move_tartaruga(a_star.caminho)
    print(a_star.caminho)


if __name__ == "__main__":
    main()
    input()
