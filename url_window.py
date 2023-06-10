import sys
from PySide6 import QtCore, QtWidgets, QtGui


class submit(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

            self.url = ""
            self.job = ""

            self.setWindowTitle("Shitpost Studio")

            # URL input
            self.url_label = QtWidgets.QLabel("Enter your URL:")
            self.url_field = QtWidgets.QLineEdit(placeholderText="URL", 
                                                alignment=QtCore.Qt.AlignCenter)
            self.download_button = QtWidgets.QPushButton("Download")
            self.convert_button = QtWidgets.QPushButton("Convert")

            # self.progress_bar = QtWidgets.QProgressBar()

            self.download_button.clicked.connect(self.download)
            self.convert_button.clicked.connect(self.convert)

            self.resize(500, 80)

            self.layout = QtWidgets.QHBoxLayout(self)
            self.layout.addWidget(self.url_label)
            self.layout.addWidget(self.url_field)
            self.layout.addWidget(self.download_button)
            self.layout.addWidget(self.convert_button)
            # self.layout.addWidget(self.progress_bar)


    @QtCore.Slot()
    def download(self):
        print('download button clicked')
        self.url = self.url_field.text()
        self.job = "download"
        
    

    def convert(self):
        print('convert button clicked')
        self.url = self.url_field.text()
        self.job = "convert"


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = submit()
    widget.show()

    sys.exit(app.exec())