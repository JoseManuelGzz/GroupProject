from Simulation import SimulationSA_CSP
from Simulation import SimulationSA_FFMSP
from Simulation import SimulationMCM_CSP
from Simulation import SimulationMCM_FFMSP
from Simulation import SimulationEv_CSP
from Simulation import SimulationEv_FFMSP

sa_csp = SimulationSA_CSP(10,7,5000,range(0,5),0.75,'RandomFlip', 0.95,200)
sa_csp.get_solution()

sa_ffmsp = SimulationSA_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip', 0.95,200)
sa_ffmsp.get_solution()

mcm_csp = SimulationMCM_CSP(10,7,5000,range(0,5),0.75,'RandomFlip',0.95,200)
mcm_csp.get_solution()

mcm_ffmsp = SimulationMCM_FFMSP(10,7,5000,range(0,5),0.75,'RandomFlip',0.95,200)
mcm_ffmsp.get_solution()

