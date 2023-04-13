import time
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2




class Ui_Dialog5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 438)

        # Set up grid layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Configure 'Cancel' button
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        # Configure 'Open Camera' button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        # Configure 'Predict' button
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        # Set up QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        # Hide row and column numbers
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)


        self.pushButton.clicked.connect(self.capture_image)

        # Connect Cancel Button click signal to QDialog reject slot
        self.pushButton_3.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        # Capture images using the webcam
    def capture_image(self):
            # Display an information             
            cap = cv2.VideoCapture(0)

            while True:
                # Capture frame-by-frame
                ret, frame = cap.read()
                
                # Display an information 
                cv2.putText(frame, "Press 'S' to save a photo, 'Q' to quit the camera.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Display the resulting frame
                cv2.imshow('Camera', frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord('s'):
                    # Save the captured image to a file
                    image_filename = f"captured_image_{time.strftime('%Y%m%d_%H%M%S')}.png"
                    cv2.imwrite(image_filename, frame)

                    # Add the saved image to the QTableWidget
                    self.add_image_to_table(image_filename)
                elif key == ord('q'):
                    break

        # When everything is done, release the capture and close the window
            cap.release()
            cv2.destroyAllWindows()


    # Add an image to the QTableWidget
    def add_image_to_table(self, image_path):
        row, col = self.tableWidget.rowCount(), self.tableWidget.columnCount()

        if row == 0 and col == 0:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            row = 1
            col = 1

        # Check if the last row is full
        if col == self.tableWidget.columnCount():
            self.tableWidget.setRowCount(row + 1)
            row += 1
            col = 0

        # Create a QTableWidgetItem with the image
        image = QtGui.QPixmap(image_path)
        icon = QtGui.QIcon(image)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)

        # Set the size of the QTableWidgetItem to a fixed size
        item.setSizeHint(QtCore.QSize(128, 128))
        self.tableWidget.setRowHeight(row - 1, 128)
        self.tableWidget.setColumnWidth(col, 128)
        self.tableWidget.setIconSize(QtCore.QSize(150, 150))

        # Insert the QTableWidgetItem into the QTableWidget
        self.tableWidget.setItem(row - 1, col, item)

        # Update the column count for the next image
        self.tableWidget.setColumnCount(col + 1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Capture Images"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Open Camera"))
        self.pushButton_2.setText(_translate("Dialog", "Predict"))
