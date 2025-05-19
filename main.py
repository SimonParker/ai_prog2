#simon parker
import matplotlib.pyplot as plt
import random

from state import *


max_iters = 4000


population_sizes = [10, 100, 500, 1000]
mutation_chances = [0.01, 0.05, 0.1, 0.3] #the chance to mutate each gene
for pop in population_sizes:
  for mut in mutation_chances:
    print(f"n{pop}_m{mut * 100}")
    individuals_list = []
    trials = [] #contains the final generation (list) of each trial.
    for i in range(5): #each combination of population size and mutation chance runs 5 times, highest final average fitness is chosen
      iters = -1 #fixing off by 1 issue
      done = False
      individuals = []
      generation_evals = []
      cur_generation = []
      for j in range(pop):
        board = rand_board()
        cur_generation.append((board, heuristic(board)))
      generation_evals.append(evaluate(cur_generation))
      individuals.append(best_individual(cur_generation))
      while iters < max_iters:
        if heuristic(best_individual(cur_generation)) == 28:
          break
        cur_generation = repopulate(cur_generation, mut) #returns a list of tuples 
        iters += 1
        generation_evals.append(evaluate(cur_generation))
      individuals.append(best_individual(cur_generation))
      trials.append(generation_evals)
      individuals_list.append(individuals)
    results = [len(x) for x in trials] #number of generations to find a solution
    max_index = results.index(min(results))
    best_trial = trials[max_index] #a list of tuples, each tuple is the fitness of a generation (average, best)
    best_individuals = individuals_list[max_index]
    
    av_fitness = [x[0] for x in best_trial]
    best_fitness = [x[1] for x in best_trial]
    g = [x for x in range(len(best_trial))]
    plt.plot(g, av_fitness, c='blue', label='Average', linewidth=0.5)
    plt.plot(g, best_fitness, c='red', label='Best', linewidth=0.5)
    plt.title(f"GA with population size {pop} and mutation chance {mut * 100}%")
    plt.xlabel("Generation #")
    plt.ylabel("Fitness")
    plt.legend()
    path = f"n{pop}_m{mut * 100}"
    plt.savefig(path + ".png")
    plt.close()

    file = open(path + ".txt", 'w')
    file.write(f"best initial state: {best_individuals[0]}\n")
    file.write(f"best final state: {best_individuals[1]}\n")
    file.write(f"achieved in {len(best_trial)} iterations\n")
    file.close()


