import numpy as np; 
import math
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm
from scipy.ndimage import gaussian_filter

def plotter(x,y):
    "Saves a heatmap as jpg"
    temp=[]

    if len(x)<len(y):
        for i in range(len(x)):
            temp.append(y[i])
        y.clear()
        y = temp
    if len(x)>len(y):
        for i in range(len(y)):
            temp.append(y[i])
        x.clear()
        x = temp
    def myplot(x, y, s, bins=600):
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
        heatmap = gaussian_filter(heatmap, sigma=s)

        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        return heatmap.T, extent
    fig, axs = plt.subplots(2, 2)
    sigmas = [0, 16, 32, 64]
    for ax, s in zip(axs.flatten(), sigmas):
        if s == 0:
            ax.plot(x, y, 'k.', markersize=5)
            ax.set_title("Scatter plot")
        else:
            img, extent = myplot(x, y, s)
            ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
            ax.set_title("")
    plt.savefig('heatmap.png')