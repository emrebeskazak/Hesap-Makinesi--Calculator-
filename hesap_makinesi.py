import sys
from hesap_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt


class hesap_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(hesap_win, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sonuc = 0
        self.sonuc_str = ""
        self.sonuc_tazeligi = True
        self.ui.pb_esittir.clicked.connect(self.esittir)        
        self.ui.pb_arti.clicked.connect(self.arti)
        self.ui.pb_eksi.clicked.connect(self.eksi)
        self.ui.pb_carpi.clicked.connect(self.carpi)
        self.ui.pb_bolu.clicked.connect(self.bolu)
        self.ui.pb_clear.clicked.connect(self.clear)
        self.ui.pb_duzelt.clicked.connect(self.duzelt)
        self.ui.pb_9.clicked.connect(self.key_9)
        self.ui.pb_8.clicked.connect(self.key_8)
        self.ui.pb_7.clicked.connect(self.key_7)
        self.ui.pb_6.clicked.connect(self.key_6)
        self.ui.pb_5.clicked.connect(self.key_5)
        self.ui.pb_4.clicked.connect(self.key_4)
        self.ui.pb_3.clicked.connect(self.key_3)
        self.ui.pb_2.clicked.connect(self.key_2)
        self.ui.pb_1.clicked.connect(self.key_1)
        self.ui.pb_0.clicked.connect(self.key_0)
        self.ui.pb_nokta.clicked.connect(self.key_comma)
        self.ui.pb_eksile.clicked.connect(self.eksile)
        self.ui.le_sonuc.textChanged.connect(self.c_or_ce)
        self.ui.actionAbout.triggered.connect(self.hakkinda)

    def hakkinda(self):
        msg = QtWidgets.QMessageBox.about(self, "Hakkında", "Emre'nin Hesap Makinesi\nVersion: 2.0\n\nNo rights reserved at all cCc")


    def eksile(self):
        if self.ui.le_sonuc.text() != "0":
            self.ui.le_sonuc.setText(str(float(self.ui.le_sonuc.text())*(-1)))

    def c_or_ce(self):
        if self.ui.le_sonuc.text() != "0":
            self.ui.pb_clear.setText("CE")
        else:
            self.ui.pb_clear.setText("C")

    def pre_key_le_check(self):
        if self.ui.le_sonuc.text() == "0":
                self.ui.le_sonuc.setText("")
        elif self.sonuc_tazeligi:
            if self.ui.le_sonuc.text() == str(self.sonuc):
                self.ui.le_sonuc.setText("")
                self.sonuc_tazeligi = False

    def key_9(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "9")
    def key_8(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "8")
    def key_7(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "7")
    def key_6(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "6")
    def key_5(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "5")
    def key_4(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "4")
    def key_3(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "3")
    def key_2(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "2")
    def key_1(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "1")
    def key_0(self):
        self.pre_key_le_check()
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + "0")
    def key_comma(self):
        if self.ui.le_sonuc.text() == "0" or self.ui.le_sonuc.text() == str(self.sonuc):
            self.ui.le_sonuc.setText("0")
        self.ui.le_sonuc.setText(self.ui.le_sonuc.text() + ".")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.duzelt()
        elif event.key() == Qt.Key_Escape:
            self.clear()
        elif event.key() == Qt.Key_Enter:
            self.esittir()
        elif event.key() == Qt.Key_Plus:
            self.arti()
        elif event.key() == Qt.Key_Minus:
            self.eksi()
        elif event.key() == Qt.Key_Slash:
            self.bolu()
        elif event.key() == Qt.Key_Asterisk:
            self.carpi()
        elif event.key() == Qt.Key_9:
            self.key_9()
        elif event.key() == Qt.Key_8:
             self.key_8()
        elif event.key() == Qt.Key_7:
            self.key_7()
        elif event.key() == Qt.Key_6:
            self.key_6()
        elif event.key() == Qt.Key_5:
            self.key_5()
        elif event.key() == Qt.Key_4:
            self.key_4()
        elif event.key() == Qt.Key_3:
            self.key_3()
        elif event.key() == Qt.Key_2:
            self.key_2()
        elif event.key() == Qt.Key_1:
            self.key_1()
        elif event.key() == Qt.Key_0:
             self.key_0()
        elif event.key() == Qt.Key_Comma:
            self.key_comma()
        elif event.key() == Qt.Key_Period:
            self.key_comma()
          

    def temp_mem(self):
        temp_le = self.ui.le_sonuc.text().strip()
        self.clear()
        self.clear()
        self.ui.le_sonuc.setText(temp_le)
    
    def noktasizlastirici(self):
        self.girdi_temp = []
        self.girdi = ""
        for i in self.ui.le_sonuc.text().strip():
            if i != "." and i != "-":
                self.girdi_temp.append(i) 
        self.girdi = "".join(self.girdi_temp)

    def duzelt(self):
        if self.sonuc_tazeligi == False:
            self.ui.le_sonuc.setText(self.ui.le_sonuc.text()[0:-1])
        elif self.sonuc_str == "":
            pass
        elif (self.sonuc_str[-1] == "="):
            self.sonuc_str=""
            self.ui.lbl_sonuc.setText(self.sonuc_str)
        else:
            pass



    def clear(self):
        if ((self.ui.le_sonuc.text().strip() == "0") or (self.ui.le_sonuc.text().strip() == "") or (self.ui.le_sonuc.text().strip() == "Sıfıra bölünemez") ) :
            self.sonuc = 0
            self.sonuc_str = ""
            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))
            self.ui.pb_arti.setEnabled(True)
            self.ui.pb_eksi.setEnabled(True)
            self.ui.pb_carpi.setEnabled(True)
            self.ui.pb_bolu.setEnabled(True)
            self.ui.pb_esittir.setEnabled(True)            
        else:
            self.ui.le_sonuc.setText("0")


    def islem(self):
        if (self.sonuc_str[-1] == "+"):
            self.sonuc = self.sonuc + float(self.ui.le_sonuc.text().strip())
        elif (self.sonuc_str[-1] == "-"):
            self.sonuc = self.sonuc - float(self.ui.le_sonuc.text().strip())
        elif (self.sonuc_str[-1] == "x"):
            self.sonuc = self.sonuc * float(self.ui.le_sonuc.text().strip())
        elif (self.sonuc_str[-1] == "/"):
            if (float(self.ui.le_sonuc.text().strip()) != 0):
                self.sonuc = self.sonuc / float(self.ui.le_sonuc.text().strip())
            else:
                self.sonuc = "Sıfıra bölünemez"
                self.ui.pb_arti.setDisabled(True)
                self.ui.pb_eksi.setDisabled(True)
                self.ui.pb_carpi.setDisabled(True)
                self.ui.pb_bolu.setDisabled(True)
                self.ui.pb_esittir.setDisabled(True)

        elif (self.sonuc_str[-1] == "="):
            self.sonuc_str = str(self.sonuc)
        else:
            self.ui.le_sonuc.setText("operatör sorunu") 

    def esittir(self):
        self.noktasizlastirici()
        if self.girdi.isdecimal():
            self.sonuc_tazeligi = True
            if (self.sonuc_str == ""):
                self.sonuc_str = self.ui.le_sonuc.text().strip() + " ="
                self.sonuc = float(self.ui.le_sonuc.text().strip())
            else:
                self.islem()                                  
                if (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) == self.sonuc):
                    self.sonuc_str = self.sonuc_str  + " =" 
                elif (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) != self.sonuc):
                    self.temp_mem()
                    self.esittir()
                else:
                    self.sonuc_str = self.sonuc_str  + " " + self.ui.le_sonuc.text().strip() + " ="
            self.sonuc_esit = self.sonuc
            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))

        else:
            self.ui.le_sonuc.setText("")   

    def arti(self):
        # if self.ui.le_sonuc.text().strip().isdecimal():
        self.noktasizlastirici()
        if self.girdi.isdecimal():
            self.sonuc_tazeligi = True
            if (self.sonuc_str == ""):
                self.sonuc_str = self.ui.le_sonuc.text().strip() + " +"
                self.sonuc = float(self.ui.le_sonuc.text().strip())
            else:
                self.islem()
                if (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) == self.sonuc):
                    self.sonuc_str = self.sonuc_str  + " +" 
                elif (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) != self.sonuc):
                    self.temp_mem()
                    self.arti()
                else:
                    self.sonuc_str = self.sonuc_str  + " " + self.ui.le_sonuc.text().strip() + " +"

            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))

        else:
            self.ui.le_sonuc.setText("")                


    def eksi(self):
        self.noktasizlastirici()
        if self.girdi.isdecimal():
            self.sonuc_tazeligi = True
            if (self.sonuc_str == ""):
                self.sonuc_str = self.ui.le_sonuc.text().strip() + " -"
                self.sonuc = float(self.ui.le_sonuc.text().strip())
            else:
                self.islem()                                  
                if (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) == self.sonuc):
                    self.sonuc_str = self.sonuc_str  + " -" 
                elif (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) != self.sonuc):
                    self.temp_mem()
                    self.eksi()
                else:
                    self.sonuc_str = self.sonuc_str  + " " + self.ui.le_sonuc.text().strip() + " -"

            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))

        else:
            self.ui.le_sonuc.setText("")      

    def carpi(self):
        self.noktasizlastirici()
        if self.girdi.isdecimal():
            self.sonuc_tazeligi = True
            if (self.sonuc_str == ""):
                self.sonuc_str = self.ui.le_sonuc.text().strip() + " x"
                self.sonuc = float(self.ui.le_sonuc.text().strip())
            else:
                self.islem()                                  
                if (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) == self.sonuc):
                    self.sonuc_str = self.sonuc_str  + " x" 
                elif (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) != self.sonuc):
                    self.temp_mem()
                    self.carpi()
                else:
                    self.sonuc_str = self.sonuc_str  + " " + self.ui.le_sonuc.text().strip() + " x"

            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))

        else:
            self.ui.le_sonuc.setText("")    

    def bolu(self):
        self.noktasizlastirici()
        if self.girdi.isdecimal():
            self.sonuc_tazeligi = True
            if (self.sonuc_str == ""):
                self.sonuc_str = self.ui.le_sonuc.text().strip() + " /"
                self.sonuc = float(self.ui.le_sonuc.text().strip())
            else:
                self.islem()                                  
                if (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) == self.sonuc):
                    self.sonuc_str = self.sonuc_str  + " /" 
                elif (self.sonuc_str == str(self.sonuc) ) and (float(self.ui.le_sonuc.text().strip()) != self.sonuc):
                    self.temp_mem()
                    self.bolu()
                else:
                    self.sonuc_str = self.sonuc_str  + " " + self.ui.le_sonuc.text().strip() + " /"

            self.ui.lbl_sonuc.setText(self.sonuc_str)
            self.ui.le_sonuc.setText(str(self.sonuc))

        else:
            self.ui.le_sonuc.setText("")  



app = QtWidgets.QApplication(sys.argv)
win = hesap_win()

win.show()
sys.exit(app.exec_())