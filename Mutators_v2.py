"""
Class mutators
            This class is used as a parent class to two additional classes.
            It contains an initialiser which takes the dataset as an argument
            and a second method called mutate used by the sub-classes
            Sub-class: ExpMutator
            Sub-class:RandomFlip
"""
import random as random
import string

class mutators:
    
    def __init__(self, dataset):
        self.dataset = dataset
    
    def mutate(self, solution):
        pass


class ExpMutator(mutators):
    
    def __init__(self, dataset, prob):
        self.dataset = dataset
        self.prob = prob
    
    def mutate(self, solution):
        i = random.randint(0, len(solution))
        curr = i
        coin = random.uniform(0, 1)
        alphabet_per_column = self.dataset.get_alphabet_per_column()
        while (curr < len(solution) or coin < self.prob):
            solution[curr] = random.choice(alphabet_per_column[curr])
            coin = random.uniform(0, 1)
            if (curr >= len(solution)-1):
                curr = len(solution)+1
            else:
                curr =  random.randint(curr, len(solution))
        return solution

class RandomFlip(mutators):
    def __init__(self, dataset, prob):
        self.dataset = dataset
        self.prob = prob
    
    def mutate(self, solution):
        i = 0
        alphabet_per_column = self.dataset.get_alphabet_per_column()
        while (i < len(solution)):
            p = random.uniform(0, 1)
            if (p < self.prob):
                solution[i] = random.choice(alphabet_per_column[i])
            i=i+1
        return solution


