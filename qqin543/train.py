# Import relevent libraries
import torch
from loadDataset import loadData
from cnn import CNNModel
from logisticRegression import logisticRegressionModel
from dnn import DNNModel
from PyQt5 import QtWidgets


'''
Purpose: This class is used to train the models when the user have selected a model.

Source: Sachin Som. “Image Classification (American Sign Language) Using PyTorch.” 
Medium. https://jovian.ml/sachinsom507/final-project-sign-language-prediction (accessed Apr 23, 2023).

Inputs: It contains two functions, train and save. 
- The inputs of train function is the batch size epoch number and the validation value that the user 
chosen to split on the train dataset.
- The input of the save function is the filename that the user have inputting from the GUI.

Outputs: train function starts training progress, and the save function will return a saved trained model.
'''
class trainModel:

    # This is the function to call when the train button is clicked
    def train(self, batchSize, epochNum, validationValue):

        global model

        # Load dataset
        train_dataloder, validation_dataloader, test_dataloader = loadData.load(self, batchSize, validationValue)

        # If the user choose logistic regression model, it will call the logistic regression class
        if self.selectModelComboBox.currentIndex() == 1:
            
            # Import logistic regression model
            model = logisticRegressionModel(in_channels = 1, num_classes = 26)

            # This function will be called in the 'fit' function
            def evaluate(model, val_loader):
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)
            
            # This function will train the dataset on the logistic regression model 
            # and return the validation loss and accuracy
            def fit(epochs, lr, model, train_loader, val_loader, opt_func=torch.optim.SGD):
                history = []
                optimizer = opt_func(model.parameters(), lr)
                for epoch in range(epochs):
                    # Training Phase 
                    for batch in train_loader:
                        loss = model.training_step(batch)
                        loss.backward()
                        optimizer.step()
                        optimizer.zero_grad()
                    # Validation phase
                    result = evaluate(model, val_loader)
                    model.epoch_end(epoch, result)
                    history.append(result)
                return history
            
            # Call the function and return for connecting to UI
            history = fit(epochNum, 0.001, model, train_dataloder, validation_dataloader)
            return history

        # If the user choose cnn model, it will call the cnn class
        elif self.selectModelComboBox.currentIndex() == 2:

            # Import cnn model
            model = CNNModel(in_channels = 1, num_classes = 26)

            # This function will be called in the 'fit' function
            @torch.no_grad()
            def evaluate(model, val_loader):
                model.eval()
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

            # This function will train the dataset on the cnn model and return the validation loss and accuracy
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

            # Call the function and return for connecting to UI
            history = fit(epochNum, 0.001, model, train_dataloder, validation_dataloader)
            return history

        # If the user choose dnn model, it will call the dnn class
        elif self.selectModelComboBox.currentIndex() == 3:

            # Import dnn model
            model = DNNModel(784, out_size = 26)
            history = []

            # This function will be called in the 'fit' function
            def evaluate(model, val_loader):
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

            # This function will train the dataset on the dnn model and return the validation loss and accuracy
            def fit(epochs, lr, model, train_loader, val_loader, opt_func=torch.optim.SGD):
                optimizer = opt_func(model.parameters(), lr)
                for epoch in range(epochs):
                    # Training Phase 
                    for batch in train_loader:
                        loss = model.training_step(batch)
                        loss.backward()
                        optimizer.step()
                        optimizer.zero_grad()
                    # Validation phase
                    result = evaluate(model, val_loader)
                    model.epoch_end(epoch, result)
                    history.append(result)
                return history

            # Call the function and return for connecting to UI
            history += fit(epochNum, 0.001, model, train_dataloder, validation_dataloader)
            return history

        else:
            # Show warning message if no model was selected
            QtWidgets.QMessageBox.warning(None, "No Model Selected", "Please select a model before training.")

    # Save the model with user input name
    def saveModel(self, fileName):
        torch.save(model.state_dict(), fileName + ".pth")