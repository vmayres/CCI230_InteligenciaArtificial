from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Função para converter a previsão em uma flor (pode ser melhorada)
def classtoflower(classe):
    for previsao in classe:
        if previsao[0] > previsao[1] and previsao[0] > previsao[2]:
            print("Setosa")
        elif previsao[1] > previsao[0] and previsao[1] > previsao[2]:
            print("Versicolor")
        else:
            print("Virginica")

#carrega o dataset iris flower disponibilizado pelo sklearn
iris_X, iris_y = load_iris(return_X_y=True)

#imprime as llista do dataset
'''
iris_X <= entrdas do dataset
iris_y <= saidas do dataset
'''
print(iris_X)
print(iris_y)

# Cria um modelo de classificação KNN com 5 vizinhos
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(iris_X, iris_y)

# Prever a classe de uma flor com as seguintes dimensões
'''
A previsão é feita com base na classe da maioria dos vizinhos mais próximos
O método predict_proba retorna a probabilidade de cada classe
exemplo: [0. 0. 1.] => 
0% de chance de ser da classe 0, 
0% de chance de ser da classe 1 e 
100% de chance de ser da classe 2
'''
print("Previsao: ", knn.predict_proba([[6.2, 3.4, 5.4, 2.3], [4.7, 3.2, 1.3, 0.2], [6, 3, 4, 2]]))

# Imprime a classe prevista para cada flor com base na probabilidade.
classtoflower(knn.predict_proba([[6.2, 3.4, 5.4, 2.3], [4.7, 3.2, 1.3, 0.2], [6, 3, 4, 2]]))
'''
predic 1 é 100% de chance de ser da classe 3
predic 2 é 100% de chance de ser da classe 0
predic 3 é 100% de chance de ser da classe 1

output: 
Previsao:  [[0. 0. 1.]
 [1. 0. 0.]
 [0. 1. 0.]]
'''


# Acuracia das previsioes realizados pelo modelo knn.
"""
retorna um valor entre 0 e 1, onde 1 é a previsão perfeita, 
por isso é multiplicado por 100 para obter o valor em porcentagem
"""
print("Score:", knn.score(iris_X, iris_y) * 100, "%")

# Cria um gráfico 3D para visualizar as dimensões do dataset
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Usar a quarta dimensão para definir o tamanho dos pontos
# O tamanho dos pontos é proporcional ao tamanho da pétala
sizes = iris_X[:, 3] * 50  # Multiplica por 50 para aumentar visibilidade

# Plota os pontos 50 primeiros pontos com a cor azul refrerente a classe 0 "setosa"
for i in range(50):
    ax.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], s=sizes[i], c='b')

# Plota os pontos 50 primeiros pontos com a cor vermelha refrerente a classe 1 "versicolor"
for i in range(50, 100):
    ax.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], s=sizes[i], c='r')

# Plota os pontos 50 primeiros pontos com a cor verde refrerente a classe 2 "virginica"
for i in range(100, 150):
    ax.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], s=sizes[i], c='g')

# Adicionar rótulos aos eixos
ax.set_xlabel('Comprimento da Sépala')
ax.set_ylabel('Largura da Sépala')
ax.set_zlabel('Comprimento da Pétala')

# Exibir o gráfico
plt.show()
