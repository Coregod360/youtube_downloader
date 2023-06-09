import sys
from datetime import timedelta
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer, QAudioDevice, QMediaDevices)
from PySide6.QtMultimediaWidgets import QVideoWidget
import range_slider

class convert(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shitpost Studio")

        # Player
        self.player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        self.audio_device = QAudioOutput()
        self.player.setAudioOutput(self.audio_device)
        
        self.player.setSource(QtCore.QUrl.fromLocalFile("/home/kensix/deadNiggerStorage/Coding/youtube_downloader/test.webm"))
        
        self.audio_device.setVolume(0.2)
        # self.player.play()

        # Player controls 
        self.play_button = QtWidgets.QPushButton('play')
        self.pause_button = QtWidgets.QPushButton('pause')


        # time slider
        self.time_slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        # TODO: Turn these into variables based on video lenght
        # TODO: Find way to make these more granular seems to be pretty tricky to get them to be precise atm 
        self.time_slider.setMinimumHeight(50)
        self.time_slider.setMinimum(0)
        self.time_slider.setMaximum(100000)
        self.time_slider.setLow(0)
        self.time_slider.setHigh(100000)
        self.time_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.start_time = QtWidgets.QLabel("00:00")
        self.end_time = QtWidgets.QLabel("00:00")

        self.start = 0
        self.end = 100000

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
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.pause_button)

        self.layout.addWidget(self.time_slider)

        self.layout.addWidget(self.start_time)
        self.layout.addWidget(self.end_time)

        self.layout.addWidget(self.preset_select)
        self.layout.addWidget(self.output_field)
        self.layout.addWidget(self.check_box_source)
        self.layout.addWidget(self.ffmpeg_button)

        self.resize(600, 800)

        self.time_slider.sliderMoved.connect(self.updateSlider)
        self.play_button.clicked.connect(self.playVideo)
        self.pause_button.clicked.connect(self.pauseVideo)

        self.player.positionChanged.connect(self.playing)


    @QtCore.Slot()
    # Sets the downloaded video as the media for the player
    def setMedia(self, media):
        self.player.setSource(QtCore.QUrl.fromLocalFile(media))

    def playVideo(self):
        self.player.setPosition(self.start)
        self.player.play()


    def pauseVideo(self):
        # self.player.setPosition(self.start)
        self.player.pause()
    
    def stopVideo(self):
        self.player.stop()

    def updateSlider(self, low_value, high_value):
        self.player.pause()

        if low_value != self.start:        
            self.start_time.setText(str(timedelta(seconds=low_value)))
            self.start = low_value
            self.player.setPosition(self.start)
            print("player position: ", self.player.position())

        if high_value != self.end:
            self.end_time.setText(str(timedelta(seconds=high_value)))
            self.end = high_value
            self.player.setPosition(self.end)
            print("player position: ", self.player.position())

        print('low_value: ', low_value)
        print('high_value: ', high_value)


    def playing(self):
        pass
        if self.player.isPlaying() and self.player.position() >= self.end:
            self.player.setPosition(self.start)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = convert()
    widget.show()

    sys.exit(app.exec())