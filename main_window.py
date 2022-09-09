from PyQt5 import QtCore, QtGui, QtWidgets
import json

with open('data.json', 'r', encoding='utf-8') as f: 
    d = json.load(f) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, d):
        names = [str(x) for x in d]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 100, 600, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(names))
        item = QtWidgets.QTableWidgetItem('ФИО')
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem('Телефон')
        self.tableWidget.setHorizontalHeaderItem(1, item)
        for i in range(len(names)):
            item = QtWidgets.QTableWidgetItem(names[i])
            self.tableWidget.setItem(i,0, item)
        for i in range(len(names)):
            item = QtWidgets.QTableWidgetItem(d[names[i]])
            self.tableWidget.setItem(i,1, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 55, 500, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.FindButton = QtWidgets.QPushButton(self.centralwidget)
        self.FindButton.setGeometry(QtCore.QRect(560, 55, 100, 31))
        self.FindButton.setObjectName("FindButton")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(570, 450, 93, 31))
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(460, 450, 93, 31))
        self.DeleteButton.setObjectName("DeleteButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Functions(self):
        self.AddButton.clicked(self.openAddWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Телефонный справочник"))
        self.FindButton.setText(_translate("MainWindow", "Найти"))
        self.AddButton.setText(_translate("MainWindow", "Добавить"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, d)
    MainWindow.show()
    sys.exit(app.exec_())