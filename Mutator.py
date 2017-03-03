"""
=============================================
||         M U T A T O R . P Y           ||
=============================================
[PURPOSE]
The purpose of this file is to provide functions that
can mutate a provided list. Each function uses a different
mutation method. Some of the functions do require different
parameters than others and some are only tailored for lists/
strings of bits (first and second function). If further mutation
methods are desired, they can be added to the file as well.

[USAGE]
Use an import statement to load the contents of the file
and then make function calls based on the mutation method
preferred.

[RESOURCES]
(1): https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)
(2): https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_mutation.htm

[AUTHOR]
Created for the purposes of Group 3 for CE903
by Alexandros G. Stergiou
Date: 18 Feb. 2017
--------------------------------------------------------------------------------
"""



"""
--------------------------------------------------------------------------------
import statements
--------------------------------------------------------------------------------
"""
import random as random
import string

class Mutator:

    def _init_(self):
        pass
    


    """
    --------------------------------------------------------------------------------
    This function will invert every bit inside the list
    --------------------------------------------------------------------------------
    """
    #Used only for bit lists
    def use_Flip_Bit(_list_):
        l = []
        for bit in _list_:
            if (bit == 0):
                l.append(1)
            else:
                l.append(0)
        return l


    """
    --------------------------------------------------------------------------------
    Here a sudo-randomly selected number of bits are fliped from the
    original list.
    --------------------------------------------------------------------------------
    """
    #Used only for bit lists
    def use_Bit_String(_list_):
        iterations = random.randrange(1,len(_list_)-1,1)
        i = 0
        print iterations
        while (i<iterations):
            pos = random.randrange(0,len(_list_)-1,1)
            print pos
            if (_list_[pos] == 0):
                _list_[pos] = 1
            else:
                _list_[pos] = 0
            i=i+1
        return _list_




    """
    --------------------------------------------------------------------------------
    This is the random flip function where a probability
    is passed as an argument and based of that,
    each bit is flipped.
    --------------------------------------------------------------------------------
    """
    #Used only for bit lists
    def use_Random_Flip(_list_, prob):
        i = 0
        while (i<len(_list_)-1):
            p = random.uniform(0, 1)
            if (p<prob):
                if (_list_[i] == 0):
                    _list_[i] = 1
                else:
                    _list_[i] = 0
            i=i+1
        return _list_
            

            


    """
    --------------------------------------------------------------------------------
    This function will repurn a sudo-rando list based on the
    initial list provided. Can be used for three types:
    ->int
    ->float
    ->string
    --------------------------------------------------------------------------------
    """
    def use_Sudorandom(_list_, _type_):
        l = []
        for element in _list_:
            if (_type_ == "int"):
                element = random.randint(min(_list_),max(_list_))
            elif (_type_ == "float"):
                element = random.uniform(min(_list_),max(_list_))
            elif (_type_ == "string"):
                element = random.choice(string.lowercase)
            l.append(element)
        return l



    """
    --------------------------------------------------------------------------------
    The use_Boundary will switch the element in the position
    defined to either the largest or smallest element in the list.
    The position of the element must be passed as a parameter
    --------------------------------------------------------------------------------
    """
    def use_Boundary(_list_,pos):
        _list_[pos] = random.choice(max(_list_),min(_list_))
        return _list_


    """
    --------------------------------------------------------------------------------
    The use_Swap function will swap the elements in the two
    specified positions. The positions are passed as arguments
    as well.
    --------------------------------------------------------------------------------
    """
    def use_Swap(_list_, pos_a , pos_b):
        temp = _list_[pos_b]
        _list_[pos_b] = _list_[pos_a]
        _list_[pos_a] = temp
        return _list_


    """
    --------------------------------------------------------------------------------
    This function will invert a segment of the list. The start and
    end of the list segment must be passed to the function in the
    call.
    --------------------------------------------------------------------------------
    """
    def use_Inversion(_list_,start,end):
        _list_[start:end] = (_list_[start:end+1])[::-1]
        return _list_


    """
    --------------------------------------------------------------------------------
    The use_Scramble will get a portion of the list and
    randomize the included elements. The start and end of the
    portion are passed as parameters.
    --------------------------------------------------------------------------------
    """
    def use_Scramble(_list_,start,end):
        _list_[start:end]= random.shuffle(_list_[start:end])
        return _list_



