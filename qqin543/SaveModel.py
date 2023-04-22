from pyexpat import model
from PyQt5 import QtCore, QtWidgets
from train import trainModel

class Ui_SaveModel(object):
    def setupUi(self, SaveModel):
        # Set up the main dialog
        SaveModel.setObjectName("SaveModel")
        SaveModel.setEnabled(True)
        SaveModel.resize(250, 200)
        SaveModel.setMinimumSize(QtCore.QSize(250, 200))
        SaveModel.setMaximumSize(QtCore.QSize(250, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveModel)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Label asking user to enter a name
        self.label = QtWidgets.QLabel(SaveModel)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        # Line edit for user to enter a name
        self.lineEdit = QtWidgets.QLineEdit(SaveModel)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        
        # Save button
        self.pushButton_1 = QtWidgets.QPushButton(SaveModel)
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_1.setCheckable(False)
        self.pushButton_1.setChecked(False)
        self.pushButton_1.setAutoDefault(True)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        
        # Cancel button
        self.pushButton_2 = QtWidgets.QPushButton(SaveModel)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        
        self.retranslateUi(SaveModel)
        QtCore.QMetaObject.connectSlotsByName(SaveModel)

        # Save model and close the window when 'save' button is clicked
        self.pushButton_1.clicked.connect(lambda: trainModel.saveModel(self, self.lineEdit.text()))
        self.pushButton_1.clicked.connect(SaveModel.reject)

        # Close the window when the 'cancel' button is clicked
        self.pushButton_2.clicked.connect(SaveModel.reject)

    def retranslateUi(self, SaveModel):
        _translate = QtCore.QCoreApplication.translate
        SaveModel.setWindowTitle(_translate("SaveModel", "Save Model"))
        self.label.setText(_translate("SaveModel", "Please Enter a Name (Letters Only)"))
        self.pushButton_1.setText(_translate("SaveModel", "Save"))
        self.pushButton_2.setText(_translate("SaveModel", "Cancel"))
    