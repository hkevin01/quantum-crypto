# Post-Quantum Crypto Explanation
EXPLANATION = (
    "Post-quantum cryptography includes cryptosystems believed to be secure against quantum attacks. "
    "Popular approaches include hash-based signatures and lattice-based encryption. "
    "This section will provide demos and visualizations for these schemes."
)

HASH_BASED_EXPLANATION = (
    "Hash-based cryptography uses hash functions to build secure digital signatures. "
    "Examples: XMSS, SPHINCS+."
)

LATTICE_BASED_EXPLANATION = (
    "Lattice-based cryptography relies on the hardness of lattice problems. "
    "Examples: NTRU, Kyber, Dilithium."
)

def placeholder_demo():
    return "Demo coming soon!"

# Toy hash-based signature demo
def toy_hash_sign(message):
    import hashlib
    return hashlib.sha256(message.encode()).hexdigest()

def toy_hash_verify(message, signature):
    return toy_hash_sign(message) == signature

# Toy lattice-based encryption demo (very simplified)
def toy_lattice_encrypt(message, key=7):
    # Just a simple modular addition for demo
    return [(ord(c) + key) % 256 for c in message]

def toy_lattice_decrypt(ciphertext, key=7):
    return ''.join([chr((c - key) % 256) for c in ciphertext]) 