# Import relevant libraries
import torch
import torch.nn as nn
import torch.nn.functional as F


'''
Purpose: This class is the logic behind the logistic regression model

Source: Sachin Som. “Image Classification (American Sign Language) Using PyTorch.” 
Medium. https://jovian.ml/sachinsom507/final-project-sign-language-prediction (accessed Apr 23, 2023).

Inputs: It takes in the batch size and epoch number that the users have selected. 
Number of channels (1 for greyscale images) and number of classes of the dataset used 
(26 for MNIST sign language dataset).

Outputs: Dispite the logic behind the model, there are other functions which 
returns the validation loss, accuracy and the round of epochs to the command.
'''
class logisticRegressionModel(nn.Module):

    def __init__(self, in_channels, num_classes):
        super().__init__()
        self.linear = nn.Linear(in_channels*28*28, num_classes)
        
    def forward(self, xb):
        xb = xb.reshape(-1, 1*28*28)
        out = self.linear(xb)
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
        return {'val_loss': loss.detach(), 'val_acc': acc.detach()}
        
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