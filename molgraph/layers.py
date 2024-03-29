# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/layers.ipynb.

# %% auto 0
__all__ = ['feed_forward', 'MessageGCN', 'UpdateGCN']

# %% ../notebooks/layers.ipynb 4
import torch
from torch import nn
from fastai.data.core import DataLoader, DataLoaders, Datasets
from fastcore.foundation import *
from fastcore.basics import *
from fastai.torch_core import Module


# %% ../notebooks/layers.ipynb 5
def feed_forward(input_dim:int, hidden_dim:int=100, num_layers:int=2, output_dim:int=1, dropout=0.1, activation=nn.ReLU):
    """Simple function to generate a feed forward neural network with ´num_layers´, ´hidden_dim´ hidden units and ´output_dim´ output units. Default activation function is reLu."""
    dims = [input_dim] + [hidden_dim] * num_layers
    layers = []
    for i in range(num_layers):      
        layers.append(nn.Linear(dims[i], dims[i + 1]))
        layers.append(nn.Dropout(dropout))
        layers.append(activation())      
    layers.append(nn.Linear(hidden_dim, output_dim))
    return nn.Sequential(*layers)

# %% ../notebooks/layers.ipynb 7
class MessageGCN(Module):
    
    """
    
    Message function from Graph convolutional network as described by Kipf & Welling (https://arxiv.org/pdf/1609.02907.pdf) and refactored as MPNN formalism.

       
    """
    
    def __init__(self, n_node_features:int, hidden_units:int=100, num_layers:int=2, output_units:int=1, dropout:float=0.15):
        
        """
        
        Arguments:
        
        n_node_features : int
            Number of features of each atom
            
        hidden_units : int (default = 100)
            Number of hidden units in `self.gcn`
            
        num_layers : int (default = 2)
            Number of hidden layers 
            
        output_units : int (default = 1)
            Number of output units of the last layer
                                 
        dropout : float (default = 0.15)
            Amount of dropout regularization
        
        
        """
        
        self.message_function = feed_forward(n_node_features, hidden_units, num_layers, output_units, dropout)
        
    
    def forward(self,x):
        node_features, adjacency_matrix, degree_matrix = x
        message = self.message_function(degree_matrix@adjacency_matrix@degree_matrix@node_features)
        return (message, adjacency_matrix, degree_matrix)

# %% ../notebooks/layers.ipynb 9
class UpdateGCN(Module):
    
    """
    
    Vertex update function from Graph convolutional network as described by Kipf & Welling (https://arxiv.org/pdf/1609.02907.pdf) and refactored as MPNN formalism.

       
    """
    
    def __init__(self,  n_updated_features:int, hidden_units:int=100, num_layers:int=2, output_units:int=1, dropout:float=0.15):
        
        """
        
        Arguments:
        
        n_node_features : int
            Number of features of each atom
            
        hidden_units : int (default = 100)
            Number of hidden units in `self.gcn`
            
        num_layers : int (default = 2)
            Number of hidden layers 
            
        output_units : int (default = 1)
            Number of output units of the last layer
                                 
        dropout : float (default = 0.15)
            Amount of dropout regularization
        
        """
        
        self.update_function = feed_forward(n_updated_features, hidden_units, num_layers, output_units, dropout)
    
    def forward(self, message):
        node_state = self.update_function(torch.mean(message, 1))
        return node_state
