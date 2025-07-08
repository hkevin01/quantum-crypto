import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton
from src import shor_demo, ecdsa_discrete_log, post_quantum_crypto

class QuantumCryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quantum Crypto Cryptography')
        self.setGeometry(100, 100, 800, 600)
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
        btn = QPushButton('Run Shor’s Algorithm Demo')
        btn.clicked.connect(shor_demo.plot_shor_result)
        layout.addWidget(btn)
        widget.setLayout(layout)
        return widget

    def create_ecdsa_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>ECDSA/Discrete Log Problem</h2>'))
        layout.addWidget(QLabel(ecdsa_discrete_log.EXPLANATION))
        layout.addWidget(QLabel(ecdsa_discrete_log.placeholder_demo()))
        widget.setLayout(layout)
        return widget

    def create_post_quantum_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'<h2>Post-Quantum Crypto</h2>'))
        layout.addWidget(QLabel(post_quantum_crypto.EXPLANATION))
        layout.addWidget(QLabel('<b>Hash-based:</b> ' + post_quantum_crypto.HASH_BASED_EXPLANATION))
        layout.addWidget(QLabel('<b>Lattice-based:</b> ' + post_quantum_crypto.LATTICE_BASED_EXPLANATION))
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