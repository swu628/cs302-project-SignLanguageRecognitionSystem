from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
import torch
import torch.nn.functional as F
from TestImagesViewer import Ui_Dialog3
from dnn import DNNModel
from train import trainModel
from loadDataset import test_dataframe_to_pytorch
import os
import zipfile

class TestViewer(Ui_Dialog3):
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        
        self.tablewidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.pushButton_5.clicked.connect(self.delete_all_button_clicked)
        self.pushButton_5.clicked.connect(self.store_selected_rows)
        self.pushButton_6.clicked.connect(self.on_predict_button_click)

        # Set row height and column width for table widget
        self.tablewidget.horizontalHeader().setDefaultSectionSize(32)
        self.tablewidget.verticalHeader().setDefaultSectionSize(32)

        # Uncomment below lines to hide grid and headers in table widget
        #self.tableWidegt.setShowGrid(False)
        #self.tablewidget.horizontalHeader().setVisible(False)
        # self.tableWidegt.verticalHeader().setVisible(False)

        # Initialize file_path and select default dataset
        path = os.getcwd()
        zip_file_path = f"{path}/sign-language-mnist.zip"
        if not os.path.exists(f"{path}/sign-language-mnist"):
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(f"{path}/sign-language-mnist")
        self.file_path = f"{path}/sign-language-mnist/sign_mnist_test.csv"
        self.checkBox_3.setChecked(True)
        self.radioButton_2.setChecked(True)
        self.load_data()

        # Connect signals to slots for handling button clicks
        self.pushButton.clicked.connect(self.add_tag_button_clicked)
        self.pushButton_2.clicked.connect(self.clear_tags_button_clicked)
        self.pushButton_3.clicked.connect(self.filter_button_clicked)

        self.tablewidget.itemClicked.connect(self.on_item_clicked)


    # Slot to clear text browser when "Clear Tag" button is clicked
    def clear_tags_button_clicked(self):
        self.textBrowser.clear()

    # Function to load dataset from the selected file_path
    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    # Function to get label from the input character
    def get_label_from_char(self, char):
        return ord(char.upper()) - ord('A')

    # Function to filter data based on the label
    def filter_data(self, label):
        filtered_data = self.data[self.data['label'] == label]
        return filtered_data

       # Function to display images in the table widget
    def display_images(self, data):
        # Set the number of images per row in the table widget
        images_per_row = 16
        
        # Calculate the number of rows needed to display all images
        row_count = int(np.ceil(data.shape[0] / images_per_row))
        
        # Set the number of columns to the number of images per row
        col_count = images_per_row

        # Configure the table widget with the calculated row and column count
        self.tablewidget.setRowCount(row_count)
        self.tablewidget.setColumnCount(col_count)

        # Loop through each image in the filtered data
        for idx, (csv_row, image_data) in enumerate(data.iterrows(), start=0):

            # Reshape the image data into a 28x28 array and convert to uint8 format
            image_array = image_data[1:].values.reshape(28, 28).astype(np.uint8)
            
            # Create a QImage from the image array with the Grayscale format
            qimage = QImage(image_array.data, 28, 28, QImage.Format_Grayscale8)
            
            # Convert the QImage to a QPixmap
            pixmap = QPixmap.fromImage(qimage)
            
            # Create a QTableWidgetItem and set its decoration role to the QPixmap
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DecorationRole, pixmap)
            item.setData(QtCore.Qt.UserRole, csv_row)

            # Calculate the row and column position for the QTableWidgetItem in the table widget
            row = idx // images_per_row
            col = idx % images_per_row
            
            # Add the QTableWidgetItem to the table widget at the calculated position
            self.tablewidget.setItem(row, col, item)


    # Function to convert input character to label, taking into account the special mapping of characters to labels
    def get_label_from_char(self, char):
        # Check if the input character is 'J' or 'Z', as these characters are not valid in this dataset
        if char.upper() == 'J' or char.upper() == 'Z':
            # Display an error message to inform the user that 'J' and 'Z' are not valid input characters
            QtWidgets.QMessageBox.warning(None, "Invalid Input", "J and Z are not valid input characters.")
            return None
        # If the input character is between 'A' and 'I', calculate the corresponding label using the character's Unicode value
        elif 'A' <= char.upper() <= 'I':
            return ord(char.upper()) - ord('A')
        # If the input character is between 'K' and 'Y', calculate the corresponding label using the character's Unicode value
        # Note that we need to subtract an extra 1 here to account for the missing 'J' label
        elif 'K' <= char.upper() <= 'Y':
            return ord(char.upper()) - ord('A') 
        


    def on_item_clicked(self, item):
        csv_row = item.data(QtCore.Qt.UserRole)
        print(f"Clicked image is at row {csv_row} in the CSV file")

    def delete_all_button_clicked(self):
        self.tablewidget.clearSelection()

    def store_selected_rows(self):
        selected_items = self.tablewidget.selectedItems()
        selected_rows = []

        for item in selected_items:
            csv_row = item.data(QtCore.Qt.UserRole)
            selected_rows.append(csv_row)

        print("Selected rows in CSV:", selected_rows)
        

    # Slot to handle "Add Tag" button click
    def add_tag_button_clicked(self):
        tag = self.lineEdit.text().strip()
        if not tag:
            QtWidgets.QMessageBox.warning(None, "Empty Input", "Please enter a character.")
            return

        label = self.get_label_from_char(tag)
        if label is not None:
            self.add_tag(label)
            self.textBrowser.append(tag.upper())

    # Function to store the label for filtering
    def add_tag(self, label):
        self.label = label

    # Slot to handle "Filter" button click
    def filter_button_clicked(self):
        if self.data is None:
            QtWidgets.QMessageBox.warning(None, "No Dataset Selected", "Please select a dataset before filtering.")
            return

        filtered_data = self.filter_data(self.label)
        self.display_images(filtered_data)

    def predict(self,model_path, model_class, input_size, output_size, img):
        # Create a new model instance
        model = model_class(input_size, output_size)
        
        # Load the saved model parameters
        model.load_state_dict(torch.load(model_path))
        
        # Set the model to evaluation mode
        model.eval()

        # Perform prediction
        xb = img.unsqueeze(0)  # Add a batch dimension
        yb = model(xb)  # Get model predictions
        # Apply softmax to convert outputs to probabilities
        probs = F.softmax(yb, dim=1)
        # Get the prediction and its confidence
        confidence, preds = torch.max(probs, dim=1)
        
       # print("Predicted class:", preds[0].item())
       # #print("Confidence:", confidence[0].item())
        
        return preds[0].item(), confidence[0].item()
       

    def on_predict_button_click(self):
        selected_items = self.tablewidget.selectedItems()
        selected_rows = []
        for item in selected_items:
            csv_row = item.data(QtCore.Qt.UserRole)
            selected_rows.append(csv_row)
        print("Selected rows in CSV:", selected_rows)
        test_ds = test_dataframe_to_pytorch.load(self)

        model_path = "/Users/qinqi/Team10/未命名/qqin543/DNN.pth"
        input_size = 784
        output_size = 26

        for row in selected_rows:
            img, label = test_ds[row]
            A, B = self.predict(model_path, DNNModel, input_size, output_size, img)
            print(f"Prediction for row {row}:")
            print("Predicted class:", A)
            print("Confidence:", B)

            # Display the image and prediction in a dialog
            dialog = QDialog(None)

            dialog.setWindowTitle(f"Prediction for row {row}")
            layout = QVBoxLayout()

            # Image label
            image_label = QLabel(dialog)
            qimage = QImage(img.view(28, 28).numpy().astype(np.uint8), 28, 28, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimage)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

            # Prediction label
            prediction_label = QLabel(dialog)
            prediction_label.setText(f"Predicted class: {A}\nConfidence: {B}")
            layout.addWidget(prediction_label)

            dialog.setLayout(layout)
            dialog.exec_()




