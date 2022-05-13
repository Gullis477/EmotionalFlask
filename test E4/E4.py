import pandas as pd
from pandas import read_csv

import numpy as np

import math

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import *

import matplotlib.animation as animation 

import ipywidgets as widgets
from ipywidgets import interact 
# ------------------------------------------------------------------------------------------------
# Import CSV as a single dataframe

mapp =  "csvfiles/E4.try/"
bvp =   pd.DataFrame( read_csv( mapp + "BVP.csv" ) )     #
eda =   pd.DataFrame( read_csv( mapp + "EDA.csv" ) )     #
hr =    pd.DataFrame( read_csv( mapp + "HR.csv" ) )      # r2 = sample rate in Hz
ibi =   pd.DataFrame( read_csv( mapp + "IBI.csv" ) )     # col1 = time, col2 = durations in sec
temp =  pd.DataFrame( read_csv( mapp + "TEMP.csv" ) )    # 

bvp.columns =   { 'BVP' }
ibi.columns =   { 'time', 'IBI' }
eda.columns = { 'EDA' }

frames = [ bvp, eda, hr, ibi, temp ]
dataFrame = pd.concat( frames, axis=0, join="outer", keys=None )
print( dataFrame )

# ------------------------------------------------------------------------------------------------
# Graphs 

def all_e4( df=dataFrame ):

    bvp_x = [ i for i in range( len( df[2:] ) ) ]
    bvp_y = df[ 'BVP' ][ 2: ]

    ibi_x = df[ 'time' ]
    ibi_y = df[ 'IBI' ]

    eda_x = [ i for i in range( len( df[ 'EDA' ][2:] ) ) ]
    eda_y = df[ 'EDA' ][ 2: ]

    hr_x = [ 1, 2, 3, 4 ]
    hr_y = [ 1, 2, 3, 4 ]

    temp_x=[1, 2, 3]
    temp_y=[1, 2, 3]

    fig, ax = plt.subplots( 2, 3 )

    ax[ 0, 0 ].plot( bvp_x, bvp_y, label='BVP' )
    ax[ 0, 0 ].set_title( "BVP" )

    ax[ 0, 1 ].plot( ibi_x, ibi_y, label='IBI' )
    ax[ 0, 1].set_title( "IBI" )

    ax[ 1, 0 ].plot( eda_x, eda_y, label='EDA' )
    ax[ 1, 0 ].set_title( "EDA" )

    ax[ 1, 1 ].plot( hr_x, hr_y, label='HR' )
    ax[ 1, 1 ].set_title( "HR")

    ax[ 1, 2 ].plot( temp_x, temp_y, label='Temperature' )
    ax[ 1, 2] .set_title( "Temperature" )
    
    plt.savefig( "static/static_e4.jpg" )
    plt.savefig( "downloads/e4.jpg")

    plt.show()

all_e4()
# all_in_one()

# ------------------------------------------------------------------------------------------------

# def graph_bvp_ibi( bvp=bvp, ibi=ibi ):
#     '''Should also contain HR'''
    
#     bvp_x = [ i for i in range( len( bvp[2:] ) ) ]
#     bvp_y = bvp[ 'BVP' ][ 2: ]

#     ibi_x = ibi[ 'time' ]
#     ibi_y = ibi[ 'IBI' ]


#     fig, ibi_ax = plt.subplots()
#     color_ibi = 'tab:blue'

#     ibi_ax.set_xlabel( 'time' )
#     ibi_ax.set_ylabel( 'IBI' )
#     ibi_ax.plot( ibi_x, ibi_y, color=color_ibi )
#     ibi_ax.tick_params( axis='y', labelcolor=color_ibi )

#     bvp_ax = ibi_ax.twinx() #allows second ax
#     color_bvp = 'tab:red'
#     bvp_ax.set_ylabel( 'BVP', color=color_bvp )
#     bvp_ax.grid()
#     bvp_ax.plot( bvp_x, bvp_y, color=color_bvp )
    
#     bvp_ax.tick_params( axis='y', labelcolor=color_bvp )

#     fig.tight_layout()
#     plt.show()



# def graph_eda( eda=eda ):
#     eda_x = [ i for i in range( len( eda[ 'EDA' ][2:] ) ) ]
#     eda_y = eda[ 'EDA' ][ 2: ]

#     fig, eda_ax = plt.subplots()
#     color_eda="tab:green"
#     eda_ax.set_ylabel( "EDA" )
#     eda_ax.grid()
#     eda_ax.plot( eda_x, eda_y, color=color_eda )
#     plt.show()



