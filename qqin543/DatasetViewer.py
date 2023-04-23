from PyQt5 import QtCore, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 555)

        # Create a grid layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Create a label and add it to the grid layout
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        # Create a text browser and add it to the grid layout
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 15, 0, 1, 1)

        # Create a push button and add it to the grid layout
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 1)

        # Create a radio button and add it to the grid layout
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 5, 0, 1, 1)

        # Create a check box and add it to the grid layout
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 10, 0, 1, 1)

        # Create a line edit and add it to the grid layout
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 12, 0, 1, 1)

        # Create a radio button and add it to the grid layout
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 6, 0, 1, 1)

        # Add spacer items to the grid layout
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)

        # Create push buttons and add them to the grid layout
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 16, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 17, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 20, 0, 1, 1)
        self.tableWidegt = QtWidgets.QTableWidget(Dialog)
        self.tableWidegt.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidegt.setObjectName("tableWidegt")
        self.gridLayout.addWidget(self.tableWidegt, 4, 1, 16, 1)

        # Connect Cancel Button click signal to QDialog reject slot
        self.pushButton_4.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dataset Viewer"))
        self.label.setText(_translate("Dialog", "Filter"))
        self.pushButton.setText(_translate("Dialog", "Add Tag"))
        self.radioButton.setText(_translate("Dialog", "Train Set"))
        self.checkBox_3.setText(_translate("Dialog", "Custom"))
        self.radioButton_2.setText(_translate("Dialog", "Test Set"))
        self.pushButton_2.setText(_translate("Dialog", "Clear Tags"))
        self.pushButton_3.setText(_translate("Dialog", "Filter"))
        self.pushButton_4.setText(_translate("Dialog", "Cancel"))