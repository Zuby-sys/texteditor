from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
import sys
from main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()