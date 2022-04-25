import pandas as pd
from pandas import read_csv

import numpy as np

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import *

import matplotlib.animation as animation 

import ipywidgets as widgets
from ipywidgets import interact 



# Import CSV as dfs:
mapp =  "csvfiles/E4.try/"
bvp =   pd.DataFrame( read_csv( mapp + "BVP.csv" ) )     #
eda =   pd.DataFrame( read_csv( mapp + "EDA.csv" ) )     #
hr =    pd.DataFrame( read_csv( mapp + "HR.csv" ) )      # r2 = sample rate in Hz
ibi =   pd.DataFrame( read_csv( mapp + "IBI.csv" ) )     # col1 = time, col2 = durations in sec
temp =  pd.DataFrame( read_csv( mapp + "TEMP.csv" ) )    # 

bvp.columns =   { 'BVP' }
bvp = bvp.iloc[ ::100, : ]
ibi.columns =   { 'time', 'IBI' }


# Graphs 
def graph_bvp_ibi( bvp=bvp, ibi=ibi ):
    
    bvp_x = [ i for i in range( len( bvp[2:] ) ) ]
    bvp_y = bvp[ 'BVP' ][2:]

    ibi_x = ibi[ 'time' ]
    ibi_y = ibi[ 'IBI' ]


    fig, ibi_ax = plt.subplots()
    color_ibi = 'tab:blue'
    ibi_ax.set_xlabel( 'time' )
    ibi_ax.set_ylabel( 'IBI' )
    ibi_ax.plot( ibi_x, ibi_y, color=color_ibi )
    ibi_ax.tick_params( axis='y', labelcolor=color_ibi)

    bvp_ax = ibi_ax.twinx() #allows second ax
    color_bvp = 'tab:red'
    bvp_ax.set_ylabel( 'BVP', color=color_bvp )
    bvp_ax.plot( bvp_x, bvp_y, color=color_bvp )
    bvp_ax.tick_params( axis='y', labelcolor=color_bvp )

    fig.tight_layout()
    plt.show()
    # fig = plt.figure( figsize=( 9, 5 ) )
    # ax = fig.add_subplot()
    # ax.grid()
    # ax.set_xlabel( "Timestamp" )
    # ax.set_ylabel( "BVP" )
    # ax.set_title( "BVP Measure" )

    # ax.plot( bvp_x, bvp_y, color='lightgray', s=1 )
    # plt.show()


graph_bvp_ibi()


