import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6 import QtCore
# Alternatively use 'PyQt6'/'PyQt5' or 'PySide2' imports

# To create custom window we subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()                                      # initializes the super class

        self.setWindowTitle("Click Counter")                    # set a title for the window
        self.countLabel = QLabel("0")                           # create the count label
        self.countLabel.setAlignment(QtCore.Qt.AlignCenter)     # center the label
        increaseButton = QPushButton("Increase")                # create the increase button
        resetButton = QPushButton("Reset")                      # create the reset button

        layout = QVBoxLayout()                                  # create a layout
        layout.addWidget(self.countLabel)                       # add the label to the layout
        layout.addWidget(increaseButton)                        # add the buttons to the layout
        layout.addWidget(resetButton)
        widget = QWidget()                                      # create a widget
        widget.setLayout(layout)                                # set the layout for the widget
        self.setCentralWidget(widget)                           # set the central widget (will take all available space)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()