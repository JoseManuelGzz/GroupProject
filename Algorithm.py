class Algorithm:

	problem_type = ''
	csp_distance = []
	ffmsp_distance = [[]]
	file_name = ""
	objFunction = ObjectiveFunction()
	mutOperator = Mutation()
	currentSolution = []

	def __init__(self, problem_type):
		self.problem_type = problem_type

	def get_solution():
		if problem_type == "CSP":
			currentSolution = initRandom()
			fCurr = evaluate(currentSolution)
			while(true):
				mutOperator = mutOperator.mutate(currentSolution)
				fMutateSolution = problem.evaluate(fMutateSolution)

		elif problem_type == "FFMSP":
			currentSolution = initRandom()
			fCurr = evaluate(currentSolution)
			while(true):
				mutOperator = mutOperator.mutate(currentSolution)
				fMutateSolution = problem.evaluate(fMutateSolution)

		return currentSolution