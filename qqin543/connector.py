# 连接部分的代码（例如，connector.py）

from model_training import load_data

class Connector:
    def load_dataset(self, file_path):
        print(f"加载数据集文件: {file_path}")
        # 在这里调用模型处理部分的方法来加载数据集
        self.data = load_data(file_path)
        print(f"数据集已加载")
        # 返回数据集和加载进度（示例值）
        return self.data, 100

