# python helper functions for plotting graphs -
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
plt.style.use('fivethirtyeight')


def derivative(f, x, delta_x=1e-6):
    return (f(x + delta_x) - f(x))/(delta_x)

def plot_graph(x, f,
               ALPHA=0.6, 
               label_x = r"$x \rightarrow$", label_y=r"$act(x), act'(x) \rightarrow$", 
               title=None,
               LABEL_Y=None,
               LABEL_Y_DASH=None,
               filepath_of_plot="plot.png"):
    y = f(x)
    y_dash = derivative(f, x)
    plt.figure(figsize=(10,8))
    plt.axhline(y=0, color="black", linestyle="--", lw=2)
    plt.axvline(x=0, color="black", linestyle="--", lw=2)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)

    if (LABEL_Y != None) and (LABEL_Y_DASH != None):
        plt.plot(x, y, alpha=ALPHA, label=LABEL_Y)
        plt.plot(x, y_dash, alpha=ALPHA, label=LABEL_Y_DASH)
        plt.legend(fontsize=14)

    else:
        plt.plot(x, y, alpha=ALPHA)
        plt.plot(x, y_dash, alpha=ALPHA)

    if os.path.isfile(filepath_of_plot):
        os.remove(filepath_of_plot) 
        
    plt.savefig(filepath_of_plot)
      
