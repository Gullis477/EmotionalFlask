# Load libraries 

from pandas import read_csv

# Slå ihop foldern till en csv fil eller dataframe

# ==============================================================================================
# Gather CSVs, ignores tags and acc

mapp = "csvfiles/e4/test"

# Data from temperature sensor, expressed degrees in celsius
temp = read_csv( mapp + "TEMP.csv")

# Data from Electrodermal activity sensor, expressed in microsiemens
eda = read_csv( mapp + "EDA.csv" )

# Data from photoplethysmograph
bvp = read_csv( mapp + "BVP.csv" )

#Data from 3-axis accelometor is not relevant 

# Time between individuals heartbeats extrakted from BVP signal 
# col1 = time , col2 = duration in seconds
ibi = read_csv( mapp + "IBI.csv" )

# Avg heartrate extracted from BVP signal 
# r1 = initial time of session , r2 = sample rate, expressed in Hz
hr = read_csv( mapp + "HR.csv" )

# Data from tags is not relevant atm 

# combine all in one df:
if 


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

