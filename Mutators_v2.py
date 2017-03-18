import random as random
import string

"""

<Mutators>: <Class that contains the different mutating operators
             as subclasses>

"""
class Mutators:
    """
    <__init__>
            <Constructor of the parent Mutators class>
            parameters:
                    <self> - Pointer to the object
                    <dataset> - A copy of the dataset object
            returns:
                    -NA-
    """
    def __init__(self, dataset):
        self.dataset = dataset

"""

<ExpMutator>: <Mutator subclass that implements the Exponential 
                mutation>

"""
class ExpMutator(Mutators):
    """
    <__init__>
            <Constructor of the Exponential mutator subclass>
            parameters:
                    <self> - Pointer to the object
                    <dataset> - A copy of the dataset object
                    <prob> - Probability of mutation
            returns:
                    -NA-
    """
    def __init__(self, dataset, prob):
        self.dataset = dataset
        self.prob = prob
    
    """
    <mutate>
            <Method that implements the exponential mutation on the 
             current solution to the problem>
            parameters:
                    <self> - Pointer to the object
                    <solution> - A list with the current solution to the problem
            returns:
                    <solution> - An updated list with the solution after undergoing mutation
    """
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

"""

<RandomFlip>: <Mutator subclass that implements the Random Flip 
                mutation>

"""
class RandomFlip(Mutators):
    """
    <__init__>
            <Constructor of the Random Flip mutator subclass>
            parameters:
                    <self> - Pointer to the object
                    <dataset> - A copy of the dataset object
                    <prob> - Probability of mutation
            returns:
                    -NA-
    """
    def __init__(self, dataset, prob):
        self.dataset = dataset
        self.prob = prob
    
    """
    <mutate>
            <Method that implements the random flip mutation on the 
             current solution to the problem>
            parameters:
                    <self> - Pointer to the object
                    <solution> - A list with the current solution to the problem
            returns:
                    <solution> - An updated list with the solution after undergoing mutation
    """
    def mutate(self, solution):
        i = 0
        alphabet_per_column = self.dataset.get_alphabet_per_column()
        while (i < len(solution)):
            p = random.uniform(0, 1)
            if (p < self.prob):
                solution[i] = random.choice(alphabet_per_column[i])
            i=i+1
        return solution


