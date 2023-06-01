import sys
from PySide6 import QtCore, QtWidgets, QtGui

class progress(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        # Download progress bar
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        
        self.resize(500, 80)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.progress_bar)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = progress()
    widget.show()

    sys.exit(app.exec())

