import tkinter
from tkinter import *
from tkinter.ttk import *
from configparser import *


def SaveConfigs():
    file1=open(fGameIniPath, 'w')
    file2=open(fGameUserSettingsIniPath, 'w')
    file1.write(gameIni.get("1.0", END))
    file2.write(gameUserSettingsIni.get("1.0", END))
    file1.close()
    file2.close()



mainWindow = Tk()
mainWindow.title("ArkControlClient")
mainWindow.geometry("1024x768")

nb = Notebook(mainWindow)
gameIni = Text(nb)
gameUserSettingsIni = Text(nb)
nb.add(gameIni, text='Game.ini')
nb.add(gameUserSettingsIni, text='GameUserSettings.ini')
nb.pack(fill='both', expand='yes')

config = ConfigParser()
config.read('conf.ini')

fGameIniPath=config['main']['GameUserSettingsIniPath'] + '\\' + 'Game.ini'
fGameUserSettingsIniPath=config['main']['GameUserSettingsIniPath'] + '\\' + 'GameUserSettings.ini'

fGameIni = open(fGameIniPath)
fGameUserSettingsIni = open(fGameUserSettingsIniPath)

gameIni.insert(1.0, fGameIni.read())
gameUserSettingsIni.insert(1.0, fGameUserSettingsIni.read())

fGameIni.close()
fGameUserSettingsIni.close()

buttonSave = Button(mainWindow, text='Save', command=SaveConfigs)
buttonSave.pack()

mainWindow.mainloop()

