from re import X
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from ExportWindow import Ui_ExportWindow
from MainWindow import Ui_MainWindow
from AddWindow import Ui_AddWindow
from ImportWindow import Ui_ImportWindow
import sys
import json
from utils import json_export, json_import
from pathlib import*
from Utils.JsonInOut import*
from Utils.TxtInOut import*
from Utils.XmlInOut import*



def Import(path):
	ImportWindow.close()
	if (Path(path).suffix == '.json'):
		contacts = json_Import(path)
	if (Path(path).suffix == '.xml'):
		contacts = xml_Import(path)
	if (Path(path).suffix == '.txt'):
		contacts = txt_Import(path)
	json_export(contacts)
	RebuildMainWindow(contacts)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow, '')
MainWindow.show()

def RebuildMainWindow(data):
	
	for i in range(ui.tableWidget.rowCount()):
		ui.tableWidget.removeRow(i)
	names = [str(x) for x in data]
	ui.tableWidget.setRowCount(len(names))
	for i in range(len(names)):
		item = QtWidgets.QTableWidgetItem(names[i])
		ui.tableWidget.setItem(i,0,item)
		item = QtWidgets.QTableWidgetItem(data[names[i]])
		ui.tableWidget.setItem(i,1,item)

def addNewContact(a, b):
	AddWindow.close()
	d = json_import()
	d[a] = b
	json_export(d)
	RebuildMainWindow(d)

def Export(path):
	ExportWindow.close()
	d = json_import()
	if (Path(path).suffix == '.json'):
		contacts = json_Export(path,d)
	if (Path(path).suffix == '.xml'):
		contacts = xml_Export(path,d)
	if (Path(path).suffix == '.txt'):
		contacts = txt_Export(path,d)


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
	ui_4 = Ui_ImportWindow()
	ui_4.setupUi(ImportWindow)
	ImportWindow.show()
	ui_4.pushButton.clicked.connect(lambda: Import(ui_4.lineEdit.text()))
	
def find():
		d = json_import()
		a = ui.lineEdit.text().lower()
		
		d2 = {}
		if (a!=''):
			names = [str(x) for x in d]
			search = []
			for i in names:
				if (i.lower().find(a)!=-1):
					d2[i] = d[i]
			
		else:
			d2 = json_import()
			
		
		RebuildMainWindow(d2)

def delete_row():
		d = json_import()
		row = ui.tableWidget.currentRow()
		del d[ui.tableWidget.item(row,0).text()]
		json_export(d)
		RebuildMainWindow(d)

ui.pushButton_2.clicked.connect(showAddWindow)
ui.pushButton.clicked.connect(find)
ui.pushButton_3.clicked.connect(delete_row)
ui.pushButton_5.clicked.connect(showExportWindow)
ui.pushButton_4.clicked.connect(showImportWindow)
sys.exit(app.exec_())
