# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/qinqi/QT Designer/Test Images Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 605)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 26, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 19, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setStyleSheet("background-color:rgb(33, 255, 6)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 26, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 5, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 20, 0, 5, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 17, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 8, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 9, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 12, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 15, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 4, 1, 22, 1)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test Images Viewer"))
        self.pushButton_4.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Filter"))
        self.pushButton_6.setText(_translate("Dialog", "Predict"))
        self.radioButton_2.setText(_translate("Dialog", "Test Set"))
        self.checkBox_3.setText(_translate("Dialog", "Custom"))
        self.label_2.setText(_translate("Dialog", "No. image"))
        self.pushButton_2.setText(_translate("Dialog", "Clear Tags"))
        self.pushButton.setText(_translate("Dialog", "Add Tag"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
        self.pushButton_5.setText(_translate("Dialog", "Deselect All"))
        self.listWidget.setSortingEnabled(True)
        self.radioButton.setText(_translate("Dialog", "Train Set"))
        self.label.setText(_translate("Dialog", "Filter"))