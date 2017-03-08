import random
class Solution:
    def __init__(self, dataset):
        self.dataset = dataset
        
    def get_solution(self):
        """
        returns a list of lists.
        All the elements of each list are from the specified alphabet.
        Default alphabet is 0-9
        Total number of lists are determined by the self.rows variable
        Number of items in each list are determined by the self.cols variable
        """
        return self.dataset.get_most_common_char_column()

    def get_solutions(self):
        pass

