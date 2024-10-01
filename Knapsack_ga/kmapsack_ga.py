from pyeasyga import pyeasyga
import random
import matplotlib.pyplot as plt

# setup data
data = [{'name': 'green', 'value': 4, 'weight': 12},
        {'name': 'gray', 'value': 2, 'weight': 1},
        {'name': 'yellow', 'value': 10, 'weight': 4},
        {'name': 'orange', 'value': 1, 'weight': 1},
        {'name': 'blue', 'value': 2, 'weight': 2}]

tamanho_populacao = 100

ga = pyeasyga.GeneticAlgorithm(data, population_size=tamanho_populacao,
                               generations=800,
                               crossover_probability=0.9,
                               mutation_probability=0.2,
                               elitism = True,
                               maximise_fitness=True
                               )

cont = 0
aptidoes_por_geracao = []
melhor_por_geracao = []

# define a fitness function
def aptidao(individual, data):
    global cont
    cont += 1
    #print("individual", individual)
    values, weights = 0, 0
    for gene, box in zip(individual, data):
        print(gene, box)
        if gene != 0:
            values += box['value']*gene
            weights += box['weight']*gene
    if weights > 15:
        values = 0
    #print(values)
    #print()
    aptidoes_por_geracao.append(values)
    if(cont >= tamanho_populacao):
      print(aptidoes_por_geracao)
      melhor_por_geracao.append( max(aptidoes_por_geracao) )
      aptidoes_por_geracao.clear()
      cont = 0
    return values

def mutate(indivdual):
    mutate_index = random.randrange(len(indivdual))
    #indivdual[mutate_index] = random.randrange(0,10)
    mut_chance = random.randrange(0,3)
    if mut_chance == 0:
        indivdual[mutate_index] += 1
    else:
        if indivdual[mutate_index] == 0:
            indivdual[mutate_index] = 0
        else:
            indivdual[mutate_index] -= 1
    
ga.mutate_function = mutate
ga.fitness_function = aptidao

ga.run()
print(ga.best_individual())
plt.plot(melhor_por_geracao)
plt.savefig('graph.jpg')