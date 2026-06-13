import torch
from torch import nn
import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt 
#import requests
#from pathlib import Path

train_data = datasets.FashionMNIST(
    root = 'data',
    download= True,
    transform=ToTensor(),
    target_transform=None
)
test_data = datasets.FashionMNIST(
    root='data',
    download=True,
    transform=ToTensor(),
    target_transform=None
)

image,label = train_data[0]
#print(len(train_data.data) ,len(train_data.targets) , len(test_data.data) , len(test_data.targets) )

#see classes
class_names = train_data.classes
#print(class_names)

#data loader
from torch.utils.data import DataLoader
batch_size = 32
train_dataloader = DataLoader(train_data,
    batch_size=batch_size,
    shuffle=True
)

test_dataloader = DataLoader(test_data,
    batch_size=batch_size,
    shuffle=True
)
#print(len(test_dataloader), len(train_dataloader))

train_features_batch , train_labels_batch = next(iter(train_dataloader))

#print(train_features_batch.shape)
##for epoch in range(epochs):
    #train_step(data_loader= train_dataloader,
       # model= model_1,
        #loss_fn= loss_fn,
       # optimizer= optimizer,
        #accuracy_fn= accuracy_fn,)
    #test_step(data_loader= train_dataloader,
       # model= model_1,
       # loss_fn= loss_fn,
        #accuracy_fn= accuracy_fn,)


