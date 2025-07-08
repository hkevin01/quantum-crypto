import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from src import ecdsa_discrete_log, post_quantum_crypto, shor_demo


class QuantumCryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quantum Crypto Cryptography')
        self.setGeometry(100, 100, 700, 600)  # Reduced width from 800 to 700
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(self.create_shor_tab(), "Shor’s Algorithm")
        tabs.addTab(self.create_ecdsa_tab(), "ECDSA/Discrete Log")
        tabs.addTab(self.create_post_quantum_tab(), "Post-Quantum Crypto")
        tabs.addTab(self.create_tab('Interactive Demos', 'Run, visualize, and compare cryptosystems.'), "Interactive Demos")
        tabs.addTab(self.create_tab('References', 'Curated resources and further reading.'), "References")
        self.setCentralWidget(tabs)

    def create_tab(self, title, description):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>{title}</h2>'))
        layout.addWidget(QLabel(description))
        widget.setLayout(layout)
        return widget

    def create_shor_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>Shor’s Algorithm</h2>'))
        layout.addWidget(QLabel(shor_demo.EXPLANATION))
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Number to factor (N):'))
        n_input = QLineEdit()
        n_input.setPlaceholderText('e.g. 15')
        input_layout.addWidget(n_input)
        layout.addLayout(input_layout)
        result_label = QLabel('')
        def run_shor():
            try:
                N = int(n_input.text())
                if N < 3 or N > 21:
                    raise ValueError('N should be between 3 and 21 for demo.')
                factors = shor_demo.run_shor_demo(N)
                if factors:
                    result_label.setText(f'Factors of {N}: {factors[0]} and {factors[1]}')
                    shor_demo.plot_shor_result(factors)
                else:
                    result_label.setText('No factors found.')
            except Exception as e:
                QMessageBox.warning(widget, 'Error', str(e))
        btn = QPushButton('Run Shor’s Algorithm Demo')
        btn.clicked.connect(run_shor)
        layout.addWidget(btn)
        layout.addWidget(result_label)
        widget.setLayout(layout)
        return widget

    def create_ecdsa_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>ECDSA/Discrete Log Problem</h2>'))
        layout.addWidget(QLabel(ecdsa_discrete_log.EXPLANATION))
        # Interactive demo: user picks base g, exponent x, modulus p
        demo_layout = QHBoxLayout()
        demo_layout.addWidget(QLabel('Base (g):'))
        g_input = QLineEdit()
        g_input.setPlaceholderText('e.g. 5')
        demo_layout.addWidget(g_input)
        demo_layout.addWidget(QLabel('Exponent (x):'))
        x_input = QLineEdit()
        x_input.setPlaceholderText('e.g. 3')
        demo_layout.addWidget(x_input)
        demo_layout.addWidget(QLabel('Modulus (p):'))
        p_input = QLineEdit()
        p_input.setPlaceholderText('e.g. 23')
        demo_layout.addWidget(p_input)
        layout.addLayout(demo_layout)
        dlog_result = QLabel('')
        def run_dlog():
            try:
                g = int(g_input.text())
                x = int(x_input.text())
                p = int(p_input.text())
                y = pow(g, x, p)
                dlog_result.setText(f'{g} ^ {x} mod {p} = {y}\nTry to recover x from g, y, p (hard classically, easy for quantum).')
            except Exception as e:
                QMessageBox.warning(widget, 'Error', str(e))
        dlog_btn = QPushButton('Compute g^x mod p')
        dlog_btn.clicked.connect(run_dlog)
        layout.addWidget(dlog_btn)
        layout.addWidget(dlog_result)
        layout.addWidget(QLabel(ecdsa_discrete_log.placeholder_demo()))
        widget.setLayout(layout)
        return widget

    def create_post_quantum_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>Post-Quantum Crypto</h2>'))
        layout.addWidget(QLabel(post_quantum_crypto.EXPLANATION))
        layout.addWidget(QLabel('<b>Hash-based:</b> ' + post_quantum_crypto.HASH_BASED_EXPLANATION))
        # Hash-based signature demo
        hash_layout = QHBoxLayout()
        hash_layout.addWidget(QLabel('Message:'))
        hash_input = QLineEdit()
        hash_input.setPlaceholderText('Type a message')
        hash_layout.addWidget(hash_input)
        sign_btn = QPushButton('Sign')
        verify_btn = QPushButton('Verify')
        hash_signature_label = QLabel('')
        hash_verify_label = QLabel('')
        def sign_hash():
            msg = hash_input.text()
            sig = post_quantum_crypto.toy_hash_sign(msg)
            hash_signature_label.setText(f'Signature: {sig}')
        def verify_hash():
            msg = hash_input.text()
            sig = hash_signature_label.text().replace('Signature: ', '')
            valid = post_quantum_crypto.toy_hash_verify(msg, sig)
            hash_verify_label.setText('Valid signature!' if valid else 'Invalid signature!')
        sign_btn.clicked.connect(sign_hash)
        verify_btn.clicked.connect(verify_hash)
        hash_layout.addWidget(sign_btn)
        hash_layout.addWidget(verify_btn)
        layout.addLayout(hash_layout)
        layout.addWidget(hash_signature_label)
        layout.addWidget(hash_verify_label)
        layout.addWidget(QLabel('<b>Lattice-based:</b> ' + post_quantum_crypto.LATTICE_BASED_EXPLANATION))
        # Lattice-based encryption demo
        lattice_layout = QHBoxLayout()
        lattice_layout.addWidget(QLabel('Message:'))
        lattice_input = QLineEdit()
        lattice_input.setPlaceholderText('Type a message')
        lattice_layout.addWidget(lattice_input)
        encrypt_btn = QPushButton('Encrypt')
        decrypt_btn = QPushButton('Decrypt')
        lattice_cipher_label = QLabel('')
        lattice_plain_label = QLabel('')
        cipher = {'value': None}
        def encrypt_lattice():
            msg = lattice_input.text()
            c = post_quantum_crypto.toy_lattice_encrypt(msg)
            cipher['value'] = c
            lattice_cipher_label.setText(f'Ciphertext: {c}')
        def decrypt_lattice():
            c = cipher['value']
            if c is not None:
                plain = post_quantum_crypto.toy_lattice_decrypt(c)
                lattice_plain_label.setText(f'Decrypted: {plain}')
            else:
                lattice_plain_label.setText('No ciphertext to decrypt.')
        encrypt_btn.clicked.connect(encrypt_lattice)
        decrypt_btn.clicked.connect(decrypt_lattice)
        lattice_layout.addWidget(encrypt_btn)
        lattice_layout.addWidget(decrypt_btn)
        layout.addLayout(lattice_layout)
        layout.addWidget(lattice_cipher_label)
        layout.addWidget(lattice_plain_label)
        layout.addWidget(QLabel(post_quantum_crypto.placeholder_demo()))
        widget.setLayout(layout)
        return widget

def main():
    app = QApplication(sys.argv)
    window = QuantumCryptoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 