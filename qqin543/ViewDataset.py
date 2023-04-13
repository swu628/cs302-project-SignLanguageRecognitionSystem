import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap
from DatasetViewer import Ui_Dialog2

class DatasetViewer(Ui_Dialog2):
    def setupUi(self, Dialog, file_path):
        super().setupUi(Dialog)
        self.load_data(file_path)
        
        # Connect signals
        self.pushButton.clicked.connect(self.add_tag_button_clicked)
        self.pushButton_3.clicked.connect(self.filter_button_clicked)

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)

    def get_label_from_char(self, char):
        return ord(char.upper()) - ord('A')

    def filter_data(self, label):
        filtered_data = self.data[self.data['label'] == label]
        return filtered_data

    def display_images(self, data):
        self.tablewidget.setRowCount(data.shape[0])
        self.tablewidget.setColumnCount(1)

        for row, (_, image_data) in enumerate(data.iterrows()):
            image_array = image_data[1:].values.reshape(28, 28).astype(np.uint8)
            qimage = QImage(image_array.data, 28, 28, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimage)
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DecorationRole, pixmap)
            self.tablewidget.setItem(row, 0, item)

    def get_label_from_char(self, char):
        char = char.upper()
        if char == "J" or char == "Z":
            raise ValueError("Gesture for letter J and Z are not available in the dataset.")
        char_code = ord(char) - ord('A')
        if char_code >= 9:
            char_code -= 1
        return char_code

    def add_tag_button_clicked(self):
        char = self.lineEdit.text()
        self.label = self.get_label_from_char(char)
        self.textBrowser.append(char)

    def filter_button_clicked(self):
        filtered_data = self.filter_data(self.label)
        self.display_images(filtered_data)
