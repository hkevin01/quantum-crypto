import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute

# Explanation string
EXPLANATION = (
    "Shor's Algorithm is a quantum algorithm for integer factorization. "
    "It can efficiently factor large numbers, threatening classical cryptosystems like RSA. "
    "This demo factors 15 using Qiskit's simulation tools."
)

def run_shor_demo():
    # For educational purposes, we use Qiskit's built-in Shor algorithm for factoring 15
    from qiskit.algorithms import Shor
    from qiskit.utils import QuantumInstance
    backend = Aer.get_backend('aer_simulator')
    quantum_instance = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=quantum_instance)
    result = shor.factor(N=15)
    return result.factors[0] if result.factors else None

def plot_shor_result():
    # Simple visualization: show the factors of 15
    factors = run_shor_demo()
    plt.figure(figsize=(4,2))
    plt.title('Shor\'s Algorithm: Factors of 15')
    plt.bar(['Factor 1', 'Factor 2'], factors)
    plt.ylabel('Value')
    plt.show() 