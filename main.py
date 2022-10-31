from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os

pygame.init()
volume = 0.5
pygame.mixer.music.set_volume(volume)  

def open_file():
    global song
    file_name = QFileDialog()
    # file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames( filter='MP3 (*.mp3)' )
    song = names[0]
    ui.listWidget.addItems(song)
    ui.label.setText('Запускай файлы')

def play_song():
    i = ui.listWidget.currentRow()     # i это порядковый номер
    if i == -1:
        error()    
    else:
        melody = ui.listWidget.item(i).text() 
        pygame.mixer.music.load ( melody ) 
        pygame.mixer.music.play()
        ui.label.setText('Играет')

def stop_song():
        pygame.mixer.music.stop()
        ui.label.setText('Стоп')

def error():
    ui.label.setText('ERROR, выберите файлы')
#    victory_win = QMessageBox()
#    victory_win.setText('error')
#    victory_win.exec_()

def volum_up():
    global volume
    if volume < 0.9 :
        volume += 0.1
        ui.label_2.setText( str(round(volume*100)) +'%' )
        pygame.mixer.music.set_volume(volume)  

def volum_down():
    global volume
    if volume > 0.1 :
        volume -= 0.1
        ui.label_2.setText(str(round(volume*100)) +'%')
        pygame.mixer.music.set_volume(volume)  

def save_playlist():
    global song
    import pickle
    f = open('playlist.dat', "wb")
    pickle.dump(song, f)
    f.close()

def load_playlist():
    global song
    import pickle
    f = open('playlist.dat', 'rb')
    song  = pickle.load(f)
    f.close()
    ui.listWidget.addItems(song)

def clear():
    global song
    song = []
    ui.listWidget.clear()

def find():
    global song
    dir = QFileDialog.getExistingDirectory()
    for dir_put, dn, filenames in os.walk(dir):
        for file in filenames:
            if file.endswith('mp3'):
                song.append(os.path.join(dir_put, file))
    ui.listWidget.addItems(song)

song = []

app = QApplication([])
ui = uic.loadUi("interface.html")
ui.setWindowTitle('Mp3 Player')
ui.show()

ui.pushButton.clicked.connect(open_file)
ui.pushButton_2.clicked.connect(play_song)
ui.pushButton_3.clicked.connect(stop_song)

ui.pushButton_5.clicked.connect(volum_up)
ui.pushButton_6.clicked.connect(volum_down)

ui.pushButton_7.clicked.connect(save_playlist)
ui.pushButton_8.clicked.connect(load_playlist)

ui.pushButton_9.clicked.connect(clear)
ui.pushButton_10.clicked.connect(find)

ui.listWidget.itemDoubleClicked.connect(play_song)

app.exec_()