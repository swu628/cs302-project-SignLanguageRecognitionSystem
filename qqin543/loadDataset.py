import os
import zipfile
import pandas as pd 
import torch
from torch.utils.data import TensorDataset, random_split, DataLoader
import matplotlib.pyplot as plt
            

class loadData:

    def load(self, batchSize, validationValue):  
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
        classes = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

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

        # Split validation and train dataset
        val_size = int(validationValue/100 * 27455)
        random_seed = 11
        torch.manual_seed(random_seed)
        train_size = len(train_dataset_full) - val_size
        train_dataset, validation_dataset = random_split(train_dataset_full, [train_size, val_size,])
        
        # Load the training,validation and test dataset in batches
        train_dataloder = DataLoader(train_dataset, batchSize, shuffle=True, num_workers=4, pin_memory=True)
        validation_dataloader = DataLoader(validation_dataset, batchSize*2, num_workers=4, pin_memory=True)
        test_dataloader = DataLoader(test_dataset, batchSize*2, num_workers=4, pin_memory=True)

        return train_dataloder, validation_dataloader, test_dataloader
