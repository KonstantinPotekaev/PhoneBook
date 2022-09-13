from ast import Add
from tkinter.tix import InputOnly
from turtle import goto
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from AddWindow import Ui_AddWindow
import sys
import json
from utils import json_export, json_import

d = json_import()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow, d, '')
MainWindow.show()

def addNewContact(a, b):
	global MainWindow
	AddWindow.close()
	d[a] = b
	json_export(d)
	MainWindow.close()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow, d, '')
	MainWindow.show()


def showAddWindow():
	global AddWindow
	AddWindow = QtWidgets.QMainWindow()
	ui = Ui_AddWindow()
	ui.setupUi(AddWindow)
	AddWindow.show()
	ui.pushButton.clicked.connect(lambda: addNewContact(ui.lineEdit.text(), ui.lineEdit_2.text()))
	
def find():
		a = ui.lineEdit.text().lower()
		print(a)
		d2 = {}
		if (a!=''):
			names = [str(x) for x in d]
			search = []
			for i in names:
				if (i.lower().find(a)!=-1):
					d2[i] = d[i]
			print(d2)
		else:
			d2 = json_import()
			print(d2)
		
		ui.setupUi(MainWindow,d2, '')

def delete_row():
		row = ui.tableWidget.currentRow()
		del d[ui.tableWidget.item(row,0).text()]
		json_export(d)
		if (row>0):
			ui.tableWidget.removeRow(row)

ui.pushButton_2.clicked.connect(showAddWindow)
ui.pushButton.clicked.connect(lambda: find())
ui.pushButton_3.clicked.connect(delete_row)

sys.exit(app.exec_())
