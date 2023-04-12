import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import cv2
from leNet5 import LeNet5
import torch.nn.functional as F
from cnn import CNNModel
from loadDataset import loadData

class trainModel:

    # This is the function to call when the train button is clicked
    def train(self, batchSize, epochNum, validationValue):
        
        # load dataset
        train_dataloder, validation_dataloader, test_dataloader = loadData.load(self, batchSize, validationValue)

        # If the user choose lenet5 model, it will call the leNet5 class
        if self.selectModelComboBox.currentIndex() == 1:
            print('letNet5')
            '''
            # Below block of codes load the dataset
            # get the path
            path = os.getcwd()
            # specify the path to the zip file
            zip_file_path = f"{path}/sign-language-mnist.zip"
            # extract the contents of the zip file to a directory if the directory does not exist
            if not os.path.exists(f"{path}/sign-language-mnist"):
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(f"{path}/sign-language-mnist")
            # Using custom GestureDataset class to load train and test data respectively.
            train_dataset = GestureDataset(f"{path}/sign-language-mnist/sign_mnist_train.csv")
            test_dataset = GestureDataset(f"{path}/sign-language-mnist/sign_mnist_test.csv")

            # Using the in-built DataLoader to create batches of images and labels for training validation respectively. 
            train_loader = DataLoader(dataset = train_dataset, batch_size = batchsize, shuffle=True)
            test_loader = DataLoader(dataset = test_dataset, batch_size = batchsize, shuffle=True)

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
        '''

        elif self.selectModelComboBox.currentIndex() == 2:

            # import cnn model
            model = CNNModel(in_channels=1, num_classes=26)

            # train the model
            @torch.no_grad()
            def evaluate(model, val_loader):
                model.eval()
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

            def fit(epochs, learning_rate, model, train_loader, val_loader, opt_func=torch.optim.SGD):
                history = []
                optimizer = opt_func(model.parameters(), learning_rate)
                for epoch in range(epochs):
                    # Training Phase 
                    model.train()
                    train_losses = []
                    for batch in train_loader:
                        loss = model.training_step(batch)
                        train_losses.append(loss)
                        loss.backward()
                        optimizer.step()
                        optimizer.zero_grad()
                    # Validation phase
                    result = evaluate(model, val_loader)
                    result['train_loss'] = torch.stack(train_losses).mean().item()
                    model.epoch_end(epoch, result)
                    history.append(result)
                return history

            history = fit(epochNum, 0.001, model, train_dataloder, validation_dataloader)
       
        elif self.selectModelComboBox.currentIndex() == 3:
            print("VGG16")
        else:
            print("Please select a model")



class GestureDataset(Dataset):

    # This function reads csv, splits Labels and Images, and converts given 1-D vectors to 2-D images.
    def __init__(self,csv,train=True):
        self.csv=pd.read_csv(csv)
        self.img_size=224
        self.train=train
        text="pixel"
        self.images=torch.zeros((self.csv.shape[0],1))
        for i in range(1,785):
            temp_text=text+str(i)
            temp=self.csv[temp_text]
            temp=torch.FloatTensor(temp).unsqueeze(1)
            self.images=torch.cat((self.images,temp),1)
        self.labels=self.csv['label']
        self.images=self.images[:,1:]
        self.images=self.images.view(-1,28,28)

    # This function...
    # Reads each image and resizes them to the size (224,224).
    # The image is then converted to Tensor of type Float.
    # Finally, the tensor values are normalized to the range (0,1). 
    def __getitem__(self,index):
        img=self.images[index]
        img=img.numpy()
        img=cv2.resize(img,(self.img_size,self.img_size))
        tensor_image=torch.FloatTensor(img)
        tensor_image=tensor_image.unsqueeze(0)
        tensor_image/=255.
        if self.train:
            return tensor_image,self.labels[index]
        else:
            return tensor_image

    # This function returns the number of images in the dataset.
    def __len__(self):
        return self.images.shape[0]

