import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from plotting import plot_graph
import os

def sigmoid(x):
    return tf.keras.activations.sigmoid(x)

def plot_sigmoid(x, path):
    plot_graph( x, 
                f = sigmoid, 
                title="Sigmoid function", 
                LABEL_Y=r"$\sigma(x) = \frac{1}{1 + e^{-x}}$", 
                LABEL_Y_DASH=r"$\sigma^\prime(x) = \sigma(x)(1-\sigma(x))$", 
                filepath_of_plot=path)

x = np.linspace(-10, 10, 100)
root_plot_dir = "plots"
os.makedirs(root_plot_dir, exist_ok=True)

plot_sigmoid(x, os.path.join(root_plot_dir, "sigmoid"))