import numpy
class Dataset(object):
    def __init__(self, rows=100, cols=10, low=0, high=10):
        self.rows = rows
        self.low = low
        self.high = high
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
            d.append(numpy.random.randint(low=self.low, high=self.high, size=self.cols))
        return d



        
