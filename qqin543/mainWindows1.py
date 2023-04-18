import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QShortcut, QFileDialog
import pandas as pd
from SelectDataset import Ui_Dialog1
from ViewDataset import DatasetViewer
from ViewTestImages import TestViewer
from Camera import Ui_Dialog5
from PyQt5.QtGui import QKeySequence
from SaveModel import Ui_SaveModel
from PyQt5.QtCore import QTimer
from train import trainModel
from PyQt5.QtCore import QThread, pyqtSignal,QObject
import time

class TrainingThread(QThread):
    # define a signal that can be used to emit progress updates
    update_progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            # emit the progress update signal
            self.update_progress.emit(i)
            time.sleep(0.1)


class Ui_TabWidget(QObject):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(550, 450)
        TabWidget.setMinimumSize(QtCore.QSize(550, 450))
        TabWidget.setMaximumSize(QtCore.QSize(550, 450))
        TabWidget.setIconSize(QtCore.QSize(16, 16))
        TabWidget.setUsesScrollButtons(False)
        TabWidget.setDocumentMode(True)
        TabWidget.setTabsClosable(False)
        self.tab_Import = QtWidgets.QWidget()
        self.tab_Import.setObjectName("tab_Import")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_Import)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab_Import)
        self.pushButton.setObjectName("pushButton")
       
        
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_Import)
        self.label.setEnabled(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        TabWidget.addTab(self.tab_Import, "")
        self.tab_Train = QtWidgets.QWidget()
        self.tab_Train.setObjectName("tab_Train")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_Train)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 80, 521, 321))
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_A1 = QtWidgets.QWidget()
        self.page_A1.setObjectName("page_A1")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.page_A1)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(370, 0, 122, 101))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_A1)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(370, 100, 122, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_ViewDataset = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_ViewDataset.setObjectName("pushButton_ViewDataset")
        
        self.horizontalLayout_2.addWidget(self.pushButton_ViewDataset)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.page_A1)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(180, 0, 189, 293))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listWidget_2 = QtWidgets.QListWidget(self.gridLayoutWidget_8)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_10.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.page_A1)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 179, 293))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_5)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.page_A1)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 200, 121, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_Continue = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Continue.setObjectName("pushButton_Continue")
        #sadasdasdasd
        #self.pushButton_Continue.clicked.connect(self.switchToStack2)
        self.gridLayout_7.addWidget(self.pushButton_Continue, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_A1)
        self.page_A2 = QtWidgets.QWidget()
        self.page_A2.setObjectName("page_A2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_A2)
        self.textBrowser.setGeometry(QtCore.QRect(290, 20, 161, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setObjectName("textBrowser")

        # Combobox for selecting model on select model page
        self.selectModelComboBox = QtWidgets.QComboBox(self.page_A2)
        self.selectModelComboBox.setGeometry(QtCore.QRect(0, 20, 171, 26))
        self.selectModelComboBox.setObjectName("selectModelComboBox")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")

        # Created spinbox and label for batch size on the select model page
        self.batchSizeSpinBox = QtWidgets.QSpinBox(self.page_A2)
        self.batchSizeSpinBox.setGeometry(QtCore.QRect(120, 50, 91, 31))
        self.batchSizeSpinBox.setObjectName("batchSizeSpinBox")
        self.batchSizeSpinBox.setMinimum(1) # Set minimum to 1
        self.batchSizeLabel = QtWidgets.QLabel(self.page_A2)
        self.batchSizeLabel.setGeometry(QtCore.QRect(0, 60, 71, 16))
        self.batchSizeLabel.setObjectName("batchSizeLabel")

        # Created spinbox and label for epoch number on the select model page
        self.epochNumSpinBox = QtWidgets.QSpinBox(self.page_A2)
        self.epochNumSpinBox.setGeometry(QtCore.QRect(120, 80, 91, 31))
        self.epochNumSpinBox.setObjectName("epochNumSpinBox")
        self.epochNumSpinBox.setMinimum(1) # Set minimum to 1
        self.epochNumLabel = QtWidgets.QLabel(self.page_A2)
        self.epochNumLabel.setGeometry(QtCore.QRect(0, 90, 101, 16))
        self.epochNumLabel.setObjectName("epochNumLabel")

        # Created a 'back' button on the select model page
        self.backBtn = QtWidgets.QPushButton(self.page_A2)
        self.backBtn.setGeometry(QtCore.QRect(0, 290, 113, 32))
        self.backBtn.setObjectName("backBtn")
        
        # Created a 'train model' button on the select model page
        self.trainModelBtn = QtWidgets.QPushButton(self.page_A2)
        self.trainModelBtn.setGeometry(QtCore.QRect(200, 290, 113, 32))
        self.trainModelBtn.setObjectName("trainModelBtn")

        # Below block of codes are for train and validation
        # Created a horizontal slider for the train and validation on the select model page
        self.trainValidationSlider = QtWidgets.QSlider(self.page_A2)
        self.trainValidationSlider.setGeometry(QtCore.QRect(140, 200, 221, 22))
        self.trainValidationSlider.setRange(0, 100) # Set minimum value to 0 and maximum to 100
        self.trainValidationSlider.setValue(50) # Set initial value to 50
        self.trainValidationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.trainValidationSlider.setObjectName("trainValidationSlider")
        # Create a spinbox and label for 'train' on the select model page
        self.trainSpinBox = QtWidgets.QSpinBox(self.page_A2)
        self.trainSpinBox.setGeometry(QtCore.QRect(90, 200, 48, 24))
        self.trainSpinBox.setObjectName("trainSpinBox")
        self.trainSpinBox.setRange(0, 100) # Set minimum value to 0 and maximum to 100
        self.trainSpinBox.setValue(50) # Set initial value to 50
        self.trainLabel = QtWidgets.QLabel(self.page_A2)
        self.trainLabel.setGeometry(QtCore.QRect(50, 200, 41, 21))
        self.trainLabel.setObjectName("trainLabel")
        # Create a spinbox and label for 'validation' on the select model page
        self.validationSpinBox = QtWidgets.QSpinBox(self.page_A2)
        self.validationSpinBox.setGeometry(QtCore.QRect(430, 200, 48, 24))
        self.validationSpinBox.setObjectName("validationSpinBox")
        self.validationSpinBox.setRange(0, 100) # Set minimum value to 0 and maximum to 100
        self.validationSpinBox.setValue(50) # Set initial value to 50
        self.validationLabel = QtWidgets.QLabel(self.page_A2)
        self.validationLabel.setGeometry(QtCore.QRect(370, 200, 60, 21))
        self.validationLabel.setObjectName("validationLabel")

        self.stackedWidget.addWidget(self.page_A2)
        self.page_A3 = QtWidgets.QWidget()
        self.page_A3.setObjectName("page_A3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_A3)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 10, 256, 191))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_A3)
        self.textBrowser_3.setGeometry(QtCore.QRect(260, 11, 256, 191))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_A3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 210, 521, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.progressLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout.addWidget(self.progressLabel)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_A3)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 250, 521, 71))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_B1 = QtWidgets.QWidget()
        self.page_B1.setObjectName("page_B1")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_B1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(29, 10, 471, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_CancelTraining = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_CancelTraining.setStyleSheet("background-color:rgb(253, 128, 8)")
        self.pushButton_CancelTraining.setObjectName("pushButton_CancelTraining")
        self.horizontalLayout_3.addWidget(self.pushButton_CancelTraining)
        self.stackedWidget_2.addWidget(self.page_B1)
        self.page_B2 = QtWidgets.QWidget()
        self.page_B2.setObjectName("page_B2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_B2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 0, 471, 66))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_TrainNewModel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_TrainNewModel.setObjectName("pushButton_TrainNewModel")
        self.gridLayout_5.addWidget(self.pushButton_TrainNewModel, 1, 0, 1, 1)
        self.pushButton_TestModel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_TestModel.setObjectName("pushButton_TestModel")
        self.gridLayout_5.addWidget(self.pushButton_TestModel, 1, 1, 1, 1)
        self.pushButton_SaveModel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_SaveModel.setStyleSheet("background-color:rgb(33, 255, 6)")
        self.pushButton_SaveModel.setObjectName("pushButton_SaveModel")
        self.gridLayout_5.addWidget(self.pushButton_SaveModel, 0, 0, 1, 2)
        self.stackedWidget_2.addWidget(self.page_B2)
        self.stackedWidget.addWidget(self.page_A3)
        self.label_2 = QtWidgets.QLabel(self.tab_Train)
        self.label_2.setGeometry(QtCore.QRect(29, 15, 161, 61))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_Train)
        self.label_3.setGeometry(QtCore.QRect(209, 15, 181, 61))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        TabWidget.addTab(self.tab_Train, "")
        self.tab_Test = QtWidgets.QWidget()
        self.tab_Test.setObjectName("tab_Test")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_Test)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(59, 39, 421, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser_1.setPalette(palette)
        self.textBrowser_1.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.horizontalLayout_4.addWidget(self.textBrowser_1)
        self.pushButton_LoadModel = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_LoadModel.setObjectName("pushButton_LoadModel")
        self.horizontalLayout_4.addWidget(self.pushButton_LoadModel)
        self.label_9 = QtWidgets.QLabel(self.tab_Test)
        self.label_9.setGeometry(QtCore.QRect(59, 230, 421, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_Test)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(60, 320, 421, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_DatasetImages = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_DatasetImages.setObjectName("pushButton_DatasetImages")
        
        self.horizontalLayout_5.addWidget(self.pushButton_DatasetImages)
        self.pushButton_Camera = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_Camera.setObjectName("pushButton_Camera")
        self.horizontalLayout_5.addWidget(self.pushButton_Camera)
        TabWidget.addTab(self.tab_Test, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        
        # Click signal connect to open the SelectDataset Dialog
        self.pushButton.clicked.connect(self.open_dialog1)

        # Click signal connect to open the Test Images Viewer Dialog
        self.pushButton_DatasetImages.clicked.connect(self.open_dialog3)

        # Click signal connect to open the Test Images Viewer Dialog
        self.pushButton_SaveModel.clicked.connect(self.open_dialog4)

        # Click signal connect to open the Capture Images Dialog
        self.pushButton_Camera.clicked.connect(self.open_dialog5)

        # Click signal connect to turn back to Dataset Selected
        self.backBtn.clicked.connect(self.switchToStack1)

        # Click signal connect to model configuration
        self.pushButton_Continue.clicked.connect(self.switchToStack2)

        # Click signal connect to model configuration
        self.pushButton_TrainNewModel.clicked.connect(self.switchToStack2)

        # Click signal connect to model Train
        self.trainModelBtn.clicked.connect(self.switchToStack3)
        self.trainModelBtn.clicked.connect(self.start_training)
        self.trainModelBtn.clicked.connect(lambda: trainModel.train(self, self.batchSizeSpinBox.value(), self.epochNumSpinBox.value(), self.validationSpinBox.value()))

        # Click signal connect to open the ViewDataset Dialog
        self.pushButton_ViewDataset.clicked.connect(self.open_dialog2)

        # Connect the slider value change signal to the left spinBox's setValue slot
        self.trainValidationSlider.valueChanged.connect(self.trainSpinBox.setValue)
        
        # Connect the left spinBox value change signal to the update_spinbox_2_value custom slot
        self.trainSpinBox.valueChanged.connect(self.updateValidationSpinBox)
        
        # Connect the right spinBox value change signal to the update_spinbox_value custom slot
        self.validationSpinBox.valueChanged.connect(self.updateTrainSpinBox)
        
        # Create shortcuts for switching stack_2 pages
        self.shortcut_pageB1 = QShortcut(QKeySequence("Ctrl+1"), TabWidget)
        self.shortcut_pageB1.activated.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.shortcut_pageB2 = QShortcut(QKeySequence("Ctrl+2"), TabWidget)
        self.shortcut_pageB2.activated.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))

        #click signal connect to Test Tab
        self.pushButton_TestModel.clicked.connect(self.switchToTab3)
        
        #Create a Timer used for check if Dataset exit to update label
        self.check_dataset_timer = QTimer()
        self.check_dataset_timer.timeout.connect(self.updateDatasetLabel)
        self.check_dataset_timer.start(500) 

        # This timer is used to check whether the dataset is being imported or not
        self.train_timer = QTimer()
        self.train_timer.timeout.connect(lambda: self.fileExist(1))
        self.train_timer.start(1000)
  

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Sign Recognization"))
        self.pushButton.setText(_translate("TabWidget", "Import Dataset"))
        self.label.setText(_translate("TabWidget", "No Dataset Selected"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_Import), _translate("TabWidget", "Import"))
        self.pushButton_ViewDataset.setText(_translate("TabWidget", "View Dataset"))
        self.pushButton_Continue.setText(_translate("TabWidget", "Continue"))
        self.textBrowser.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">DNN Name:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">Batch Size:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">Epoch Number:</span></p></body></html>"))
        
        # ComboBox for model selection on select model page
        self.selectModelComboBox.setItemText(0, _translate("TabWidget", "Selecet a Model"))
        self.selectModelComboBox.setItemText(1, _translate("TabWidget", "Logistic Regression"))
        self.selectModelComboBox.setItemText(2, _translate("TabWidget", "CNN"))
        self.selectModelComboBox.setItemText(3, _translate("TabWidget", "DNN"))


        self.batchSizeLabel.setText(_translate("TabWidget", "Batch Size:"))
        self.epochNumLabel.setText(_translate("TabWidget", "Epoch Number:"))
        self.backBtn.setText(_translate("TabWidget", "Back"))
        self.trainModelBtn.setText(_translate("TabWidget", "Train Model"))
        self.trainValidationSlider.setToolTip(_translate("TabWidget", "<html><head/><body><p><span style=\" color:#fd8008;\">Validation set and Train set must &gt; 10%</span></p></body></html>"))
        self.trainLabel.setText(_translate("TabWidget", "Train:"))
        self.validationLabel.setText(_translate("TabWidget", "Validation:"))
        self.textBrowser_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">DNN Name:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Batch Size:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Epoch Number:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Train Set Size:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Validation Set Size:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Test Set Size:</span></p></body></html>"))
        self.progressLabel.setText(_translate("TabWidget", "0%"))
        self.pushButton_CancelTraining.setText(_translate("TabWidget", "Cancel Training"))
        self.pushButton_TrainNewModel.setText(_translate("TabWidget", "Train New Model"))
        self.pushButton_TestModel.setText(_translate("TabWidget", "Test Model"))
        self.pushButton_SaveModel.setText(_translate("TabWidget", "Save Model as..."))
        self.label_2.setText(_translate("TabWidget", "Dataset Name:"))
        self.label_3.setText(_translate("TabWidget", "Number of Images:"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_Train), _translate("TabWidget", "Train"))
        self.textBrowser_1.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">DNN Name:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">Batch Size:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#fd8008;\">Epoch Number:</span></p></body></html>"))

        # When the 'load model from file' is clicked, open file dialog and load the saved model
        self.pushButton_LoadModel.setText(_translate("TabWidget", "Load Model from file "))
        self.pushButton_LoadModel.clicked.connect(self.select_file_dialog)

        self.label_9.setText(_translate("TabWidget", "Chose Test using:"))
        self.pushButton_DatasetImages.setText(_translate("TabWidget", "Dataset Images"))
        self.pushButton_Camera.setText(_translate("TabWidget", "Camera"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_Test), _translate("TabWidget", "Test"))

        TabWidget.tabBarClicked.connect(lambda: self.fileExist(1))
 
    def open_dialog1(self):
    # Create a QDialog instance
        dialog = QtWidgets.QDialog()
    # Create a Ui_Dialog instance
        dialog1 = Ui_Dialog1()
    # Configure the QDialog instance using the setupUi method
        dialog1.setupUi(dialog)
        dialog.exec_()

    #open Dataster Viewer Dialog
    def open_dialog2(self):
    # Create a QDialog instance
        dialog = QtWidgets.QDialog()
    # Create a Ui_Dialog instance
        dialog2 = DatasetViewer()
    # Configure the QDialog instance using the setupUi method
        dialog2.setupUi(dialog)
        dialog.exec_()

    data_signal1 = pyqtSignal(int)
    data_signal2 = pyqtSignal(str)
   
    def open_dialog3(self):
    # Create a QDialog instance
     dialog = QtWidgets.QDialog()
    # Create a Ui_Dialog instance
     dialog3 = TestViewer()
    # Configure the QDialog instance using the setupUi method
     dialog3.setupUi(dialog)
     self.data_signal1.connect(dialog3.get_Combobox_Value)
     self.data_signal1.emit(self.get_combobox_value()) 
     self.data_signal2.connect(dialog3.get_File_Path)
     self.data_signal2.emit(self.get_model_file_path())
     dialog.exec_()

    def open_dialog4(self):
     # Create a QDialog instance
      dialog = QtWidgets.QDialog()
     # Create a Ui_Dialog instance
      dialog4 = Ui_SaveModel()
     # Configure the QDialog instance using the setupUi method
      dialog4.setupUi(dialog)
      dialog.exec_()

    def open_dialog5(self):
     # Create a QDialog instance
      dialog = QtWidgets.QDialog()
     # Create a Ui_Dialog instance
      dialog5 = Ui_Dialog5()
     # Configure the QDialog instance using the setupUi method
      dialog5.setupUi(dialog)
      dialog.exec_()

    
    #After Selected Dataset change to configration model
    def switchToStack2(self):
        self.stackedWidget.setCurrentIndex(1)
    
    
    # Allow user turn back to Select Dataset
    def switchToStack1(self):
        self.stackedWidget.setCurrentIndex(0)
 
    # Switch into the Train Model Phase
    def switchToStack3(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)

    # Switch to the test phase
    def switchToTab3(self):
       TabWidget.setCurrentIndex(2)

   
    # Custom slot to update the validation (right) spinBox's value based on the train (left) spinBox's value
    def updateValidationSpinBox(self):
        # Calculate the value of the validation (right) spinBox to make the sum equal to 100
        value = 100 - self.trainSpinBox.value()
        # Set the calculated value to the right spinBox
        self.validationSpinBox.setValue(value)
        # Update the slider value to match the left spinBox's value
        self.trainValidationSlider.setValue(self.trainSpinBox.value())

    # Custom slot to update the train (left) spinBox's value based on the validation (right) spinBox's value
    def updateTrainSpinBox(self):
        # Calculate the value of the train (left) spinBox to make the sum equal to 100
        value = 100 - self.validationSpinBox.value()
        # Set the calculated value to the left spinBox
        self.trainSpinBox.setValue(value)
        # Update the slider value to match the left spinBox's value
        self.trainValidationSlider.setValue(value)

    def displayNumbers(self):
        # Specify the dataset path
        dataset_path = os.getcwd()
        # Join the dataset file path with the dataset path
        dataset_file = f"{dataset_path}/sign-language-mnist/sign_mnist_test.csv"
        data = pd.read_csv(dataset_file)
        letter_counts = data['label'].value_counts().sort_index()

        # Separate the letters into two groups
        group1 = [x for x in range(0, 13) if x != 9]  # A-I,K,L,M
        group2 = range(13, 25)  # N-Y

        # Clear the ListWidgets before adding new items
        self.listWidget.clear()
        self.listWidget_2.clear()

        # Add the counts for the first group (A-I, K, L, M) to the first ListWidget
        for label in group1:
            # Determine the corresponding letter for the label
            if label <= 8:
                letter = chr(ord('A') + label)
            elif 10 <= label <= 24:
                letter = chr(ord('A') + label)

            # Retrieve the count for the current label
            count = letter_counts.get(label, 0)
            # Create a QListWidgetItem with the formatted label count
            item = QtWidgets.QListWidgetItem(f"{letter}: {count}")
            # Add the item to the list widget
            self.listWidget.addItem(item)

        # Add the counts for the second group (N-Y) to the second ListWidget
        for label in group2:
            # Determine the corresponding letter for the label
            if label <= 8:
                letter = chr(ord('A') + label)
            elif 10 <= label <= 24:
                letter = chr(ord('A') + label)
                
            # Retrieve the count for the current label
            count = letter_counts.get(label, 0)
            # Create a QListWidgetItem with the formatted label count
            item = QtWidgets.QListWidgetItem(f"{letter}: {count}")
            # Add the item to the list widget
            self.listWidget_2.addItem(item)

    def updateDatasetLabel(self):
    # Specify the dataset path
       dataset_path = os.getcwd()
    # Join the dataset file path with the dataset path
       dataset_file = f"{dataset_path}/sign-language-mnist/sign_mnist_test.csv"

    # Check if the dataset file exists
       if os.path.exists(dataset_file):
           # If the dataset file exists, set the label text to "MNIST Dataset Selected"
           self.label.setText("MNIST Dataset Selected")
           self.label_2.setText("Dataset Name: MNIST")
           self.label_3.setText("Number of Images: 34627")
           self.displayNumbers()
       else:
           self.label.setText("No Dataset Selected")
           self.label_2.setText("Dataset Name:")
           self.label_3.setText("Number of Images:")


    def select_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select a file", "", "All Files (*);;CSV Files (*.csv)", options=options)
        

    def get_model_file_path(self):
        file_path = self.file_path

        if file_path:
            return file_path
        else:
            return None
        
    def get_combobox_value(self):
        return self.selectModelComboBox.currentIndex()

    # This function is used to check whether the dataset is being imported or not
    # If no then disable the tab and set tooltip, if yes then enable the tab and disable tooltip
    def fileExist(self, index):
        path = os.getcwd()
        file_path = f"{path}/sign-language-mnist"
        if index == 1:
            if os.path.exists(file_path):
                TabWidget.setTabEnabled(1, True)
                TabWidget.setTabToolTip(1, "")
            else:
                TabWidget.setTabEnabled(1, False)
                TabWidget.setTabToolTip(1, "Please import a dataset before training")


    def start_training(self):
        # create the training thread
        self.thread = TrainingThread()
        # connect the progress update signal to the update_progress method
        self.thread.update_progress.connect(self.update_progress)
        # start the thread
        self.thread.start()

    def update_progress(self, value):
        # update the progress bar value
        self.progressBar.setValue(value)
        self.progressLabel.setText(str(value) + "%")
        if value == 100:
            self.stackedWidget_2.setCurrentIndex(1)

        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()

    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
  

