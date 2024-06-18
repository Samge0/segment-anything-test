#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-06-05 13:51
# describe：

import os
from matplotlib import pyplot as plt
import torch
from segment_anything import SamPredictor, sam_model_registry
from PIL import Image
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print("device = ", device)

model_path = "checkpoints/sam_vit_h_4b8939.pth"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# 加载预训练模型
sam = sam_model_registry["vit_h"](checkpoint=model_path)
sam.to(device)

# 创建预测器
predictor = SamPredictor(sam)

# 加载和预处理图像
image = Image.open("test.png")
image_np = np.array(image)
predictor.set_image(image_np)

# 定义点坐标（假设的点坐标，请替换为实际坐标）
x, y = 100, 100  # 替换为实际的点坐标
input_point = np.array([[x, y]])
input_label = np.array([1])  # 1 表示前景点

# 进行预测
masks, scores, logits = predictor.predict(point_coords=input_point, point_labels=input_label, multimask_output=False)

# 显示结果
plt.figure(figsize=(10, 10))
plt.imshow(image_np)
for mask in masks:
    plt.contour(mask, colors='r', levels=[0.5])
plt.show()