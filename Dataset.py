"""

Dataset: Class that generates random sequences for the simulation of
            a problem instance.

"""

import random
from collections import Counter
class Dataset:
    """
            __init__
                    Constructor for the Dataset class
                    parameters:
                            rows:  size of the dataset (number of sequences)
                            cols: size of each sequence - columns
                            alphabet: characters from which the sequences are built
                    returns:
                            -None-

        """
    def __init__(self, rows=100, cols=10, alphabet=range(0,10)):
        self.rows = rows
        self.alphabet = alphabet
        self.cols = cols
        self.alphabet_per_column = []
        self.most_common_char = []
        self.d = []
        for _ in range(self.rows):
            self.d.append([random.choice(self.alphabet) for _ in range(self.cols)])

        for i in range(self.cols):
            column = zip(*self.d)[i]
            self.alphabet_per_column.append(list(column))
            self.most_common_char.append(Counter(column).most_common(1)[0][0])

    """
        get_data
                Get data from dataset
                parameters:
                        None
                returns:
                        self.d --> (data from the dataset)

    """
    def get_data(self):
        """
        returns a list of lists.
        All the elements of each list are from the specified alphabet.
        Default alphabet is 0-9
        Total number of lists are determined by the self.rows variable
        Number of items in each list are determined by the self.cols variable
        """
        return self.d

    """
        get_most_common_char_column
                returns most common character from a column
                parameters:
                        -None-
                returns:
                        self.most_common_char --> (Most common character from the columns, it is a sequence of the length self.cols)

    """
    def get_most_common_char_column(self):
        return self.most_common_char

    """
        get_alphabet_per_column
                returns all characters used in a column
                parameters:
                        -None-
                returns:
                        self.alphabet_per_column --> (All characters from the columns, returned as list of lists)

    """
    def get_alphabet_per_column(self):
        return self.alphabet_per_column

    """
        get_cols
                returns no of columns in a dataset
                parameters:
                        -None-
                returns:
                        self.cols

    """
    def get_cols(self):
        return self.cols

    """
        get_alphabet
                returns alphabet used in the dataset
                parameters:
                        -None-
                returns:
                        self.alphabet

    """
    def get_alphabet(self):
        return self.alphabet

        