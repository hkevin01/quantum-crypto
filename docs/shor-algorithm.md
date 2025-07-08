# Shor's Algorithm

Shor's Algorithm is a quantum algorithm for integer factorization, threatening classical cryptosystems like RSA. It leverages quantum parallelism and the Quantum Fourier Transform to efficiently find the period of a function, which is the key to factoring.

## Steps
1. Pick a composite number N to factor.
2. Choose a random integer a < N.
3. Use quantum circuits to find the period r of the function f(x) = a^x mod N.
4. If r is even and a^(r/2) ≠ -1 mod N, compute gcd(a^(r/2) ± 1, N) to get a factor.

## Impact
- Efficiently factors large numbers.
- Breaks RSA and other public-key cryptosystems.

## Demo
See the Shor's Algorithm tab in the app for a live demo. 