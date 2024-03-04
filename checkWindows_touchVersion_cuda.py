# 下载对应版本：https://pytorch.org/
# windows CUDA 12.1
#     pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# windows CUDA 11.8
#     pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

import torch
print(torch.__version__)
print(torch.cuda.is_available())