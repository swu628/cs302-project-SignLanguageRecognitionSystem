from PyQt5 import QtCore, QtGui, QtWidgets
import os


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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 2)
        
        # Create a layout for the Import button
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
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
        
        self.pushButton.clicked.connect(self.Download_dataset)
        # Connect the Cancel Button to Delete Dataset File
        self.pushButton_2.clicked.connect(self.Delete_file)
        # Connect the Cancel Button to Delete Dataset File and Update Progressbar's valure
        self.pushButton_2.clicked.connect(self.Update_Progress)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Dataset"))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Dataset"))
        self.comboBox.setItemText(1, _translate("Dialog", "MNIST"))
        self.label.setText(_translate("Dialog", " Please Selected a Dataset"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Download"))
        self.label_3.setText(_translate("Dialog", "0%"))


    def Download_dataset(self):
        kaggle_dataset = "datamunge/sign-language-mnist"
        os.system(f"kaggle datasets download -d datamunge/sign-language-mnist")
        # When the download is complete, set the progress bar value to 100%
        self.progressBar.setValue(100)
        self.label_3.setText("100%")
    
    # Update the label text when "MNIST" is selected
    def on_dataset_selected(self, dataset_name):
        # Update the label text when "MNIST" is selected
        if dataset_name == "MNIST":
            self.label.setText("You have selected MNIST dataset, please click Download")
        else:
            self.label.setText("Please select a dataset")

  

    
    # Delete the Dataset file
    def Delete_file(file_path, file_name):
    
      file_to_delete = os.path.join("/Users/qinqi/project-1-python-team_10/qqin543", "sign-language-mnist.zip")
      
      try:
        # Remove the file
          os.remove(file_to_delete)
          print(f"Successfully deleted file {file_name}")
      except FileNotFoundError:
          print(f"File {file_name} does not exist")
    def Update_Progress(self):

     self.progressBar.setValue(0)
     self.label_3.setText("0%")

      



        
