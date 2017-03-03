import random
class Dataset(object):
    def __init__(self, rows=100, cols=10, alphabet=range(0,10)):
        self.rows = rows
        self.alphabet = alphabet
        self.cols = cols
        
    def get_data(self):
        """
        returns a list of lists.
        All the elements of each list are from the specified alphabet.
        Default alphabet is 0-9
        Total number of lists are determined by the self.rows variable
        Number of items in each list are determined by the self.cols variable
        """
        d = []
        for _ in range(self.rows):
            d.append([random.choice(self.alphabet) for _ in range(self.cols)])
        return d



        
