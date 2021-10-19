import sys
from PySide6 import QtWidgets
import app
from db.models import Kisi
from db import session

from gui import Ui_LoginDialog


class MainWindow(QtWidgets.QDialog, Ui_LoginDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def giris(self):
        kisi = session.query(Kisi).filter_by(email=self.editEmail.text()).first()
        if kisi is None:
            print("kisi bulunamadi")
        else:
            durum = kisi.parola_kontrol(self.editParola.text())
            if durum:
                self.lblMesaj.setText("Basarili")
                print("basarili")
            else:
                self.lblMesaj.setText("Basarisiz")
                print("basarisiz")

        pass

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
