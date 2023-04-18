import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from dnn import DNNModel
from loadDataset import loadData

class Predictor:
    def __init__(self, model_path, model_class, input_size, output_size):
        self.model = model_class(input_size, output_size)
        self.load_model(model_path)
    
    def load_model(self, model_path):
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
    
    def predict_image(self, img):
        xb = img.unsqueeze(0)
        yb = self.model(xb)
        probs = F.softmax(yb, dim=1)
        confidence, preds = torch.max(probs, dim=1)
        return preds[0].item(), confidence[0].item()
    
    def display_prediction(self, img, prediction, confidence):
        plt.imshow(img, cmap='gray')
        plt.title(f"Predicted class: {prediction}\nConfidence: {confidence:.4f}")
        plt.axis('off')
        plt.show()


model_path = "/Users/qinqi/Team10/未命名/qqin543/CNN.pth"
input_size = 784
output_size = 26
predictor = Predictor(model_path, DNNModel, input_size, output_size)

prediction, confidence = predictor.predict_image(img)
predictor.display_prediction(img, prediction, confidence)