"""
<class name>: <class description/objective>
        (?)<subclass name>: <subclass description/objective>
"""
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

	"""
        <func_name>
                <description>
                parameters:
                        <param-1> - 
                returns:
                        <description>

    """
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