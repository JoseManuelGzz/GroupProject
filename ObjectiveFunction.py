"""
    Class definition for ObjectiveFunction
    and corresponding subclasses
    MaximisingFunction and MinimisingFunction
    """

class ObjectiveFunction(object):
    def __init__(self):
        pass
        
    # function that creates a list of distances from each sequence to a given string
    def calculate_hamming_distances(self, sequences, string):
        result = []
        dist = 0
        for sequence in sequences:
        #Add 1 if elements are different, 0 if they are the same
            for i in range(len(sequence)):
                if sequence[i] != string[i]:
                    dist = dist + 1
                    result.append(dist)
                    dist = 0
        return result

class MaximisingFunction(ObjectiveFunction):
    def evaluate(self, sequences, proposed_solution, threshold):
        error = False
        #Validating the parameters
        if type(sequences) != type([]):
            error = True
        elif type(sequences[0]) != type([]):
                error = True
        elif type(sequences[0][0]) != type(0):
            error = True
        elif type(sequences[0][0]) != type(proposed_solution[0]):
                error = True
        if error:
            raise NameError("First argument must be a list of lists, second argument must be a list,\
                            both containing the same type, and third argument must be an integer")
        
        #Obtain the list of distances between the proposed solution and the sequences
        distances = self.calculate_hamming_distances(sequences, proposed_solution)
        return len(filter(lambda x: x >= threshold, distances))

class MinimisingFunction(ObjectiveFunction):
    def evaluate(self, sequences, proposed_solution):
        error = False
        #Validating the parameters
        if type(sequences) != type([]):
            error = True
        elif type(sequences[0]) != type([]):
                error = True
        elif type(sequences[0][0]) != type(0):
                error = True
        elif type(sequences[0][0]) != type(proposed_solution[0]):
                error = True
        if error:
            raise NameError("First argument must be a list of lists, second argument must be a list,\
                            both containing the same type")
        
        #Obtain the list of distances between the proposed solution and the sequences
        distances = self.calculate_hamming_distances(sequences, proposed_solution)
                
        return max(distances)




