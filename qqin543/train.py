import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from leNet5 import LeNet5

class trainModel:
    # This is the function to call when the train button is clicked
    def train(self, batchsize, epochNum):

        # If the user choose lenet5 model, it will call the leNet5 class
        if self.selectModelComboBox.currentIndex() == 1:

            #Loading the dataset and preprocessing
            train_dataset = torchvision.datasets.MNIST(root = './data', train = True, 
            transform = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor(), 
            transforms.Normalize(mean = (0.1307,), std = (0.3081,))]), download = True)

            test_dataset = torchvision.datasets.MNIST(root = './data', train = False,
            transform = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor(),
            transforms.Normalize(mean = (0.1325,), std = (0.3105,))]), download=True)

            train_loader = torch.utils.data.DataLoader(dataset = train_dataset, 
            batch_size = batchsize, shuffle = True)

            test_loader = torch.utils.data.DataLoader(dataset = test_dataset, 
            batch_size = batchsize, shuffle = True)

            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            self.model = LeNet5().to(self.device)
            
            # Setting the loss function
            self.cost = nn.CrossEntropyLoss()
            
            #Setting the optimizer with the model parameters and learning rate
            self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
            
            #this is defined to print how many steps are remaining when training
            total_step = len(train_loader)

            for epoch in range(epochNum):
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
                        print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, epochNum, i+1, total_step, loss.item()))
        
        elif self.selectModelComboBox.currentIndex() == 2:
            print("InceptionV1")
        elif self.selectModelComboBox.currentIndex() == 3:
            print("VGG16")
        else:
            print("Please select a model")