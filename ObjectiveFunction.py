"""
ObjectiveFunction: Class that implements functions 
                    for minimisation in the context of String Consensus
                    Problems
"""

class ObjectiveFunction(object):
    def __init__(self):
        pass
        
    """
    calculate_hamming_distances
        Calculates n numeric values representing the 
            number of chars that are different between 
            a sequence in the dataset and in the solution
        parameters:
            sequences - List of lists representing char sequences
            solution - List representing a sequence of chars
        returns:
            List with the hamming distances between the 
                sequences in the dataset and the 
                solution given
    """
    # function that creates a list of distances from each sequence to a given string
    def calculate_hamming_distances(self, sequences, solution):
        result = []
        dist = 0
        for sequence in sequences:
        #Add 1 if elements are different, 0 if they are the same
            for i in range(len(sequence)):
                if sequence[i] != solution[i]:
                    dist = dist + 1
            result.append(dist)
            dist = 0
        return result

"""
FFMSPObjectiveFunction: To determine how far a string is from
            a set of sequences (Extends ObjectiveFunction)
"""
class FFMSPObjectiveFunction(ObjectiveFunction):
    def __init__(self, threshold):
        self.threshold = threshold

    """
    evaluate
        Use the hamming distances to determine how far a string is from
            a set of sequences
        parameters:
            sequences - List of lists representing char sequences
            proposed_solution - List representing a sequence of chars
        returns:
            The length of a list  with the distances above the 
                threshold defined in the class

    """
    def evaluate(self, sequences, proposed_solution):        
        #Obtain the list of distances between the proposed solution and the sequences
        distances = self.calculate_hamming_distances(sequences, proposed_solution)
        return -1 * len(filter(lambda x: x >= self.threshold, distances))

"""
CSPObjectiveFunction: To determine how close a string is from 
    a set of sequences (Extends ObjectiveFunction)
"""
class CSPObjectiveFunction(ObjectiveFunction):

    """
    evaluate
        Use the hamming distances to determine how close a string is from
            a set of sequences
        parameters:
            sequences - List of lists representing char sequences
            proposed_solution - List representing a sequence of chars
        returns:
            The largest distance between the proposed solution and 
                the sequences of the dataset

    """
    def evaluate(self, sequences, proposed_solution):        
        #Obtain the list of distances between the proposed solution and the sequences
        distances = self.calculate_hamming_distances(sequences, proposed_solution)
        return max(distances)




