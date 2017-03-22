"""

Evolutionary: 

"""

from Mutator import Mutator
#import matplotlib.pyplot as plt  
import math 
import random
import numpy
#from Dataset import Dataset
import operator

class Evolutionary:
    """
            _init_
                    Constructor for the Evolutionary class
                    parameters:
                            dataset - An instance of Dataset class
                            solution - An instance of Solution class
                            mutator - An instance of Mutator class
                            obj_func - An instance of ObjectiveFunction class
                            status - An instance of Status class
                            num_parents - Number of parents in the original Solution

                    returns:
                            -None-

    """
    def __init__(self, dataset, solution, mutator, obj_func, status, num_parents=6):
        self.dataset = dataset
        self.data = dataset.get_data()
        self.solution = solution
        self.mutator = mutator
        self.obj_func = obj_func
        #self.rows = rows
        #self.chrom_length = chrom_length
        self.status = status
        self.results = []
        self.solutions = []
        self.num_parents = num_parents
        self.set_initial_population()

    """
        set_initial_population
                Generates the initial population of parents for running the evolutionary algorithm
                Called from inside the constructor only.
                Uses the alphabet from the Dataset instance to generate the individual parents
                parameters:
                        -None-

                returns:
                        -None-

    """
    def set_initial_population(self):
        alphabet_per_column = self.dataset.get_alphabet_per_column()
        #print(len(alphabet_per_column))
        #print(len(alphabet_per_column[0]))
        for i in range(self.num_parents):
            a = []
            for j in range(self.dataset.get_cols()):
                a.append(random.choice(alphabet_per_column[j]))
            self.solutions.append(a)

            #self.solutions.append([numpy.random.choice(alphabet_per_column[i], replace=True) for _ in range(self.dataset.get_cols())])
            #self.solutions.append(numpy.random.choice(alphabet_per_column[i], replace=True, size=self.dataset.get_cols()) )

    """
        run()
                Runs the evolutionary algorithm instance for the given objective function
                parameters:
                        -None-

                returns:
                        An instance of Status class with details of the iterations and the scores

    """
    def run(self):
        iterations = 0
        max_iter = self.status.get_max_iterations()
        
        parent_result = []
        child_result = []


        best_score = self.dataset.get_cols
        best_solution = []

        while iterations < max_iter:
            self.status.add_function_calls()
            iterations +=  1
            self.status.add_iteration()
            #print len(self.solutions)
            #print self.num_parents
            for i in xrange(self.num_parents):
                parent_result.append ((self.solutions[i], self.obj_func.evaluate(self.data, self.solutions[i])))
                child =  self.mutator.mutate(list(self.solutions[i]))
                child_result.append((child, self.obj_func.evaluate(self.data, child)))
            #combined_population = self.merge_two_dicts(parent_result,child_result)
            combined_population = parent_result + child_result
            sorted_combined = sorted(combined_population, key=lambda x:x[1]) #returns a list of tuples, key is the first part of tuple and score is the second
            child_sorted = sorted(child_result, key=lambda x: x[1])
            current_child_best_score = child_sorted[0][1]
            #print sorted_combined
            current_score = sorted_combined[0][1]
            if  current_score < best_score:
                best_score = sorted_combined[0][1]
                best_solution = sorted_combined[0][0]
            [solutions, scores] = zip(*sorted_combined[:self.num_parents])
            self.solutions = list(solutions)
            parent_result=[]
            child_result=[]
            current_entry = [iterations, self.status.get_function_calls(), best_score, current_child_best_score]
            self.status.add_solution_record_entry(current_entry)
            #print self.solutions

        print("Best solution:")
        print(best_solution)

        print("Best score:")
        print(best_score)

        return self.status

             

        


