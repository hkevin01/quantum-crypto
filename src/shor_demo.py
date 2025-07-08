import matplotlib.pyplot as plt
import numpy as np
from qiskit_aer import Aer

# Explanation string
EXPLANATION = (
    "Shor's Algorithm is a quantum algorithm for integer factorization. "
    "It can efficiently factor large numbers, threatening classical cryptosystems like RSA. "
    "This demo factors small numbers using Qiskit's simulation tools."
)

def run_shor_demo(N=15):
    from qiskit_algorithms import Shor
    from qiskit_primitives import BackendSampler
    backend = Aer.get_backend('aer_simulator')
    sampler = BackendSampler(backend)
    shor = Shor(sampler=sampler)
    result = shor.factor(N=N)
    return result.factors[0] if result.factors else None

def plot_shor_result(factors):
    # Simple visualization: show the factors
    plt.figure(figsize=(4,2))
    plt.title('Shor\'s Algorithm: Factors')
    plt.bar(['Factor 1', 'Factor 2'], factors)
    plt.ylabel('Value')
    plt.show() 