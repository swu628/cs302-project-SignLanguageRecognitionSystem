import os
import time
import torch.nn.functional as F
import cv2
import csv
from PIL import Image
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QScrollArea
import pandas as pd
import torch
from cnn import CNNModel
from logisticRegression import logisticRegressionModel
from dnn import DNNModel
from loadDataset import test_dataframe_to_pytorch

class Ui_Dialog5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 438)
        # Set up grid layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Configure 'Cancel' button
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_4.clicked.connect(self.save_selected_images_to_csv)


        # Configure 'Cancel' button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        # Configure 'Predict' button
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_2.clicked.connect(self.on_predict_button_click)


        # Set up QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        # Hide row and column numbers
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        # Allow user choose multiple test set images used for prediction
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.pushButton.clicked.connect(self.capture_image)

        # Connect Cancel Button click signal to QDialog reject slot
        self.pushButton_3.clicked.connect(Dialog.reject)

        #self.tableWidget.itemClicked.connect(self.on_item_clicked)

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Initialize file_path and select default dataset
        path = os.getcwd()
        self.file_path = f"{path}/sign_mnist_test的副本.csv"
        

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()

            # Flip the image horizontally
            frame = cv2.flip(frame, 1)

            cv2.putText(frame, "Press 'S' to save a photo, 'Q' to quit the camera.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow('Camera', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                # Convert to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Calculate new dimensions while preserving the aspect ratio
                height, width = gray.shape
                aspect_ratio = float(width) / height
                if width > height:
                    new_width = int(28 * aspect_ratio)
                    new_height = 28
                else:
                    new_height = int(28 / aspect_ratio)
                    new_width = 28
                
                # Resize while preserving the aspect ratio
                resized_gray = cv2.resize(gray, (new_width, new_height), interpolation=cv2.INTER_AREA)

                # Calculate the position to crop the 28x28 image
                y_offset = (new_height - 28) // 2
                x_offset = (new_width - 28) // 2

                # Crop the 28x28 image without black borders
                final_image = resized_gray[y_offset:y_offset+28, x_offset:x_offset+28]

                hand_filename = f"hand_image_{time.strftime('%Y%m%d_%H%M%S')}.png"
                cv2.imwrite(hand_filename, final_image)
                self.add_image_to_table(hand_filename)
            elif key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    def add_image_to_table(self, image_path):
        row, col = self.tableWidget.rowCount(), self.tableWidget.columnCount()

        if row == 0 and col == 0:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            row = 1
            col = 1

        if col == self.tableWidget.columnCount():
            self.tableWidget.setRowCount(row + 1)
            row += 1
            col = 0

        image = QtGui.QPixmap(image_path)
        icon = QtGui.QIcon(image)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)

        item.setSizeHint(QtCore.QSize(32, 32))
        self.tableWidget.setRowHeight(row - 1, 32)
        self.tableWidget.setColumnWidth(col, 32)
        self.tableWidget.setIconSize(QtCore.QSize(32, 32))
        item.setData(QtCore.Qt.UserRole, image_path)

        self.tableWidget.setItem(row - 1, col, item)

        self.tableWidget.setColumnCount(col + 1)

        
    import pandas as pd

    def save_selected_images_to_csv(self):
        selected_items = self.tableWidget.selectedItems()
        csv_path = self.file_path

        # Initialize a list to store row indices
        self.images_indices = []

        # Read the CSV file into a DataFrame
        try:
            df = pd.read_csv(csv_path, header=None)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame()

        for item in selected_items:
            # Get image path
            image_path = item.data(QtCore.Qt.UserRole)
            # Open the image, convert it to grayscale, resize to 28x28, and flatten pixel values to a 1D array
            img = Image.open(image_path).convert('L')
            img = img.resize((28, 28), Image.ANTIALIAS)
            pixel_values = np.array(img).flatten()
            # Insert 0 at the beginning of the pixel values list
            pixel_values = np.insert(pixel_values, 0, 0)

            # Add the pixel values as a row in the DataFrame
            df = df.append(pd.Series(pixel_values), ignore_index=True)

            # Add the current row count to the row_indices list
            self.images_indices.append(len(df) - 1)

        # Write the DataFrame back to the CSV file
        df.to_csv(csv_path, index=False, header=None)

        # Return the list of row indices
        return self.images_indices


    def predict(self, model_path, model_class, input_size, output_size, img):
    # Helper function to convert label to character
        def get_char_from_label(label):
            if 0 <= label <= 8:
                return chr(label + ord('A'))
            elif 9 <= label <= 24:
                return chr(label + ord('A'))  # Add 1 to account for the missing 'J' label
            else:
                return None

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

        # Convert the predicted label to the corresponding character
        predicted_char = get_char_from_label(preds[0].item())

        return predicted_char, round(confidence[0].item(), 4)

    
    def get_File_Path(self,path):
        self.Model_File_Path = path
        
    def get_Combobox_Value(self,data1):
        self.Value = data1
        print(self.Value)
    
    def on_predict_button_click(self):
        
        
        #for item in selected_items:
        #    csv_row = item.data(QtCore.Qt.UserRole)
        #    selected_rows.append(csv_row)
        #print("Selected rows in CSV:", selected_rows)
        test_ds = test_dataframe_to_pytorch.load(self,self.file_path)
        

        

        model_path = self.Model_File_Path
        if model_path:
            print(f"Selected file path: {model_path}")
        else:
            print("No file was selected.")
        
        print(f"self.Value: {self.Value}")

        if self.Value == 1:
            
            model_calss= logisticRegressionModel
            in_channels = 1
            num_classes = 26
            input_size  = in_channels
            output_size = num_classes 

        elif self.Value == 2:

            model_calss= CNNModel
            in_channels = 1
            num_classes = 26
            input_size  = in_channels
            output_size = num_classes 

        elif self.Value == 3:

            model_calss= DNNModel
            input_size  = 784
            output_size = 26
      

        # 确保 row_indices 中的值在有效范围内
        valid_row_indices = [row for row in self.images_indices if 0 <= row < len(test_ds)]
        
        # Create the dialog and layout outside the loop
        dialog = QDialog(None)
        dialog.setWindowTitle("Predictions")
        scroll_area = QScrollArea(dialog)
        scroll_area.setWidgetResizable(True)

        # Container widget for the images and predictions
        container = QWidget()
        layout = QVBoxLayout(container)
        
        
        for row in valid_row_indices:
            
            img, label = test_ds[row]
            
            A, B = self.predict(model_path, model_calss, input_size, output_size, img)
            print(f"Prediction for row {row}:")
          
            print("Predicted class:", A)
            print("Confidence:", B)

            # Image label
            image_label = QLabel()
            qimage = QImage(img.view(28, 28).numpy().astype(np.uint8), 28, 28, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimage)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

            # Prediction label
            prediction_label = QLabel()
            prediction_label.setText(f"Prediction for row: {row}\nPredicted class: {A}\nConfidence: {B}")
            layout.addWidget(prediction_label)

     # Set up the scroll area and dialog layout
        scroll_area.setWidget(container)
        dialog_layout = QVBoxLayout(dialog)
        dialog_layout.addWidget(scroll_area)
        dialog.setLayout(dialog_layout)
        dialog.exec_()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Capture Images"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Open Camera"))
        self.pushButton_2.setText(_translate("Dialog", "Predict"))
        self.pushButton_4.setText(_translate("Dialog", "Save Images"))

