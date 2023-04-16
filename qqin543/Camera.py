import time
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

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

    def capture_image(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.putText(frame, "Press 'S' to save a photo, 'Q' to quit the camera.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow('Camera', frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('s'):
                image_filename = f"captured_image_{time.strftime('%Y%m%d_%H%M%S')}.png"
                cv2.imwrite(image_filename, frame)
                self.add_image_to_table(image_filename)

                # Load the saved image
                img = cv2.imread(image_filename)

                # Convert the image to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Create a skin color range mask to detect the hand
                lower_skin = np.array([0, 20, 70], dtype=np.uint8)
                upper_skin = np.array([20, 255, 255], dtype=np.uint8)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, lower_skin, upper_skin)

                # Apply the mask to the grayscale image
                res = cv2.bitwise_and(gray, gray, mask=mask)

                # Find contours in the masked image
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                #
                max_area = -1
                max_cnt = None
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > max_area:
                        max_area = area
                        max_cnt = cnt

                # If a hand contour is found, extract the hand region
                if max_cnt is not None:
                    x, y, w, h = cv2.boundingRect(max_cnt)
                    hand_region = gray[y:y+h, x:x+w]
                     
                    # Resize the hand region to 28x28
                    blurred = cv2.GaussianBlur(hand_region, (5, 5), 0)
                    resized_hand = cv2.resize(hand_region, (28, 28), interpolation=cv2.INTER_CUBIC)



                    # Save the resized hand image
                    hand_filename = f"hand_image_{time.strftime('%Y%m%d_%H%M%S')}.png"
                    cv2.imwrite(hand_filename, resized_hand)

                    # Add the resized hand image to the QTableWidget
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

            item.setSizeHint(QtCore.QSize(128, 128))
            self.tableWidget.setRowHeight(row - 1, 128)
            self.tableWidget.setColumnWidth(col, 128)
            self.tableWidget.setIconSize(QtCore.QSize(150, 150))

            self.tableWidget.setItem(row - 1, col, item)

            self.tableWidget.setColumnCount(col + 1)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Capture Images"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Open Camera"))
        self.pushButton_2.setText(_translate("Dialog", "Predict"))

