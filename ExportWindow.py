from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        ExportWindow.setObjectName("ExportWindow")
        ExportWindow.resize(340, 250)
        self.centralwidget = QtWidgets.QWidget(ExportWindow)
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
        
        ExportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        ExportWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExportWindow)
        self.statusbar.setObjectName("statusbar")
        ExportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExportWindow)
        QtCore.QMetaObject.connectSlotsByName(ExportWindow)

    def retranslateUi(self, ExportWindow):
        _translate = QtCore.QCoreApplication.translate
        ExportWindow.setWindowTitle(_translate("ExportWindow", "Экспорт"))
        self.label.setText(_translate("ExportWindow", "Введите путь:"))
        self.pushButton.setText(_translate("ExportWindow", "Экспорт"))
        


