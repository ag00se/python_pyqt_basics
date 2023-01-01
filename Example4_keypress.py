import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6 import QtCore
# Alternatively use 'PyQt6'/'PyQt5' or 'PySide2' imports

# To create custom window we Subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Event Demo")
        self.label = QLabel("0")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)
                
    def keyPressEvent(self, e):                                  # override the keyPressEvent of the parent class
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key.Key_R:
            self.label.setText(str(random.randint(1,1000)))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
