import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
import range_slider

class convert(QtWidgets.QWidget):
    def __init__(self, min_time, max_time=100):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        # Player
        self.player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        self.player.setAudioOutput(QAudioOutput())
        self.player.setSource(QtCore.QUrl.fromLocalFile("test.mp4"))
        self.player.play()

        # time slider
        self.time_slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        self.time_slider.setMinimumHeight(30)
        self.time_slider.setMinimum(0)
        self.time_slider.setMaximum(100)
        self.time_slider.setLow(0)
        self.time_slider.setHigh(100)
        self.time_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.start_time = QtWidgets.QLabel("00:00")
        self.end_time = QtWidgets.QLabel("00:00")

        # output preset selector
        self.preset_select = QtWidgets.QComboBox()
        self.preset_select.addItem("source quality")
        self.preset_select.addItem("4chan")
        self.preset_select.addItem("discord")


        # output preset selector 
        # output file name
        self.output_label = QtWidgets.QLabel("Output file name:")
        self.output_field = QtWidgets.QLineEdit(placeholderText="File name", 
                                                alignment=QtCore.Qt.AlignCenter)

        # options - keep_source_file - output_format - etc etc 
        self.check_box_source = QtWidgets.QCheckBox("Keep source file")

        # ffmpeg button
        self.ffmpeg_button = QtWidgets.QPushButton("Convert")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.video_widget)
        self.layout.addWidget(self.time_slider)
        self.layout.addWidget(self.start_time)
        self.layout.addWidget(self.end_time)
        self.layout.addWidget(self.preset_select)
        self.layout.addWidget(self.output_field)
        self.layout.addWidget(self.check_box_source)
        self.layout.addWidget(self.ffmpeg_button)

        self.resize(600, 800)


        self.time_slider.sliderMoved.connect(self.updateSlider)


    @QtCore.Slot()
    # Sets the downloaded video as the media for the player
    def setMedia(self, media):
        print(media)

    def playVideo(self):
        self.player.play()

    def pauseVideo(self):
        self.player.pause()
    
    def stopVideo(self):
        self.player.stop()

    def updateSlider(self, low_value, high_value):
        self.start_time.setText(str(low_value))
        self.end_time.setText(str(high_value))
        print('low_value: ', low_value)
        print('high_value: ', high_value)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = convert()
    widget.show()

    sys.exit(app.exec())