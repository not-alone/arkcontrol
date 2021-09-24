from tkinter import *
from tkinter.ttk import *
from configparser import *

mainWindow = Tk()
mainWindow.title("ArkControlClient")
mainWindow.geometry("1024x768")

nb = Notebook(mainWindow)
gameIni = Text(nb)
gameUserSettingsIni = Text(nb)


nb.add(gameIni, text='Game.ini')
nb.add(gameUserSettingsIni, text='GameUserSettings.ini')
nb.pack(fill='both', expand='yes')

config=ConfigParser()
config.read('conf.ini')
fGameIni = open(config['main']['GameUserSettingsIniPath'] + '\\' + 'Game.ini')
fGameUserSettingsIni = open(config['main']['GameUserSettingsIniPath'] + '\\' + 'GameUserSettings.ini')

gameIni.insert(1.0, fGameIni.read())
gameUserSettingsIni.insert(1.0, fGameUserSettingsIni.read())

fGameIni.close()
fGameUserSettingsIni.close()
mainWindow.mainloop()
