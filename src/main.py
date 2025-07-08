import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class QuantumCryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quantum Crypto Cryptography')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(self.create_tab('Shor’s Algorithm', 'Demo, explanation, and visualization of Shor’s Algorithm.'), "Shor’s Algorithm")
        tabs.addTab(self.create_tab('ECDSA/Discrete Log Problem', 'Explanation and quantum vulnerability.'), "ECDSA/Discrete Log")
        tabs.addTab(self.create_tab('Post-Quantum Crypto', 'Hash-based, lattice-based, and other schemes.'), "Post-Quantum Crypto")
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

def main():
    app = QApplication(sys.argv)
    window = QuantumCryptoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 