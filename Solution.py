"""
<class name>: <class description/objective>
        (?)<subclass name>: <subclass description/objective>
"""
import random
from collections import Counter
class Solution:
    def __init__(self, dataset):
        self.dataset = dataset
<<<<<<< Updated upstream
    
    """
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

    """   
=======
	self.rows = 0
        
>>>>>>> Stashed changes
    def get_solution(self, solution_type):
        """
        returns a list of lists.
        All the elements of each list are from the specified alphabet.
        Default alphabet is 0-9
        Total number of lists are determined by the self.rows variable
        Number of items in each list are determined by the self.cols variable
        """
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

