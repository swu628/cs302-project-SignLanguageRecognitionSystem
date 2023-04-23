# Import relevant libraries
import zipfile
from PyQt5 import QtCore, QtWidgets
import os
import shutil


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        # Set up the main dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 395)
        Dialog.setMinimumSize(QtCore.QSize(430, 300))
        Dialog.setMaximumSize(QtCore.QSize(10000, 10000))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        # Create a layout for the combo box and label
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        # Combo box for dataset selection
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        
        # Label to ask for dataset selection
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        # Connect the "activated" signal of the combo box to a slot function
        self.comboBox.activated[str].connect(self.on_dataset_selected)
        
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 4)
        
        # Create a layout for the Cancel button
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteBtn.setObjectName("deleteBtn")
        self.deleteBtn.setEnabled(False)
        self.verticalLayout_2.addWidget(self.deleteBtn)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 2)
        
        # Create a layout for the Import button
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.downloadBtn = QtWidgets.QPushButton(Dialog)
        self.downloadBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.downloadBtn.setObjectName("downloadBtn")
        self.downloadBtn.setEnabled(True)
        self.verticalLayout.addWidget(self.downloadBtn)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        
        # Create a layout for the progress bar and labels
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # Progress bar used for indicate Import progress
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        
        # Labels for progress percentage
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.downloadBtn.clicked.connect(self.Download_dataset)
        # Connect the Cancel Button to Delete Dataset File
        self.deleteBtn.clicked.connect(self.Delete_file)
        # Connect the Cancel Button to Delete Dataset File and Update Progressbar's valure
        self.deleteBtn.clicked.connect(self.Update_Progress)

        # Check whether the dataset is imported, if yes: enable delete button, if no: enable download button
        path = os.getcwd()
        if os.path.exists(f"{path}/sign-language-mnist"):
            self.downloadBtn.setEnabled(False)
            self.deleteBtn.setEnabled(True)
        else:
            self.downloadBtn.setEnabled(True)
            self.deleteBtn.setEnabled(False)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Dataset"))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Dataset"))
        self.comboBox.setItemText(1, _translate("Dialog", "MNIST"))
        self.label.setText(_translate("Dialog", " Please Selected a Dataset"))
        self.deleteBtn.setText(_translate("Dialog", "Delete"))
        self.downloadBtn.setText(_translate("Dialog", "Download"))
        self.label_3.setText(_translate("Dialog", "0%"))

    # This function will download the MNIST sign language dataset from kaggle using API
    def Download_dataset(self):
        #Got the current be Selected Dataset Name
        Current_dataset_name = self.comboBox.currentText()
        if Current_dataset_name == "MNIST":
            kaggle_dataset = "datamunge/sign-language-mnist"
            os.system(f"kaggle datasets download -d datamunge/sign-language-mnist")
            # When the download is complete, set the progress bar value to 100%
            self.progressBar.setValue(100)
            self.label_3.setText("100%")
            self.downloadBtn.setEnabled(False)
            self.deleteBtn.setEnabled(True)
            path = os.getcwd()
            # specify the path to the zip file
            zip_file_path = f"{path}/sign-language-mnist.zip"
            # extract the contents of the zip file to a directory if the directory does not exist
            if not os.path.exists(f"{path}/sign-language-mnist"):
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(f"{path}/sign-language-mnist")
        else: 
            # Display error message when no dataset is selected but the download button is pressed
            QtWidgets.QMessageBox.warning(None, "No Dataset Selected", "Please select a dataset.")
    
    # This fucntion will update the label text when "MNIST" is selected
    def on_dataset_selected(self, dataset_name):
        # Update the label text when "MNIST" is selected
        if dataset_name == "MNIST":
            self.label.setText("You have selected MNIST dataset, please click Download")
        else:
            self.label.setText("Please select a dataset")
    
    # This function will be used to delete the downloaded dataset file
    def Delete_file(file_path):
        try:
            # Remove the file
            path = os.getcwd()
            os.remove(f"{path}/sign-language-mnist.zip")
            shutil.rmtree(f"{path}/sign-language-mnist")
            print(f"Successfully deleted file: sign-language-mnist")
        except FileNotFoundError:
            print(f"File: sign-language-mnist does not exist")
    
    # This function will be used to update the progress of the download dataset
    def Update_Progress(self):
     self.progressBar.setValue(0)
     self.label_3.setText("0%")
     self.downloadBtn.setEnabled(True)
     self.deleteBtn.setEnabled(False)