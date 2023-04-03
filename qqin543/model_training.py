# 在模型训练和处理部分的代码中

import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    # 在这里对数据进行预处理，例如：分割训练集和测试集、对数据进行归一化等
    return data
