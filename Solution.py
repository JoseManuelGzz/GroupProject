import random
from collections import Counter

"""

Solution: Class that creates a solution for the 
             string consensus problem for both the 
             CSP and FFMSP given a dataset

"""
class Solution:
    """
    __init__
            Constructor for the Solution class
            parameters:
                    self - Pointer to the object
                    dataset - A dataset object with the same 
                                length sequences as characters 
            returns:
                    -None-
    """  
    def __init__(self, dataset):
        self.dataset = dataset

    """
    get_solution
            Method that returns a solution when using the SA or MCM algorithms.
            parameters:
                    self - Pointer to the object
                    solution_type - String that specifies the problem type, CSP or FFMSP
            returns:
                    result - A list of lists with the proposed solution 
    """    
    def get_solution(self, solution_type):
        if solution_type.lower() == 'csp':
            return self.dataset.get_most_common_char_column()
        else:
            result = []
            for alpha in self.dataset.get_alphabet_per_column():
                counter = Counter(alpha)
                counter_size = len(counter)
                element = counter.most_common(counter_size)[counter_size-1][0]
                result.append(element)
            return result

    """
    get_solutions
            Method that returns a solution when using the Genetic algorithm.
            parameters:
                    self - Pointer to the object
                    rows - The number of rows in the dataset
            returns:
                    result - A list of lists with the proposed solution 
    """  
    def get_solutions(self, rows):
        solutions = [[]]  
	self.rows = rows
	chrom_length = self.dataset.cols
    	for i in range(rows):  
            temp = []  
            for j in range(chrom_length):  
                temp.append(random.randint(0, 3))  
                solutions.append(temp)  
        return solutions[1:]

