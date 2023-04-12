import torch
import torch.nn as nn
from torch.utils.data import Dataset, TensorDataset, random_split, DataLoader
import torchvision
import torchvision.transforms as transforms
import pandas as pd
import cv2
import os
import zipfile
from leNet5 import LeNet5
import torch.nn.functional as F
import matplotlib.pyplot as plt

class trainModel:

    # This is the function to call when the train button is clicked
    def train(self, batchsize, epochNum):

        # If the user choose lenet5 model, it will call the leNet5 class
        if self.selectModelComboBox.currentIndex() == 1:
            
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
        
        elif self.selectModelComboBox.currentIndex() == 2:
            
            # Below block of codes load the dataset
            # get the path
            path = os.getcwd()
            # specify the path to the zip file
            zip_file_path = f"{path}/sign-language-mnist.zip"
            # extract the contents of the zip file to a directory if the directory does not exist
            if not os.path.exists(f"{path}/sign-language-mnist"):
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(f"{path}/sign-language-mnist")
            # Load the .csv files of the train and test data respectively.
            train_datafile = pd.read_csv(f"{path}/sign-language-mnist/sign_mnist_train.csv")
            test_datafile = pd.read_csv(f"{path}/sign-language-mnist/sign_mnist_test.csv")
            Classes = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

            # This is a helper function to convert all dataframes into numpy array
            def dataframe_to_nparray(train_df, test_df):
                train_df = train_df.copy(deep = True)
                test_df = test_df.copy(deep = True)
                train_images = train_df.iloc[:, 1:].to_numpy(dtype = 'float32')
                test_images = test_df.iloc[:, 1:].to_numpy(dtype = 'float32')
                return train_images,test_images

            train_img, test_img = dataframe_to_nparray(train_datafile, test_datafile)
            train_labels = train_datafile['label'].values
            test_labels = test_datafile['label'].values
            train_images_shaped = train_img.reshape(train_img.shape[0],1,28,28)
            test_images_shaped = test_img.reshape(test_img.shape[0],1,28,28)

            # Convert all numpy arrays into pytorch tensors
            train_images_tensors = torch.from_numpy(train_images_shaped)
            train_labels_tensors = torch.from_numpy(train_labels)
            test_images_tensors = torch.from_numpy(test_images_shaped)
            test_labels_tensors = torch.from_numpy(test_labels)

            # pytorch dataset
            train_dataset_full = TensorDataset(train_images_tensors, train_labels_tensors) #this dataset will further devided into validation dataset and training dataset
            test_dataset = TensorDataset(test_images_tensors, test_labels_tensors)
            img, label = train_dataset_full[0]
            
            # Hyperparmeters
            batch_size = batchsize
            learning_rate = 0.001
            num_epochs = epochNum
            # Other constants
            in_channels = 1
            input_size = in_channels * 28 * 28
            num_classes = 26
            opt_func = torch.optim.Adam

            # Split validation and train dataset
            random_seed = 11
            torch.manual_seed(random_seed);
            val_size = 7455
            train_size = len(train_dataset_full) - val_size
            train_dataset, validation_dataset = random_split(train_dataset_full, [train_size, val_size,])

            # This function gets the sign language images from train dataset
            def show_image(image, label):
                print("Alphabet: ", Classes[label.item()])
                plt.imshow(image.view(28,28))
            
            # Load the training,validation and test dataset in batches
            train_dataloder = DataLoader(train_dataset, batch_size, shuffle=True, num_workers=4, pin_memory=True)
            validation_dataloader = DataLoader(validation_dataset, batch_size*2, num_workers=4, pin_memory=True)
            test_dataloader = DataLoader(test_dataset, batch_size*2, num_workers=4, pin_memory=True)

            def accuracy(outputs, labels):
                _, preds = torch.max(outputs, dim=1)
                return torch.tensor(torch.sum(preds == labels).item() / len(preds))

            class ASLBase(nn.Module):
                def training_step(self, batch):
                    images, labels = batch 
                    out = self(images)                  # Generate predictions
                    loss = F.cross_entropy(out, labels) # Calculate loss
                    return loss
    
                def validation_step(self, batch):
                    images, labels = batch 
                    out = self(images)                    # Generate predictions
                    loss = F.cross_entropy(out, labels)   # Calculate loss
                    acc = accuracy(out, labels)           # Calculate accuracy
                    return {'val_loss': loss.detach(), 'val_acc': acc}
        
                def validation_epoch_end(self, outputs):
                    batch_losses = [x['val_loss'] for x in outputs]
                    epoch_loss = torch.stack(batch_losses).mean()   # Combine losses
                    batch_accs = [x['val_acc'] for x in outputs]
                    epoch_acc = torch.stack(batch_accs).mean()      # Combine accuracies
                    return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
                def epoch_end(self, epoch, result):
                    print("Epoch [{}], train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
                    epoch, result['train_loss'], result['val_loss'], result['val_acc']))

            class CNNModel(ASLBase):
                def __init__(self, in_channels, num_classes):
                    super().__init__()
                    self.network = nn.Sequential(
                        nn.Conv2d(in_channels, 28, kernel_size=3, padding=1),
                        nn.ReLU(),
                        nn.Conv2d(28, 28, kernel_size=3, stride=1, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(2, 2),     #image size : 28*14*14 
                        
                        nn.Conv2d(28, 56, kernel_size=3, stride=1, padding=1),
                        nn.ReLU(),
                        nn.Conv2d(56, 56, kernel_size=3, stride=1, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(2, 2),  # image size : 56*7*7
                        
                        nn.Flatten(), 
                        nn.Linear(56*7*7, 512),
                        nn.ReLU(),
                        nn.Linear(512, 128),
                        nn.ReLU(),
                        nn.Linear(128, num_classes))
        
                def forward(self, xb):
                    return self.network(xb)

            model = CNNModel(in_channels, num_classes)

            @torch.no_grad()
            def evaluate(model, val_loader):
                model.eval()
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

            def fit(epochs, lr, model, train_loader, val_loader, opt_func=torch.optim.SGD):
                history = []
                optimizer = opt_func(model.parameters(), lr)
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

            history = fit(num_epochs, 0.001 , model, train_dataloder, validation_dataloader, opt_func)
       
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

