# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imit_mod1_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 381, 61))
        self.label.setObjectName("label")
        self.Compute = QtWidgets.QPushButton(self.centralwidget)
        self.Compute.setGeometry(QtCore.QRect(10, 540, 181, 91))
        self.Compute.setObjectName("Compute")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 371, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.M = QtWidgets.QLineEdit(self.layoutWidget)
        self.M.setObjectName("M")
        self.horizontalLayout.addWidget(self.M)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.m = QtWidgets.QLineEdit(self.layoutWidget)
        self.m.setObjectName("m")
        self.horizontalLayout_2.addWidget(self.m)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.number_of_intervals = QtWidgets.QLineEdit(self.layoutWidget)
        self.number_of_intervals.setObjectName("number_of_intervals")
        self.horizontalLayout_3.addWidget(self.number_of_intervals)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.math_hope = QtWidgets.QLineEdit(self.layoutWidget)
        self.math_hope.setObjectName("math_hope")
        self.horizontalLayout_5.addWidget(self.math_hope)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.dispersion = QtWidgets.QLineEdit(self.layoutWidget)
        self.dispersion.setObjectName("dispersion")
        self.horizontalLayout_6.addWidget(self.dispersion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.standart_devitation = QtWidgets.QLineEdit(self.layoutWidget)
        self.standart_devitation.setObjectName("standart_devitation")
        self.horizontalLayout_7.addWidget(self.standart_devitation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(390, 10, 491, 621))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.table_freq_and_intervals = QtWidgets.QTableWidget(self.layoutWidget1)
        self.table_freq_and_intervals.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_freq_and_intervals.setObjectName("table_freq_and_intervals")
        self.table_freq_and_intervals.setColumnCount(3)
        self.table_freq_and_intervals.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_freq_and_intervals.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_freq_and_intervals.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_freq_and_intervals.setHorizontalHeaderItem(2, item)
        self.table_freq_and_intervals.horizontalHeader().setVisible(True)
        self.table_freq_and_intervals.horizontalHeader().setCascadingSectionResizes(True)
        self.table_freq_and_intervals.horizontalHeader().setHighlightSections(False)
        self.table_freq_and_intervals.horizontalHeader().setMinimumSectionSize(50)
        self.table_freq_and_intervals.horizontalHeader().setSortIndicatorShown(False)
        self.table_freq_and_intervals.horizontalHeader().setStretchLastSection(False)
        self.table_freq_and_intervals.verticalHeader().setVisible(True)
        self.table_freq_and_intervals.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_3.addWidget(self.table_freq_and_intervals)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(890, 10, 231, 621))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.numbers_table = QtWidgets.QTableWidget(self.layoutWidget2)
        self.numbers_table.setObjectName("numbers_table")
        self.numbers_table.setColumnCount(1)
        self.numbers_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.numbers_table.setHorizontalHeaderItem(0, item)
        self.verticalLayout_5.addWidget(self.numbers_table)
        self.ShowGist = QtWidgets.QPushButton(self.centralwidget)
        self.ShowGist.setGeometry(QtCore.QRect(200, 540, 181, 91))
        self.ShowGist.setObjectName("ShowGist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Лабораторна робота №1</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Моделювання випадкових чисел</span></p></body></html>"))
        self.Compute.setText(_translate("MainWindow", "Розрахувати"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">M =</span></p></body></html>"))
        self.M.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">159643</p></body></html>"))
        self.M.setText(_translate("MainWindow", "1234567"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">m =</span></p></body></html>"))
        self.m.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.m.setText(_translate("MainWindow", "10"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Кількість інтервалів =</span></p></body></html>"))
        self.number_of_intervals.setText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">M(X) =</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">D(X) =</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">σ =</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Таблиця інтервалів та частот</span></p></body></html>"))
        self.table_freq_and_intervals.setSortingEnabled(False)
        item = self.table_freq_and_intervals.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Інтервал"))
        item = self.table_freq_and_intervals.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Частота патораплянь"))
        item = self.table_freq_and_intervals.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Відносна частота"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Випадкові числа</span></p></body></html>"))
        item = self.numbers_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Число"))
        self.ShowGist.setText(_translate("MainWindow", "Гістограма"))
