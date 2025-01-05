import torch
import numpy as np
x =torch.rand(size=(10,))
print(x)
print(torch.topk(x,k=2))