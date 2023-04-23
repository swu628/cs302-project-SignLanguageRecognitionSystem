# Import relevant libraries
import torch
import torch.nn as nn
import torch.nn.functional as F


'''
Purpose: This class is the logic behind the dnn model

Source: Sachin Som. “Image Classification (American Sign Language) Using PyTorch.” 
Medium. https://jovian.ml/sachinsom507/final-project-sign-language-prediction (accessed Apr 23, 2023).

Inputs: It takes in the batch size and epoch number that the users have selected. 
An input tensor of size 784, representing the number of pixels in a 28x28 image, 
and returns an output tensor of size 26, representing the number of classes. 

Outputs: Dispite the logic behind the model, there are other functions which 
returns the validation loss, accuracy and the round of epochs to the command.
'''
class DNNModel(nn.Module):
    # Feedfoward neural network with 2 hidden layer
    def __init__(self, in_size, out_size):
        super().__init__()
        # hidden layer 1
        self.linear1 = nn.Linear(in_size, 512)
        # hidden layer 2
        self.linear2 = nn.Linear(512, 256)
        # hidden layer 3
        self.linear3 = nn.Linear(256, 128)
        # output layer  
        self.linear4 = nn.Linear(128, out_size)
        
    def forward(self, xb):
        # Flatten the image tensors
        out = xb.view(xb.size(0), -1)
        # Get intermediate outputs using hidden layer 1
        out = self.linear1(out)
        # Apply activation function
        out = F.relu(out)
        # Get intermediate outputs using hidden layer 2
        out = self.linear2(out)
        # Apply activation function
        out = F.relu(out)
        # Get inermediate outputs using hidden layer 3
        out = self.linear3(out)
        # Apply a activation function
        out = F.relu(out)
        # Get predictions using output layer
        out = self.linear4(out)
        return out
    
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
        return {'val_loss': loss, 'val_acc': acc}
        
    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()   # Combine losses
        batch_accs = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_accs).mean()      # Combine accuracies
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
    def epoch_end(self, epoch, result):
        print("Epoch [{}], val_loss: {:.4f}, val_acc: {:.4f}".format(epoch, result['val_loss'], result['val_acc']))

def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))