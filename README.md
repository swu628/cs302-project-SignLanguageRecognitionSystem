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

## Version Iteration
### Version-0.5
*   Our project officially started, and my teammates and I implemented the UI prototype in Figma, mainly using Windows to display various stages. Although the functionalities were not connected, the entire interface looked messy. We held a team meeting to prepare for restructuring the UI.

### Version-1.0
*   We redesigned a clean UI, replacing the complex Windows with a neat QTabWidget, and implemented the overall UI framework through coding. We held another team meeting to discuss our main features and design implementation methods.
### Version-2.0
*   In this version, we have implemented all the UI designs, and added pop-up Dialogs for implementing main features and auxiliary functions.

### Version-2.5
*   Our team's model designer constructed our first model, marking a significant breakthrough.

### Version-3.0
*   In this version, our project has entered a stage of meticulous division of labor and achieved important progress, successfully connecting the Model and UI.

*   In terms of Model design:
    Our model designer has fully constructed the completed Training Process Users
    can access all the training functions by clicking buttons in the UI, 
    including setting the test and training dataset ratio and training the model.
    We chose accuracy as the evaluation criterion and obtained satisfactory 
    training results, but the results are not yet displayed in the UI, and the 
    trained model cannot be saved.
    
    It's worth noting that in this version, we abandoned the Lenet-5 model and
    replaced it with a better-performing CNN model after testing.

*   In terms of UI development:
    Our UI designer has implemented remote dataset downloading and several
    essential features after loading the dataset, such as View Dataset and
    Display Dataset Statistics.

### Version-3.5
*   In this version, we implemented the use of the user's camera. We utilized the OpenCV library to mirror the captured image, process it into a 28x28 pixel grayscale image, but background noise could not be eliminated, and the image aspect ratio was distorted.

### Version-4.0
*   Our project has achieved milestone progress in this version.

*   In terms of model design:
    The model designer constructed all the required models and obtained the
    optimal training parameters. We used confidence as the evaluation criterion 
    for prediction accuracy and tested the accuracy of the three models on the 
    test set separately. The CNN model performed best, while the DNN model and 
    logistic regression model had relatively poor recognition results for noisy 
    background images.
    
*   In image processing:
    We maintained the original aspect ratio after resizing the image, minimizing 
    background noise to the greatest extent.

*   In UI construction:
    We connected the prediction function of the three models to the camera, but 
    have not yet determined how to pass the captured image data to the prediction 
    function.
    
### Version-4.5
*   After discussing with the model designer, we finally decided to flatten the grayscale values of the captured image and write them into a CSV file. The prediction function will directly read the CSV file and use the Test Set prediction function for predictions.

    We fixed UI logic bugs and added necessary QMessageBoxes to prevent improper 
    operations from causing the program to exit.
    
### Version-5.0
*   Our team has completed all the coding work and added detailed comments to the code. Our tool has entered the maintenance phase. Our next task is to conduct extensive testing and fix any bugs exposed during the testing process.






