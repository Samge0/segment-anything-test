## segment-anything-test

[segment-anything](https://github.com/facebookresearch/segment-anything)的测试demo

### 下载模型:
```shell
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth checkpoints/sam_vit_h_4b8939.pth
```


### 环境配置
- 【推荐】使用vscode的`Dev Containers`模式，参考[.devcontainer/README.md](.devcontainer/README.md)

- 【可选】其他虚拟环境方式
    - 【二选一】安装torch-cpu版
        ```shell
        pip install torch torchvision
        ```
    - 【二选一】安装torch-cuda版
        ```shell
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
        ```
    - 【必要】安装依赖
        ```shell
        pip install -r requirements.txt
        ```

### 推理
- 推理glm4v-9b-chat:
  ```shell
  # 30GB GPU memory
  CUDA_VISIBLE_DEVICES=0,1 swift infer --model_type glm4v-9b-chat
  ```