
import random
def initializing(length,n,t):
  population=[]
  for x in range(length):
    new=""
    for i in range(n*t):
      new+=str(random.randint(0,1))
    population.append(new)
  return population

def fitness_check(chromosome, n, t):
  overlap = 0
  con = 0

  for i in range(t):
    timeslot = chromosome[i * n:(i + 1) * n]
    count = timeslot.count("1")
    if count > 1:
       overlap += count - 1

  for i in range(n):
    count = 0
    for j in range(t):
      if chromosome[i * n + j] == "1":
        count += 1
    if count != 1:
      con += abs(count - 1)

  total = overlap + con
  return -total

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)

    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return offspring1, offspring2

def mutation(chromosome, rate):
    m_chromosome = list(chromosome)
    for gene_index in range(len(m_chromosome)):
        if random.random() < rate:
            if m_chromosome[gene_index] == "1":
                m_chromosome[gene_index] = "0"
            else:
                m_chromosome[gene_index] = "1"
    return "".join(m_chromosome)

def gen_algo(n, t, length=10, max_generations=10, rate=0.01):
    population = initializing(length, n, t)
    best_solution = None
    best_fitness = float("-inf")
    for generation in range(max_generations):
        fitness_values = [fitness_check(chromosome, n, t) for chromosome in population]

        for chromosome, fitness_val in zip(population, fitness_values):
            if fitness_val > best_fitness:
                best_fitness = fitness_val
                best_solution = chromosome

        new_population = []
        while len(new_population) < length:
            parent1, parent2 = selection(population, fitness_values)

            offspring1, offspring2 = single_point_crossover(parent1, parent2)

            offspring1 = mutation(offspring1, rate)
            offspring2 = mutation(offspring2, rate)

            new_population.extend([offspring1, offspring2])

        population = new_population[:length]

    return best_solution, best_fitness

def selection(population, fitness_values):
  total_fit = sum(fitness_values)
  pro = []
  for i in fitness_values:
    pro.append(i/total_fit)
  parents = random.choices(population, weights=pro, k=2)
  return parents

import numpy as np

# Coefficients of the equations (A) and constants (b)
A = np.array([
    [1, 1, 1],
    [2, -1, 3],
    [-1, 4, -1],
    [1, 2, 5]
])
b = np.array([6, 14, 2, 18])

# Solve the overdetermined system using least squares (minimizes ||Ax - b||)
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Solution x:",x)

print(round(.29998437,2))
print(1/1000)

with open("input.txt", "r") as inputs, open("output.txt", "a") as outputs:
    line = inputs.readline().strip().split()
    num_c = int(line[0])
    num_t = int(line[1])

    course_names = []
    for i in range(num_c):
        course_line = inputs.readline().strip()
        course_names.append(course_line)

    best_solution, best_fitness = gen_algo(num_c,num_t,)

    outputs.write("Genetic Algorithm Results:\n")
    outputs.write(f"Best Solution: {best_solution}\n")
    outputs.write(f"Best Fitness: {best_fitness}\n")

def two_point_crossover(parent1, parent2):
  first_point = random.randint(0, len(parent1) - 1)
  second_point = random.randint(first_point + 1, len(parent1))
  first_child = parent1[:first_point] + parent2[first_point:second_point] + parent1[second_point:]
  second_child = parent2[:first_point] + parent1[first_point:second_point] + parent2[second_point:]
  return first_child, second_child
