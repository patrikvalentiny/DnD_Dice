# qpy:kivy
import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from random import randint

size = 20


class mainWindow(Screen):
    rollButton = ObjectProperty(None)
    mainText = ObjectProperty(None)
    diceCountVar = ObjectProperty(None)
    historyLabel1 = ObjectProperty(None)
    historyLabel2 = ObjectProperty(None)
    historyLabel3 = ObjectProperty(None)
    historyLabel4 = ObjectProperty(None)
    historyLabel5 = ObjectProperty(None)
    historyLabel6 = ObjectProperty(None)
    historyLabel7 = ObjectProperty(None)
    historyLabel8 = ObjectProperty(None)
    historyLabel9 = ObjectProperty(None)
    historyLabel10 = ObjectProperty(None)
    menuButton = ObjectProperty(None)
    menuImage = ObjectProperty(None)
    diceMenu = ObjectProperty(None)
    historyButton = ObjectProperty(None)
    menuImage1 = ObjectProperty(None)
    xImage = ObjectProperty(None)
    xImage1 = ObjectProperty(None)
    closeImage = ObjectProperty(None)
    minusImage = ObjectProperty(None)
    plusImage = ObjectProperty(None)

    diceCount = 1
    historyList = ['' for i in range(10)]
    nord0 = (46 / 255, 52 / 255, 64 / 255, 1)
    nord1 = (59 / 255, 66 / 255, 82 / 255, 1)
    nord2 = (67 / 255, 76 / 255, 94 / 255, 1)
    nord3 = (76 / 255, 86 / 255, 106 / 255, 1)
    nord4 = (216 / 255, 222 / 255, 233 / 255, 1)
    nord5 = (229 / 255, 233 / 255, 240 / 255, 1)
    nord6 = (236 / 255, 239 / 255, 244 / 255, 1)

    def rollValue(self):
        valuelist = []
        value = 0
        for i in range(0, self.diceCount()):
            valuelist.insert(0, randint(1, size))

        for j in range(0, len(valuelist)):
            value += valuelist[j]

        return valuelist, value

    def rollButton_dwn(self):
        if self.diceCount() == None:
            self.mainText.text = 'Nezadaný počet kociek'

        elif 0 < float(self.diceCount()) <= 15:
            valuelist, value = self.rollValue()
            answer = ''
            if len(valuelist) == 1:
                answer += str(valuelist[0]) + ' '
            else:
                for i in range(0, len(valuelist) - 1):
                    answer += str(valuelist[i]) + ' + '
                answer += str(valuelist[-1])

            self.mainText.text = '"' + str(self.diceCount()) + 'xD' + str(size) + '": ' + answer + ' = ' + str(value)
            self.historyList.insert(0, '"' + str(self.diceCount()) + 'xD' + str(size) + '": ' + str(value))

            self.historyLabel1.text = self.historyList[0]
            self.historyLabel2.text = self.historyList[1]
            self.historyLabel3.text = self.historyList[2]
            self.historyLabel4.text = self.historyList[3]
            self.historyLabel5.text = self.historyList[4]
            self.historyLabel6.text = self.historyList[5]
            self.historyLabel7.text = self.historyList[6]
            self.historyLabel8.text = self.historyList[7]
            self.historyLabel9.text = self.historyList[8]
            self.historyLabel10.text = self.historyList[9]


        elif float(self.diceCount()) == 0:
            self.mainText.text = 'Počet kociek je 0'

        elif float(self.diceCount()) < 0:
            self.mainText.text = 'Počet kociek je záporný'
        elif float(self.diceCount()) > 15:
            self.mainText.text = 'Počet kociek je príliš velký'

    def diceSize(self, dice):
        global size
        size = dice
        self.diceCountVar.text = '1'
        self.rollButton.text = 'Hoď ' + str(self.diceCount()) + 'xD' + str(size)

    def diceCount(self):
        if self.diceCountVar.text == '':
            return None
        else:
            count = int(self.diceCountVar.text)
            return count

    def plusButton_down(self):
        self.plusImage.source = 'Icons/plusButton_down.png'

    def plusButton_up(self):
        if self.diceCountVar.text == '':
            self.diceCountVar.text = '1'
        elif float(self.diceCountVar.text) < 15:
            self.diceCountVar.text = str(int(self.diceCountVar.text) + 1)
            self.rollButton.text = 'Hoď ' + str(self.diceCount()) + 'xD' + str(size)
        self.plusImage.source = 'Icons/plusButton.png'

    def minusButton_down(self):
        self.minusImage.source = 'Icons/minusButton_down.png'

    def minusButton_up(self):
        if self.diceCountVar.text == '':
            self.diceCountVar.text = '1'
        elif 1 < float(self.diceCountVar.text) <= 20:
            self.diceCountVar.text = str(int(self.diceCountVar.text) - 1)
            self.rollButton.text = 'Hoď ' + str(self.diceCount()) + 'xD' + str(size)
        self.minusImage.source = 'Icons/minusButton.png'

    def historyButton_down(self):
        self.menuImage1.source = 'Icons/historyButton.png'

    def historyButton_up(self):
        self.menuImage1.source = 'Icons/historyButton_white.png'
        self.historyMenu.pos_hint = {'x': 0.7}
        self.menuButton.disabled = True

    def menuButton_up(self):
        self.menuImage.source = 'Icons/diceButton_white.png'
        self.diceMenu.pos_hint = {'x': 0}
        self.historyButton.disabled = True

    def menuButton_down(self):
        self.menuImage.source = 'Icons/diceButton.png'

    def diceCloseButton_up(self):
        self.xImage.source = 'Icons/xButton_white.png'
        self.xImage1.source = 'Icons/xButton_white.png'
        self.diceMenu.pos_hint = {'x': 1}
        self.historyMenu.pos_hint = {'x': 1}
        self.menuButton.disabled = False
        self.historyButton.disabled = False
        if self.diceCountVar.text == '':
            self.diceCountVar.text = '1'
        else:
            self.rollButton.text = 'Hoď ' + str(self.diceCount()) + 'xD' + str(size)

    def diceCloseButton_down(self):
        self.xImage.source = 'Icons/xButton.png'
        self.xImage1.source = 'Icons/xButton.png'

    def closeButton(self):
        Window.close()

    def closeButton_down(self):
        self.closeImage.source = 'Icons/closeButton_down.png'


kv = Builder.load_file('my.kv')


class DiceApp(App):
    def build(self):
        Window.clearcolor = mainWindow.nord0
        Window.size = (1280, 720)
        Window.left = 320
        Window.top = 180
        return kv


if __name__ == '__main__':
    DiceApp().run()
