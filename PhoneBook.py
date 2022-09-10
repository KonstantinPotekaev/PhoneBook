from ast import Add
from tkinter.tix import InputOnly
from turtle import goto
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from AddWindow import Ui_AddWindow
import sys
import json
from utils import json_export

with open('data.json', 'r', encoding='utf-8') as fh: 
	d = json.load(fh)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow, d)
MainWindow.show()

def addNewContact(a, b):
	AddWindow.close()
	d[a] = b
	json_export(d)
	print(d)
	ui.setupUi(MainWindow, d)


def showAddWindow():
	global AddWindow
	AddWindow = QtWidgets.QMainWindow()
	ui = Ui_AddWindow()
	ui.setupUi(AddWindow)
	AddWindow.show()
	ui.pushButton.clicked.connect(lambda: addNewContact(ui.lineEdit.text(), ui.lineEdit_2.text()))
	


ui.pushButton_2.clicked.connect(showAddWindow)


sys.exit(app.exec_())
