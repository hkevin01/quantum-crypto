import numpy as np
import matplotlib.pyplot as plt
from qiskit import Aer

# Explanation string
EXPLANATION = (
    "Shor's Algorithm is a quantum algorithm for integer factorization. "
    "It can efficiently factor large numbers, threatening classical cryptosystems like RSA. "
    "This demo factors small numbers using Qiskit's simulation tools."
)

def run_shor_demo(N=15):
    from qiskit.algorithms import Shor
    from qiskit.utils import QuantumInstance
    backend = Aer.get_backend('aer_simulator')
    quantum_instance = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=quantum_instance)
    result = shor.factor(N=N)
    return result.factors[0] if result.factors else None

def plot_shor_result(factors):
    # Simple visualization: show the factors
    plt.figure(figsize=(4,2))
    plt.title('Shor\'s Algorithm: Factors')
    plt.bar(['Factor 1', 'Factor 2'], factors)
    plt.ylabel('Value')
    plt.show() 