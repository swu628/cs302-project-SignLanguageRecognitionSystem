from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        # Set up the main dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 555)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        # Cancel button
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 26, 0, 1, 1)
        
       # Label to show image number
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 20, 0, 5, 1)
        
        # Filter label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        
        # Text browser for Tag be added display
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 16, 0, 1, 1)
        
        # Add tag button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 15, 0, 1, 1)
        
        # Radio button for Train set
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 5, 0, 1, 1)
       
        # Radio button for Test set
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 6, 0, 1, 1)
        
        # Filter button
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 19, 0, 1, 1)
        
        # Check box 
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 9, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 10, 0, 1, 1)
        
        # Custom check box
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 11, 0, 1, 1)
        
        # Line edit for user input
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 13, 0, 1, 1)
        
        # Clear tags button
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 18, 0, 1, 1)
        
        # Space to give some breathing room
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        
        # Another space for more breathing room
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        
        # Table widget for Dataset Display
        self.tablewidget = QtWidgets.QTableWidget(Dialog)
        self.tablewidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tablewidget.setObjectName("tablewidget")
        self.gridLayout.addWidget(self.tablewidget, 5, 1, 21, 1)
        
    
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # Connect Cancel Button click signal to QDialog reject slot
        self.pushButton_4.clicked.connect(Dialog.reject)
      

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dataset Viewer"))
        self.pushButton_4.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "No. image"))
        self.label.setText(_translate("Dialog", "Filter"))
        self.pushButton.setText(_translate("Dialog", "Add Tag"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
        self.radioButton.setText(_translate("Dialog", "Train Set"))
        self.pushButton_3.setText(_translate("Dialog", "Filter"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_3.setText(_translate("Dialog", "Custom"))
        self.radioButton_2.setText(_translate("Dialog", "Test Set"))
        self.pushButton_2.setText(_translate("Dialog", "Clear Tags"))

