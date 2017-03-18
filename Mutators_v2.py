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
        i = random.randint(0, len(solution)-1)
        curr = i
        coin = random.uniform(0, 1)
        alphabet_per_column = self.dataset.get_alphabet_per_column()
        while (curr < len(solution) and coin < self.prob):
            solution[curr] = random.choice(alphabet_per_column[curr])
            coin = random.uniform(0, 1)
            #To avoid always considering the final element
            #if the method reaches the third from last element
            #consider the following options equally:
            #go to second from last, and then either to the end or finish
            #go to the last element and then finish
            #finish completely
            if (curr < len(solution)-2):
                curr =  random.randint(curr+1, len(solution))
                if (curr == len(solution)) :break
            else:
                break
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


