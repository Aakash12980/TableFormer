from turtle import forward
import torch.nn as nn
import torch 
import torchvision.models as models
from typing import List, Dict, Tuple

class TableFormerModel(nn.Module):
    def __init__(self) -> None:
        super(TableFormerModel, self).__init__()

    def forward(self):
        pass
    

    class CNNBackboneNetwork():
        def __init__(self) -> None:
            resnet_modules = list(models.resnet18().modules())[:-2]
            self.resnet = nn.Sequential(
                        *resnet_modules,
                        nn.AdaptiveAvgPool2d((28,28))
                    )

        def forward(self):
            pass


    class StructureDecoder():
        def __init__(self) -> None:
            pass
            
    class CellBBoxDecode():
        def __init__(self) -> None:
            pass
