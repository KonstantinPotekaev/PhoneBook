import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from ExportWindow import Ui_ExportWindow
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

def RebuildMainWindow(d):
	
	for i in range(ui.tableWidget.rowCount()):
		ui.tableWidget.removeRow(i)
	names = [str(x) for x in d]
	ui.tableWidget.setRowCount(len(names))
	for i in range(len(names)):
		item = QtWidgets.QTableWidgetItem(names[i])
		ui.tableWidget.setItem(i,0,item)
		item = QtWidgets.QTableWidgetItem(d[names[i]])
		ui.tableWidget.setItem(i,1,item)

def addNewContact(a, b):
	AddWindow.close()
	d[a] = b
	json_export(d)
	RebuildMainWindow(d,'')

def Export(path):
	print(1)
def Import(path):
	print(2)

def showAddWindow():
	global AddWindow
	AddWindow = QtWidgets.QMainWindow()
	ui_2 = Ui_AddWindow()
	ui_2.setupUi(AddWindow)
	AddWindow.show()
	ui_2.pushButton.clicked.connect(lambda: addNewContact(ui_2.lineEdit.text(), ui_2.lineEdit_2.text()))

def showExportWindow():
	global ExportWindow
	ExportWindow = QtWidgets.QMainWindow()
	ui_3 = Ui_ExportWindow()
	ui_3.setupUi(ExportWindow)
	ExportWindow.show()
	ui_3.pushButton.clicked.connect(lambda: Export(ui_3.lineEdit.text()))

def showImportWindow():
	global ImportWindow
	ImportWindow = QtWidgets.QMainWindow()
	ui_4 = Ui_ExportWindow()
	ui_4.setupUi(ImportWindow)
	ImportWindow.show()
	ui_4.pushButton.clicked.connect(lambda: Import(ui_4.lineEdit.text()))
	
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
		
		RebuildMainWindow(d2,a)

def delete_row():
		row = ui.tableWidget.currentRow()
		del d[ui.tableWidget.item(row,0).text()]
		json_export(d)
		RebuildMainWindow(d, '')

ui.pushButton_2.clicked.connect(showAddWindow)
ui.pushButton.clicked.connect(find)
ui.pushButton_3.clicked.connect(delete_row)
ui.pushButton_5.clicked.connect(showExportWindow)
ui.pushButton_4.clicked.connect(showImportWindow)
sys.exit(app.exec_())
