# System imports
import os 
import sys 

# Data science
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Ellipse
import seaborn as sns

# Signal processing 


# misc 
import warnings
import csv

# ------------------------------------------------------------------------------
# Style settings 
sns.set( style='whitegrid', rc={'axes.facecolor' : '#EFF2F7' } )

# Sample freq for ECG sensor
settings = {}
settings[ 'fs' ] = 500

# Load data
df = pd.read_csv( 'data.csv', sep=',' )

plt.figure( figsize=( 20, 7 ) )
start = 0 
stop = 11
fs = 100.0 
duration = (stop-start) / fs

plt.title( "signals %-1f seconds" % duration )
plt.plot( df[start:stop].index, df[start:stop].hr, color = 'red' )

plt.xlabel( "Time", fontsize = 16 )
plt.ylabel( "Amp" )
plt.show()