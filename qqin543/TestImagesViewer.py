# Import relevant libraries
from PyQt5 import QtCore, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        # Set up the main dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 605)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        # Create various buttons
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
        
        # Create radio buttons for select Test Set
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 5, 0, 1, 1)
       
        # Create check boxes for filter dataset
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 10, 0, 1, 1)
        
        # Create Add Tag and Clear Tag buttons
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 17, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 1)
        
        # Create line edit
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 12, 0, 1, 1)
        
        # Create another button
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        
        # Create text browser for Tag Added Dispaly
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 15, 0, 1, 1)

        # Create table widget for show Test Display
        self.tablewidget = QtWidgets.QTableWidget(Dialog)
        self.tablewidget.setTabletTracking(True)
        self.tablewidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tablewidget.setTabKeyNavigation(True)
        self.tablewidget.setDragEnabled(True)
        self.tablewidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tablewidget.setObjectName("tablewidget")
        self.gridLayout.addWidget(self.tablewidget, 4, 1, 22, 1)

        # Space to give some breathing room
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 1)

        # Create label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        # Add Space to give some breathing room
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        
        # Connect Cancel Button click signal to QDialog reject slot
        self.pushButton_4.clicked.connect(Dialog.reject)
        
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
        self.pushButton_2.setText(_translate("Dialog", "Clear Tags"))
        self.pushButton.setText(_translate("Dialog", "Add Tag"))
        self.pushButton_5.setText(_translate("Dialog", "Deselect All"))
        self.tablewidget.setSortingEnabled(True)
        self.label.setText(_translate("Dialog", "Filter"))