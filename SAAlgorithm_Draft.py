

# Initial implementation of the Simulated Annealing Algorithm

import random as r
import math as m
from functions import MinimisingFunction as minfun
from functions import MaximisingFunction as maxfun

# def function(x):
# 	# x^3 - x^2 + 2x - 7
# 	return x ** 3 - x ** 2 + 2 * x - 7

def print_min_fun(a, b):
	y_min = 100000
	y_temp = 0
	x_min = 0
	while a <= b:
		y_temp = function(a)
		if y_temp < y_min:
			y_min = y_temp
			x_min = a
		a = a + 1
	print("The minimum value is y =" + str(y_min) + " in x = " + str(x_min))

# number: the number of random numbers to be discarded
# seed: the seed for the random number generator
def prepare_random_numbers(number, seed):
	r.seed(seed)
	for i in range(number):
		r.random()
	print(r.random())

# function that creates a list of distances from each sequence to a given string
def calculate_hamming_distances(sequences, string):
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

def csp_cost_function(distances):
	return max(distances)

def ffmsp_cost_function(distances, t):
	return len(filter(lambda x: x >= t, distances))


def simulated_annealing():
	iterations = 0
	max_iter = 1

	#Add mutator operator
	x = r.randint(1, 300)
	y = function(x)
	c = 0.3 # Control parameter, defined by the function of Temperature
	x_temp = 0
	y_temp = 0
	energy_change = 0
	while iterations <= max_iter:
		
		#Get random new state
		i_temp = r.randint(1, 100)
		y_temp = function(x)

		#Calculate change of energy
		energy_change = y_temp - y

		#Determining if the random state should be
			#accepted as the new state
		if energy_change <= 0:
			x = x_temp
			y = function(x)
		else:
			#The new state is accepted if a random number is less than
				#the calculated probability
			if m.exp(energy_change / c) > r.random:
				x = x_temp
				y = function(x)
		iterations = iterations + 1
	print("The Global Minimum value calculated after " + str(max_iter) + " iterations is")
	print("x = " + str(x) + " and y = " + str(y))

