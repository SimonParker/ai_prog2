#simon parker
import matplotlib.pyplot as plt
import random

from state import *


max_iters = 1000

'''
each generation consists of N individuals. A list N long of (Objects, fitness of object) tuples

need a function to take a board state and calculate the fitness (# of mutually attacking queens? rows seem easy, but diagonals?)

need a function to randomly sample from generation list based on values in tuple

need a function to perform crossover on 2 board states

need a function to mutate a board state based on a given percent chance

need to save the plots and individuals from each configuration
'''

population_sizes = [10, 100, 500, 1000]
mutation_chances = [0.001, 0.01, 0.05, 0.2] #the chance to mutate each gene
for pop in population_sizes:
  for mut = mutation_chances:
    indivduals_list = []
    trials = [] #contains the final generation (list) of each trial.
    for i in range(3): #each combination of population size and mutation chance runs 3 times, highest final average fitness is chosen
      individuals = []
      generation_evals = [] #1000 long list of generational evaluations
      cur_generation = []
      for j in range(pop):
        board = rand_board()
        #cur_generation.append(board, heuristic(board))
      generation_evals.append(evaluate(cur_generation))
      for j in range(max_iters):
        if j == 0 or j == (max_iters / 2) - 1 or j == max_iters - 1:
          individuals.append(best_individual(cur_generation)) 
        #cur_generation = repopulate(cur_generation, mut) #returns a list of tuples 
        generation_evals.append(evaluate(cur_generation))
      trials.append(generation_evals)
      individuals_list.append(individuals)
    max_index = trials.index(max([x[-1][0] for x in trials]))
    best_trial = trials[max_index] #a list of 1000 tuples, each tuple is the fitness of a generation (average, best)
    best_individuals = individuals_list[max_index]
    #plot best trial, save to disk
    #save the best_indivuals to disk as a text file or something
    

