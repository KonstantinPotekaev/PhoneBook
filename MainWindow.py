from ast import Delete
from re import A
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from utils import json_export, json_import
class Ui_MainWindow(object):
	def setupUi(self, MainWindow, searhtext):

		


		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(706, 545)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(60, 100, 600, 340))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem('ФИО')
		self.tableWidget.setHorizontalHeaderItem(0,item)
		item = QtWidgets.QTableWidgetItem('Телефон')
		self.tableWidget.setColumnWidth(0,300)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setHorizontalHeaderItem(1,item)
		#self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		
		
		
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(60, 55, 500, 30))
		self.lineEdit.setText(searhtext)
		self.lineEdit.setObjectName("lineEdit")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(560, 55, 100, 30))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(570, 450, 93, 30))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(460, 450, 93, 31))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setGeometry(QtCore.QRect(60, 450, 93, 30))
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_5.setGeometry(QtCore.QRect(170, 450, 93, 30))
		self.pushButton_5.setObjectName("pushButton_5")
		

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

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Телефонный справочник"))
		self.pushButton.setText(_translate("MainWindow", "Найти"))
		self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
		self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
		self.pushButton_4.setText(_translate("MainWindow", 'Импорт'))
		self.pushButton_5.setText(_translate("MainWindow", 'Экспорт'))



	
