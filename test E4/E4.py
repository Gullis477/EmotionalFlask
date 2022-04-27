import pandas as pd
from pandas import read_csv

import numpy as np

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import *

import matplotlib.animation as animation 

import ipywidgets as widgets
from ipywidgets import interact 



# Import CSV as dfs:
mapp=  "csvfiles/E4.try/"
bvp=   pd.DataFrame( read_csv( mapp + "BVP.csv" ) )     #
eda=   pd.DataFrame( read_csv( mapp + "EDA.csv" ) )     #
hr=    pd.DataFrame( read_csv( mapp + "HR.csv" ) )      # r2 = sample rate in Hz
ibi=   pd.DataFrame( read_csv( mapp + "IBI.csv" ) )     # col1 = time, col2 = durations in sec
temp=  pd.DataFrame( read_csv( mapp + "TEMP.csv" ) )    # 



# Graphs 
def graph_bvp( bvp=bvp ):
    # header = str( 16443467447.0000 )
    x = [ i for i in range( len( bvp[2:] ) ) ]
    y = bvp[ 2: ]
    y.columns = [ 'bvp' ] # assign headers
    # print( y )

    y.divide( 400, fill_value=0 )

    print( y )


    data_linreg = np.polyfit( x, y, 1 )
    xp = np.linspace( 5, 33000, 3000)
    pr = np.polyval( data_linreg, xp)

    fig = plt.figure( figsize=( 9, 5 ) )
    ax = fig.add_subplot()
    ax.grid()
    ax.set_xlabel( "Timestamp" )
    ax.set_ylabel( "BVP" )
    ax.set_title( " BVP Measure" )

    ax.scatter( x, y, color='lightgray', s=1 )
    ax.plot( xp, pr )
    plt.show()


graph_bvp()


