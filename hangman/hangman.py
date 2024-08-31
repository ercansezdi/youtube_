from PyQt5.QtWidgets import *
import sys
from main_ui import Ui_MainWindow
import os 
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.verbose = True


        self.ui.tahmin_linedit.setMaxLength(1)
        self.ui.tahmin_butonu.clicked.connect(self.tahmin_et)

        self.setupGame()



    def setupGame(self):
        self.ui.tahmin_linedit.setEnabled(True)
        self.ui.tahmin_butonu.setText("Tahmin Et")
        self.tahmin_kelimesi = self.kelime_ver()
        self.tahmin_kelimesi = self.tahmin_kelimesi.lower()
        self.kullanici_tahmin = ['_' for i in range(len(self.tahmin_kelimesi))]
        self.hak_sayisi = 5
        self.ui.hak_sayisi.setText(str(self.hak_sayisi))

        self.edit_tahminler_frame(len(self.tahmin_kelimesi))



    def edit_tahminler_frame(self,tahmin_kelime):
        for i in range(self.ui.horizontalLayout_2.count()):
            self.ui.horizontalLayout_2.itemAt(i).widget().deleteLater()

        for i in range(tahmin_kelime):
            self.label_3 = QLabel(self.ui.tahminler_frame)
            self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
    "font: 75 36pt \"MS Shell Dlg 2\";")
            self.label_3.setObjectName("tahminx_" + str(i))
            self.label_3.setText("_")
            self.ui.horizontalLayout_2.addWidget(self.label_3)



    def tahmin_et(self):
        if self.ui.tahmin_butonu.text() == "Tekrar Oyna":
            self.setupGame()
            return
        kelime  = self.ui.tahmin_linedit.text()
        kelime = kelime.lower()

        self.ui.tahmin_linedit.clear()
        if kelime == "" or kelime.isnumeric():
            return
        

        if kelime in self.tahmin_kelimesi:
            for i in range(len(self.tahmin_kelimesi)):
                if self.tahmin_kelimesi[i] == kelime:
                    self.kullanici_tahmin[i] = kelime
                    self.ui.horizontalLayout_2.itemAt(i).widget().setText(kelime)
            
            if not "_" in self.kullanici_tahmin:
                self.game_win()
        else:
            self.hak_sayisi -= 1
            self.ui.hak_sayisi.setText(str(self.hak_sayisi))

            if self.hak_sayisi == 0:
                self.game_over()
    def game_over(self):
        self.ui.tahmin_linedit.setEnabled(False)
        self.ui.tahmin_butonu.setText("Tekrar Oyna")

        QMessageBox.information(self, "Oyun Bitti", "Oyun Bitti. Doğru kelime: " + self.tahmin_kelimesi)


    def game_win(self):
        self.ui.tahmin_linedit.setEnabled(False)
        self.ui.tahmin_butonu.setText("Tekrar Oyna")
        self.kullanici_tahmin = []

        QMessageBox.information(self, "Oyun Bitti", "Tebrikler Kazandınız")



    def kelime_ver(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'material', 'words.csv'))
        with open(path, 'r', encoding='utf-8') as file:
            words = file.readlines()
            word = words[randint(0, len(words)-1)].strip()
            if self.verbose:
                print(word)
            return word
    







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())