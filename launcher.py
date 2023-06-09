import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import subprocess

class Launcher(QWidget):
    def __init__(self):
        super().__init__()

        # set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(24, 24, 24))
        self.setPalette(p)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Launcher')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel('SALUTE Launcher')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white; font-size: 20px; margin-bottom: 20px;")
        self.layout.addWidget(self.title)

        self.button1 = QPushButton('SALUTE Reports')
        self.button1.setStyleSheet("background-color: rgba(255, 0, 0, 15%); border: 1px solid white; color: white;")
        self.button1.clicked.connect(self.run_app1)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton('Export Reports')
        self.button2.setStyleSheet("background-color: rgba(0, 0, 255, 15%); border: 1px solid white; color: white;")
        self.button2.clicked.connect(self.run_app2)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton('Upload Images')
        self.button3.setStyleSheet("background-color: rgba(0, 255, 0, 15%); border: 1px solid white; color: white;")
        self.button3.clicked.connect(self.run_app3)
        self.layout.addWidget(self.button3)

    def run_app1(self):
        subprocess.Popen(['cmd', '/C', 'start', 'cmd', '/K',
                          r'python -m streamlit run SALUTE.py'])

    def run_app2(self):
        subprocess.Popen(['cmd', '/C', 'start', 'cmd', '/K',
                          r'python -m streamlit run export_SALUTE.py'])

    def run_app3(self):
        subprocess.Popen(['cmd', '/C', 'start', 'cmd', '/K',
                          r'python -m streamlit run upload_images.py'])


def main():
    app = QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
