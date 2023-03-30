import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QRadioButton, QSpinBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Create radio buttons
        rbtn1 = QRadioButton('LeNet-5', self)
        rbtn1.move(50, 50)
        # rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('InceptionV3')
        # rbtn2.setChecked(True)

        rbtn3 = QRadioButton(self)
        rbtn3.move(50, 70)
        rbtn3.setText('ResNet-50')
        # rbtn2.setChecked(True)

        # Create spin box for user to adjust the hyper parameters
        # Batch size
        self.batchSizeBox = QSpinBox()
        self.batchSizeBox.setRange(0, 30) # set minimum to 0 and set maximum to 30
        self.batchSizeBox.setSingleStep(1)        
        # This line will be used later => self.batchSizeBox.valueChanged.connect(self.value_changed)
        self.batchSizeLabel = QLabel('Batch Size: ')
        # Epoch number
        self.EpochNumberBox = QSpinBox()
        self.EpochNumberBox.setRange(0, 30) # set minimum to 0 and set maximum to 30
        self.EpochNumberBox.setSingleStep(1)        
        # This line will be used later => self.EpochNumberBox.valueChanged.connect(self.value_changed)
        self.EpochNumberLabel = QLabel('Epoch Number: ')

        # Create cancel and save buttons
        btn1 = QPushButton('Cancel', self)
        btn2 = QPushButton('Save', self)

        # Set the layout of radio buttons and buttons
        vbox = QVBoxLayout()
        chooseModel = QHBoxLayout()
        chooseModel.addWidget(rbtn1)
        chooseModel.addWidget(rbtn2)
        chooseModel.addWidget(rbtn3)

        batchSizeLayout = QHBoxLayout()
        batchSizeLayout.addWidget(self.batchSizeLabel)
        batchSizeLayout.addWidget(self.batchSizeBox)

        EpochNumberLayout = QHBoxLayout()
        EpochNumberLayout.addWidget(self.EpochNumberLabel)
        EpochNumberLayout.addWidget(self.EpochNumberBox)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(btn1)
        buttonsLayout.addWidget(btn2)
        vbox.addLayout(chooseModel)
        vbox.addLayout(batchSizeLayout)
        vbox.addLayout(EpochNumberLayout)
        vbox.addLayout(buttonsLayout)
        self.setLayout(vbox)

        # Call a function when button is clicked
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        # Set and show the window
        self.setWindowTitle('Model')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    # This is the function to call when the spin box is adjusted
    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))

    # This is the function to call when the button is clicked
    def resizeBig(self):
        self.resize(400, 500)

    # This is the function to call when the button is clicked
    def resizeSmall(self):
        self.resize(200, 250)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())