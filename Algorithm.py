class Algorithm:

	problem_type = ''
	csp_distance = []
	ffmsp_distance = [[]]
	file_name = ""
	objFunction = ObjectiveFunction()
	mutOperator = Mutation()
	currentSolution = []

	def __init__(self, algorithm_type):
		self.algorithm_type = algorithm_type

	def get_solution():
		if algorithm_type == "CSP":
			currentSolution = initRandom()
			fCurr = evaluate(currentSolution)
			while(true):
				mutOperator = mutOperator.mutate(currentSolution)
				fMutateSolution = problem.evaluate(fMutateSolution)

		elif algorithm_type == "FFMSP":
			currentSolution = initRandom()
			fCurr = evaluate(currentSolution)
			while(true):
				mutOperator = mutOperator.mutate(currentSolution)
				fMutateSolution = problem.evaluate(fMutateSolution)

		return currentSolution