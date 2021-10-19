# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(381, 182)
        LoginDialog.setInputMethodHints(Qt.ImhHiddenText)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblEmail = QLabel(LoginDialog)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblEmail)

        self.editEmail = QLineEdit(LoginDialog)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editEmail)

        self.lblParola = QLabel(LoginDialog)
        self.lblParola.setObjectName(u"lblParola")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblParola)

        self.editParola = QLineEdit(LoginDialog)
        self.editParola.setObjectName(u"editParola")
        self.editParola.setInputMethodHints(Qt.ImhNone)
        self.editParola.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editParola)


        self.verticalLayout.addLayout(self.formLayout)

        self.lblMesaj = QLabel(LoginDialog)
        self.lblMesaj.setObjectName(u"lblMesaj")

        self.verticalLayout.addWidget(self.lblMesaj)

        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnIptal = QPushButton(LoginDialog)
        self.btnIptal.setObjectName(u"btnIptal")

        self.horizontalLayout.addWidget(self.btnIptal)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnGiris = QPushButton(LoginDialog)
        self.btnGiris.setObjectName(u"btnGiris")

        self.horizontalLayout.addWidget(self.btnGiris)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LoginDialog)
        self.btnIptal.clicked.connect(LoginDialog.close)
        self.btnGiris.clicked.connect(LoginDialog.giris)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Dialog", None))
        self.lblEmail.setText(QCoreApplication.translate("LoginDialog", u"Email", None))
        self.lblParola.setText(QCoreApplication.translate("LoginDialog", u"Parola", None))
        self.lblMesaj.setText("")
        self.btnIptal.setText(QCoreApplication.translate("LoginDialog", u"Iptal", None))
        self.btnGiris.setText(QCoreApplication.translate("LoginDialog", u"Giris", None))
    # retranslateUi

