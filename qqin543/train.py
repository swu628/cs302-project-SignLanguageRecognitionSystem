import torch
from loadDataset import loadData
from cnn import CNNModel
from logisticRegression import logisticRegressionModel
from dnn import DNNModel

class trainModel:

    # This is the function to call when the train button is clicked
    def train(self, batchSize, epochNum, validationValue):

        global model
        
        # load dataset
        train_dataloder, validation_dataloader, test_dataloader = loadData.load(self, batchSize, validationValue)

        # If the user choose lenet5 model, it will call the leNet5 class
        if self.selectModelComboBox.currentIndex() == 1:
            
            model = logisticRegressionModel(in_channels = 1, num_classes = 26)

            def evaluate(model, val_loader):
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

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

            history = fit(epochNum, 0.001, model, train_dataloder, validation_dataloader)

        elif self.selectModelComboBox.currentIndex() == 2:

            # import cnn model
            model = CNNModel(in_channels = 1, num_classes = 26)

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

            model = DNNModel(784, out_size = 26)
            history = []

            def evaluate(model, val_loader):
                outputs = [model.validation_step(batch) for batch in val_loader]
                return model.validation_epoch_end(outputs)

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

            history += fit(epochNum, .001, model, train_dataloder, validation_dataloader)

        else:
            print("Please select a model")

    # Save the model with user input name
    def saveModel(self, fileName):
        torch.save(model.state_dict(), fileName + ".pth")