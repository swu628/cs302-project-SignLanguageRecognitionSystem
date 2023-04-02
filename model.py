from multiprocessing.pool import TERMINATE
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton, QSpinBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from leNet5 import LeNet5

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Create radio buttons
        self.lenetRadioBtn = QRadioButton(self)
        self.lenetRadioBtn.setText('LeNet-5')
        self.inceptionRadioBtn = QRadioButton(self)
        self.inceptionRadioBtn.setText('InceptionV3')
        self.resnetRadioBtn = QRadioButton(self)
        self.resnetRadioBtn.setText('ResNet-50')

        # Create spin box for user to adjust the hyper parameters
        # Batch size
        self.batchSizeBox = QSpinBox()
        self.batchSizeBox.setRange(1, 30) # set minimum to 0 and set maximum to 30
        self.batchSizeBox.setSingleStep(1)        
        self.batchSizeLabel = QLabel('Batch Size: ')
        # Epoch number
        self.epochNumberBox = QSpinBox()
        self.epochNumberBox.setRange(1, 30) # set minimum to 0 and set maximum to 30
        self.epochNumberBox.setSingleStep(1)        
        self.epochNumberLabel = QLabel('Epoch Number: ')

        # Create cancel and save buttons
        cancelBtn = QPushButton('Cancel', self)
        trainBtn = QPushButton('Train', self)

        # Set the layout of radio buttons and buttons
        vbox = QVBoxLayout()
        chooseModel = QHBoxLayout()
        chooseModel.addWidget(self.lenetRadioBtn)
        chooseModel.addWidget(self.inceptionRadioBtn)
        chooseModel.addWidget(self.resnetRadioBtn)

        batchSizeLayout = QHBoxLayout()
        batchSizeLayout.addWidget(self.batchSizeLabel)
        batchSizeLayout.addWidget(self.batchSizeBox)

        epochNumberLayout = QHBoxLayout()
        epochNumberLayout.addWidget(self.epochNumberLabel)
        epochNumberLayout.addWidget(self.epochNumberBox)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(cancelBtn)
        buttonsLayout.addWidget(trainBtn)
        vbox.addLayout(chooseModel)
        vbox.addLayout(batchSizeLayout)
        vbox.addLayout(epochNumberLayout)
        vbox.addLayout(buttonsLayout)
        self.setLayout(vbox)

        # Call a function when button is clicked
        trainBtn.clicked.connect(self.train)

        # Set and show the window
        self.setWindowTitle('Model')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    # This is the function to call when the train button is clicked
    def train(self):

        # If the user choose lenet5 model, it will call the leNet5 class
        if self.lenetRadioBtn.isChecked():
            
            #Loading the dataset and preprocessing
            train_dataset = torchvision.datasets.MNIST(root = './data', train = True, 
            transform = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor(), 
            transforms.Normalize(mean = (0.1307,), std = (0.3081,))]), download = True)

            test_dataset = torchvision.datasets.MNIST(root = './data', train = False,
            transform = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor(),
            transforms.Normalize(mean = (0.1325,), std = (0.3105,))]), download=True)

            train_loader = torch.utils.data.DataLoader(dataset = train_dataset, 
            batch_size = self.batchSizeBox.value(), shuffle = True)

            test_loader = torch.utils.data.DataLoader(dataset = test_dataset, 
            batch_size = self.batchSizeBox.value(), shuffle = True)

            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            self.model = LeNet5().to(self.device)
            
            # Setting the loss function
            self.cost = nn.CrossEntropyLoss()
            
            #Setting the optimizer with the model parameters and learning rate
            self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
            
            #this is defined to print how many steps are remaining when training
            total_step = len(train_loader)

            for epoch in range(self.epochNumberBox.value()):
                for i, (images, labels) in enumerate(train_loader):  
                    images = images.to(self.device)
                    labels = labels.to(self.device)
        
                    #Forward pass
                    outputs = self.model(images)
                    loss = self.cost(outputs, labels)
        	
                    # Backward and optimize
                    self.optimizer.zero_grad()
                    loss.backward()
                    self.optimizer.step()
        		
                    if (i+1) % 400 == 0: 
                        print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, self.epochNumberBox.value(), i+1, total_step, loss.item()))
        
        elif self.inceptionRadioBtn.isChecked():
            print ("inception")
        else:
            print("resnet")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())