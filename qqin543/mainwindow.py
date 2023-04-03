import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QCheckBox, QRadioButton, QPushButton, QTableWidget, QSlider, QProgressBar, QTabWidget, QFileDialog, QGraphicsScene, QGraphicsView, QSplitter, QListWidget, QListWidgetItem, QLineEdit, QGroupBox,QTextEdit)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage

from connector import Connector

class GestureRecognitionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connector = Connector()  # 创建Connector实例
        self.selected_file_path = None
        
        self.setWindowTitle("手势识别")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

       # self.output_text_edit = QTextEdit()
       # self.output_text_edit.setReadOnly(True)  # 设置为只读模式
        #self.layout.addWidget(self.output_text_edit)


        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.import_tab = QWidget()
        self.training_tab = QWidget()
        self.prediction_tab = QWidget()

        self.tab_widget.addTab(self.import_tab, "导入数据集")
        self.tab_widget.addTab(self.training_tab, "训练模型")
        self.tab_widget.addTab(self.prediction_tab, "预测")

        self.init_import_tab()
        self.init_training_tab()
        self.init_prediction_tab()
        self.init_output_text_edit()


    def init_import_tab(self):
        self.import_layout = QVBoxLayout()
        self.import_tab.setLayout(self.import_layout)
        self.import_layout.addStretch(2)
        self.dataset_combo_box = QComboBox()
        self.dataset_combo_box.addItem("Select Dataset")
        self.dataset_combo_box.addItem("MNIST")
        self.import_layout.addWidget(self.dataset_combo_box)

        self.dataset_combo_box.currentIndexChanged.connect(self.choose_dataset)

        self.import_button = QPushButton("Import")
        self.import_layout.addWidget(self.import_button)
        self.import_button.clicked.connect(self.load_selected_dataset)

        self.cancel_button = QPushButton("Cancel")
        self.import_layout.addWidget(self.cancel_button)
        self.cancel_button.clicked.connect(self.cancel_import)
        self.import_layout.addStretch(1)
        
        self.import_layout.addStretch(3)
        self.progress_label = QLabel("导入进度：")
        self.import_layout.addWidget(self.progress_label)
        
        
        

        self.progress_bar = QProgressBar()
        self.import_layout.addWidget(self.progress_bar)
        self.import_layout.addStretch(1)
        self.selected_dataset = None



        # ...

    def init_output_text_edit(self):
        self.output_text_edit = QTextEdit(self)
        self.layout.addWidget(self.output_text_edit)
        self.layout.setAlignment(self.output_text_edit, Qt.AlignBottom)
        
        

        self.output_text_edit.setFixedHeight(30)  # 根据字体大小调整高度
        self.output_text_edit.setReadOnly(True)  # 设置为只读
    

    
    def print_to_gui(self, text):
        self.output_text_edit.clear()  # 清除之前的文本
        cursor = self.output_text_edit.textCursor()
        cursor.insertHtml('<p align="center" style="color: blue;">{}</p>'.format(text))
        self.output_text_edit.setTextCursor(cursor)


    def choose_dataset(self, index):
        if index == 0:
            self.print_to_gui("请选择一个数据集")
            self.selected_file_path = None  # 将 selected_file_path 设置为 None  
        elif index == 1:
            self.print_to_gui("选择了MNIST数据集")
            self.selected_file_path = "/Users/qinqi/Downloads/archive/sign_mnist_train.csv"  # 这里替换为您的MNIST文件路径
    
    def load_selected_dataset(self):
      
        if self.selected_file_path:
        # 调用连接部分的方法来加载数据集
            self.data, progress = self.connector.load_dataset(self.selected_file_path)
            
            self.progress_bar.setValue(progress) 
            
            self.print_to_gui(f"数据集已加载")
        else:
            self.print_to_gui("未选择数据集")

    
    # ...
    def cancel_import(self):
            self.print_to_gui("取消导入")
            self.progress_bar.setValue(0)
        #    在这里清除已加载的数据集




    def init_training_tab(self):
        self.training_layout = QVBoxLayout()
        self.training_tab.setLayout(self.training_layout)

        # DNN Model Selection
        self.model_selection_group = QGroupBox("选择深度神经网络")
        self.training_layout.addWidget(self.model_selection_group)
        self.model_selection_layout = QVBoxLayout()
        self.model_selection_group.setLayout(self.model_selection_layout)

        self.model_combo_box = QComboBox()
        self.model_combo_box.addItems(["Model 1", "Model 2", "Model 3"])
        self.model_selection_layout.addWidget(self.model_combo_box)

        # Hyperparameters
        self.hyperparameters_group = QGroupBox("超参数设置")
        self.training_layout.addWidget(self.hyperparameters_group)
        self.hyperparameters_layout = QVBoxLayout()
        self.hyperparameters_group.setLayout(self.hyperparameters_layout)

        self.batch_size_label = QLabel("批次大小：")
        self.hyperparameters_layout.addWidget(self.batch_size_label)

        self.batch_size_line_edit = QLineEdit()
        self.hyperparameters_layout.addWidget(self.batch_size_line_edit)

        self.epochs_label = QLabel("训练次数：")
        self.hyperparameters_layout.addWidget(self.epochs_label)

        self.epochs_line_edit = QLineEdit()
       
        self.hyperparameters_layout.addWidget(self.epochs_line_edit)

        # Training Progress
        self.training_progress_group = QGroupBox("训练进度")
        self.training_layout.addWidget(self.training_progress_group)
        self.training_progress_layout = QVBoxLayout()
        self.training_progress_group.setLayout(self.training_progress_layout)

        self.train_progress_bar = QProgressBar()
        self.training_progress_layout.addWidget(self.train_progress_bar)

        self.train_button = QPushButton("开始训练")
        self.training_layout.addWidget(self.train_button)
        self.train_button.clicked.connect(self.start_training)

    def start_training(self):
        self.print_to_gui("开始训练")
        # 在这里处理模型训练
        # 更新训练进度条
        self.train_progress_bar.setValue(50)  # 示例进度值

    def init_prediction_tab(self):
        self.prediction_layout = QVBoxLayout()
        self.prediction_tab.setLayout(self.prediction_layout)

        self.load_model_button = QPushButton("加载已训练的模型")
        self.prediction_layout.addWidget(self.load_model_button)

        self.load_model_button.clicked.connect(self.load_trained_model)

        self.choose_images_button = QPushButton("选择测试图像")
        self.prediction_layout.addWidget(self.choose_images_button)

        self.choose_images_button.clicked.connect(self.choose_test_images)

        self.prediction_result_label = QLabel("预测结果：")
        self.prediction_layout.addWidget(self.prediction_result_label)

        self.predict_button = QPushButton("开始预测")
        self.prediction_layout.addWidget(self.predict_button)
        self.predict_button.clicked.connect(self.start_prediction)

    def load_trained_model(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "加载已训练的模型", "", "Model Files (*.pth);;All Files (*)", options=options)
        if file_name:
            self.print_to_gui_to_gui("加载的模型文件:", file_name)
            # 在这里加载模型

    def choose_test_images(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "选择测试图像", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if files:
            self.print_to_gui("选择的测试图像:", files)
            # 在这里处理测试图像

    def start_prediction(self):
        self.print_to_gui("开始预测")
        # 在这里处理预测
        # 更新预测结果标签
        self.prediction_result_label.setText("预测结果：A")  # 示例预测结果

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestureRecognitionGUI()
    window.show()
    sys.exit(app.exec_())

