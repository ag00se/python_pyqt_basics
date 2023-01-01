import sys                                              # Import the needed qt classes
from PySide6.QtWidgets import QApplication, QLabel      
# Alternatively use 'PyQt6'/'PyQt5' or 'PySide2' imports

app = QApplication(sys.argv)                            # Create the main QApplication object
label = QLabel("Hello World!")
label.show()                                            # The label needs to be 'shown' as it is hidden by default
app.exec()                                              # Start the QApplication