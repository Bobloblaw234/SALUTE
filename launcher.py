import os
import sys
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import subprocess
import urllib.request

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

        self.button1 = QPushButton('Run SALUTE')
        self.button1.setStyleSheet("background-color: rgba(255, 0, 0, 15%); border: 1px solid white; color: white;")
        self.button1.clicked.connect(self.run_app1)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton('Run App 2')
        self.button2.setStyleSheet("background-color: rgba(0, 0, 255, 15%); border: 1px solid white; color: white;")
        self.button2.clicked.connect(self.run_app2)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton('Run App 3')
        self.button3.setStyleSheet("background-color: rgba(0, 255, 0, 15%); border: 1px solid white; color: white;")
        self.button3.clicked.connect(self.run_app3)
        self.layout.addWidget(self.button3)

    def run_app1(self):
        filename = os.path.join(os.path.expanduser("~/Documents/Downloads"), "SALUTE.py")
        if not os.path.exists(filename):
            url = "https://raw.githubusercontent.com/Bobloblaw234/SALUTE/main/SALUTE.py"
            self.download_file(url, filename)
        self.run_app(filename)

    def run_app2(self):
        filename = os.path.join(os.path.expanduser("~/Documents/Downloads"), "export_SALUTE.py")
        if not os.path.exists(filename):
            url = "https://raw.githubusercontent.com/Bobloblaw234/SALUTE/main/export_SALUTE.py"
            self.download_file(url, filename)
        self.run_app(filename)

    def run_app3(self):
        filename = os.path.join(os.path.expanduser("~/Documents/Downloads"), "upload_images.py")
        if not os.path.exists(filename):
            url = "https://raw.githubusercontent.com/Bobloblaw234/SALUTE/main/upload_images.py"
            self.download_file(url, filename)
        self.run_app(filename)

    def download_file(self, url, filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"Error downloading file: {e}")

    def run_app(self, filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])


def main():
    app = QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
