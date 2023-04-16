import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap
from TestImagesViewer import Ui_Dialog3
import os
import zipfile

class TestViewer(Ui_Dialog3):
    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        # Set row height and column width for table widget
        self.tablewidget.horizontalHeader().setDefaultSectionSize(28)
        self.tablewidget.verticalHeader().setDefaultSectionSize(28)

        # Uncomment below lines to hide grid and headers in table widget
        # self.tableWidegt.setShowGrid(False)
        # self.tableWidegt.horizontalHeader().setVisible(False)
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
        for idx, (_, image_data) in enumerate(data.iterrows()):
            # Reshape the image data into a 28x28 array and convert to uint8 format
            image_array = image_data[1:].values.reshape(28, 28).astype(np.uint8)
            
            # Create a QImage from the image array with the Grayscale format
            qimage = QImage(image_array.data, 28, 28, QImage.Format_Grayscale8)
            
            # Convert the QImage to a QPixmap
            pixmap = QPixmap.fromImage(qimage)
            
            # Create a QTableWidgetItem and set its decoration role to the QPixmap
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DecorationRole, pixmap)

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

