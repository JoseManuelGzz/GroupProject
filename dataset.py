import random
from collections import Counter
class Dataset:
    def __init__(self, rows=100, cols=10, alphabet=range(0,10)):
        self.rows = rows
        self.alphabet = alphabet
        self.cols = cols
        self.alphabet_per_column = []
        self.most_common_char = []
        
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

        print("Dataset")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in d]))

        #Building the array with the sets of alphabet in each column
        #and
        #Building the array with the most common character in each column
        for i in range(self.cols):
            column = zip(*d)[i]
            print(column)
            self.alphabet_per_column.append(list(set(column)))
            print(self.alphabet_per_column[i])
            self.most_common_char.append(Counter(column).most_common(1)[0][0])
            print(self.most_common_char[i])
            print("---")
        return d



        
