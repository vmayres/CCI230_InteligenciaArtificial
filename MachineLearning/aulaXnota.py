from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

# entradas
# carregar dados do arquivo 
data = np.loadtxt(r'EX2_Notas.txt', delimiter='\t')

# Separar colunas
livros = data[:, 0]
aulas = data[:, 1]
notas = data[:, 2]

# Converter todas as listas para inteiros
livros = list(map(int, livros))
aulas = list(map(int, aulas))
notas = list(map(int, notas))

# Criar uma lista de listas com as entradas livros e aulas
entradas = [list(c) for c in zip(livros, aulas)]

# cria um grafico 3D
fig = plt.figure() #grafico sem previsao
fig_pred = plt.figure() #grafico com previsao
ax = fig.add_subplot(111, projection='3d')
ax_pred = fig_pred.add_subplot(111, projection='3d')

# plota os pontos
ax.scatter(livros, aulas, notas) #grafico sem previsao
ax_pred.scatter(livros, aulas, notas) #grafico com previsao

# Cria um modelo de regressão linear
regressao = linear_model.LinearRegression()
regressao.fit(entradas, notas)

#calcula os coeficientes da regressao linear
# y = a*x + b
# a = coef angular e b = coef linear
a = regressao.coef_
b = regressao.intercept_
print("Coef Angular:", a, "Coef Linear:", b)

# Prever as notas para os pontos de entrada
previsao = regressao.predict(entradas)

# Plota a previsão no gráfico como uma linha vermelha
ax_pred.plot(livros, aulas, previsao, color="red", label='Previsão')

#prever notas para os pontos de entrada
"""
no exemplo abaixo, a previsao é feita para os pontos de nº de Livros e nª de Aulas:
(2, 11), obteve uma nota de 59.7
(0, 5), obteve uma nota de 43.7
(4, 10), obteve uma nota de 79.1
(2, 10), obteve uma nota de 58.2
(4, 15), obteve uma nota de 72.7
"""
predic = regressao.predict([[2, 11],[0, 5],[4, 10],[2, 10],[4, 15]])
print("Previsao: ", predic)

# Calcular a acurácia do modelo de regressão, multiplicando por 100 para obter o valor em porcentagem
score = regressao.score(entradas, notas)
print("Score: ",score * 100, "%")


# Adicionar rótulos aos eixos
#figura sem previsao
ax.set_xlabel('Livros')
ax.set_ylabel('Aulas')
ax.set_zlabel('Notas')

#figura com previsao
ax_pred.set_xlabel('Livros')
ax_pred.set_ylabel('Aulas')
ax_pred.set_zlabel('Notas')

# Mostrar o gráfico
plt.show()
