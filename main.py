import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtMultimedia
import downloader

class urlRequest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        self.url_field = QtWidgets.QLineEdit(placeholderText="URL", alignment=QtCore.Qt.AlignCenter)

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.url_field)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.resize(400, 250)

        self.url_field.returnPressed.connect(self.urlSubmit)
        self.button.clicked.connect(self.urlSubmit)



    @QtCore.Slot()
    def urlSubmit(self):
        print("URL submitted: " + self.url_field.text())
        self.hide()
        self.dowloadProgress = downloadProgress(10)
        self.dowloadProgress.show()
        downloader.yld_download(self.url_field.text(), 'download')
        # run downloader.py
        # switch to shitpost editor
        

        

class downloadProgress(QtWidgets.QWidget):
    def __init__(self, progress):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        self.progress = progress
        self.progressBar = QtWidgets.QProgressBar()

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                        alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.resize(400, 250)

        

class editor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                        alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.resize(700, 800)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = urlRequest()
    widget.show()

    sys.exit(app.exec())