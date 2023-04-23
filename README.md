# Sign Language Recognition System

## Introduction of team
This project is completed by Qi Qin and Kylyn Wu at April 23, 2023.

## Introduction to our system
We are developing a sign language recognition system to assist hard-of-hearing people in communicating with others. In this project, the system will train on a dataset for sign language recognition using multiple NN models, then make predictions on the test dataset and demonstrate testing accuracy. The system should also be able to use the camera to recognise a person's hand gesture and determine what letter the gesture represents.

## Dataset used
As our dataset, we decided to use the MNIST sign language recognition from Kaggle. Each image is 28 by 28 grayscale pixels. In addition, the dataset includes roughly over 27,000 training images and approximately 7,000 test images. 

## Models used
Additionally, we employed logistic regression, CNN, and DNN as architectures. The first model is an uncomplicated algorithm that is simple to implement. CNN contributes favourably to the MNIST sign language dataset. DNN is a multi-layered neural network utilised in various applications, including speech recognition and natural language processing.

## Methodologies used
### Pattern
Our team is developing the system using the agile methodology. That is a highly adaptable, interactive process. We can move back and forth between phases when we discover that our system requires refinement.

### Software environments
The chosen software environments are PyTorch, Pyqt5, and OpenCV. Pytorch has many integrated features that facilitate the creation and training of neural networks. PyQt5 was used to build our GUI in Python. OpenCV is used to capture user gestures from the camera.

### Tools
Visual Studio Code, GitHub, QtDesigner, and Figma have been utilised. VS Code is our development IDLE, while GitHub is our version control and collaborative software development platform. QtDesigner performs our GUI. Figma is our prototyping tool.

## Key functionalities of our system
Our system has serveral key functions will includes:
1. Import dataset
* Download dataset
* Delete downloaded dataset
* Display error message if no dataset downloaded
2. View dataset
* Add tag
* Customise filter
* View train/test dataset
* Show statistics of the dataset
3. Train
* Select model
* Customise hyperparameters
* Split train/validation set
* Show training loss and validation accuracy
* Save trained model
4. Test
* Load trained model
* Predicting using camera
* Show prediction result (with accuracy)
* View test set and choose images for testing