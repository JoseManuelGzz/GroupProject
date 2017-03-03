import random
class Solution:
    def __init__(self, cols=10, alphabet=range(0,10)):
        self.alphabet = alphabet
        self.cols = cols
        
    def get_solution(self):
        """
        returns a list of lists.
        All the elements of each list are from the specified alphabet.
        Default alphabet is 0-9
        Total number of lists are determined by the self.rows variable
        Number of items in each list are determined by the self.cols variable
        """
        return random.choice(self.alphabet)
