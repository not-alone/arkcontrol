from tkinter import *
from tkinter.ttk import *
from configparser import *
import tkinter.font as tkfont

class MainWindow():
    def SaveConfigs(self):
        self._file1 = open(self._fGameIniPath, 'w')
        self._file2 = open(self._fGameUserSettingsIniPath, 'w')
        self._file1.write(self._gameIni.get("1.0", END))
        self._file2.write(self._gameUserSettingsIni.get("1.0", END))
        self._file1.close()
        self._file2.close()

    def __init__(self):
        self._config = ConfigParser()
        self._config.read('conf.ini')
        self._fontSize = self._config['main']['FontSize']

        self.mainWindow = Tk()

        self._default_font = tkfont.nametofont("TkDefaultFont")
        self._default_font.configure(size=self._fontSize)

        self._default_font2 = tkfont.nametofont("TkFixedFont")
        self._default_font2.configure(size=self._fontSize)

        # mainWindow.option_add("*Font", default_font)

        self.mainWindow.title("ArkControlClient", )
        self.mainWindow.geometry("1024x768")
        # mainWindow.option_add("*Font", ('Verdana', 30))

        self._menubar = Menu(self.mainWindow)
        self.mainWindow.config(menu=self._menubar)
        self._menubar.add_command(label='SAVE', command=self.SaveConfigs)

        self._nb = Notebook(self.mainWindow)
        self._gameIni = Text(self._nb)
        self._gameUserSettingsIni = Text(self._nb)
        self._nb.add(self._gameIni, text='Game.ini')
        self._nb.add(self._gameUserSettingsIni, text='GameUserSettings.ini')
        self._nb.pack(fill='both', expand='yes')

        self._fGameIniPath = self._config['main']['GameUserSettingsIniPath'] + '\\' + 'Game.ini'
        self._fGameUserSettingsIniPath = self._config['main']['GameUserSettingsIniPath'] + '\\' + 'GameUserSettings.ini'

        self._fGameIni = open(self._fGameIniPath)
        self._fGameUserSettingsIni = open(self._fGameUserSettingsIniPath)

        self._gameIni.insert(1.0, self._fGameIni.read().strip())
        self._gameUserSettingsIni.insert(1.0, self._fGameUserSettingsIni.read().strip())

        self._fGameIni.close()
        self._fGameUserSettingsIni.close()

        self._sbGameIni = Scrollbar(self._gameIni, command=self._gameIni.yview)
        self._sbGameUserSettingsIni = Scrollbar(self._gameUserSettingsIni, command=self._gameUserSettingsIni.yview)
        self._sbGameIni.pack(side=RIGHT, fill=Y)
        self._sbGameUserSettingsIni.pack(side=RIGHT, fill=Y)

window=MainWindow()

window.mainWindow.mainloop()


