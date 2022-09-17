from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImportWindow(object):
    def setupUi(self, ImportWindow):
        ImportWindow.setObjectName("ImportWindow")
        ImportWindow.resize(340, 250)
        self.centralwidget = QtWidgets.QWidget(ImportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 200, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 90, 30))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 90, 25))
        self.pushButton.setObjectName("pushButton")
        
        ImportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        ImportWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImportWindow)
        self.statusbar.setObjectName("statusbar")
        ImportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImportWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportWindow)

    def retranslateUi(self, ImportWindow):
        _translate = QtCore.QCoreApplication.translate
        ImportWindow.setWindowTitle(_translate("ImportWindow", "Импорт"))
        self.label.setText(_translate("ImportWindow", "Введите путь:"))
        self.pushButton.setText(_translate("ImportWindow", "Импорт"))
        


