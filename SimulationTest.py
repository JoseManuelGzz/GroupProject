from Simulation import SimulationSA_CSP
from Simulation import SimulationSA_FFMSP

sa_csp = SimulationSA_CSP(10,7,5000,range(0,5),0.75, 'csp', 0.95,200)
sa_csp.get_solution()