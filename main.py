import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
import downloader
import url_window
import progress_window
import clip_window


if __name__ == "__main__":

    # TODO: Add update function that runs on startup to check for updates

    app = QtWidgets.QApplication([])

    url_window = url_window.submit()
    url_window.show()

    while(url_window.isVisible()):
        app.processEvents()
        if(url_window.url != ""):
            print("URL submitted: " + url_window.url_field.text())
            try:
                # TODO: Add a way to pass progress back to the progress window
                # progress_window = progress_window.progress()
                # progress_window.show()
                downloader.yld_download(url_window.url, url_window.update_progress)
        
            except Exception as e:
                print("Error: " + str(e))
                error = QtWidgets.QMessageBox()
                error.setWindowTitle("Error")
                error.setText("Error: " + str(e))
                error.exec()
                sys.exit()
                
            if(url_window.job == "download"):
                # progress_window.close()
                url_window.close()

            if(url_window.job == "convert"):
                # progress_window.close()
                url_window.close()
                # TODO: Add a way to get the video's length in milliseconds   
                # TODO: add a way to get the downloaded video's path
                clip_window = clip_window.convert(0, 366000)
                clip_window.setMedia('/home/kensix/deadNiggerStorage/Coding/youtube_downloader/test.webm')
                clip_window.show()
           

    sys.exit(app.exec())