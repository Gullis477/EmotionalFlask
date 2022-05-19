from doctest import IGNORE_EXCEPTION_DETAIL
import socket
import time
import numpy as np; 
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.cm as cm
from scipy.ndimage import gaussian_filter

def calibrate():
    "Calibration of the eye tracker, should be called first time the software is used"
    HOST = '127.0.0.1'
    # Gazepoint Port
    PORT = 4242
    ADDRESS = (HOST, PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ADDRESS)
        s.send(str.encode('<SET ID="CALIBRATE_SHOW" STATE="1" />\r\n'))
    except ConnectionRefusedError as e:print ("ERROR:Unable to connect to ADRESS")
    
def sort_data(data):
    "String to lists of x and y coordinates"
    povx = []
    povy = []
    invalid = 0
    for temp in data:
        if "FPOGX" in temp:
            if ((temp[7] == "0") and (temp[13] != "0")):
                    povx.append(temp[7:14])
            else:
                 invalid = invalid +1
        elif "FPOGY" in temp:
            if ((temp[7] == "0") and (temp[13] != "0")):
                povy.append(temp[7:14])
    return povx,povy

def fixated_eyes(x,y):
    "Check for eye fixation"
    #Max amount of similar datapoints: 1200
    counter = 0
    fix_pos=[]
    for i in range(len(x)-1):
        if (x[i][4:5] == x[i+1][4:5]):
            counter = counter + 1
    for i in range(len(y)-1):
        if (y[i][4:5] == y[i+1][4:5]):
            counter = counter + 1
            fix_pos.append(y[i])

    y_temp = [float(y_cord) for y_cord in fix_pos]  

    summ = sum(y_temp)
    length = float(len(fix_pos))
    pos = summ/length
    return counter,pos

###########################################################################   
# Host machine IP
def collect_data():
    "Data collector, runs until 600 datapoints are collected(10 sec if all datapoints are valid)"
    HOST = '127.0.0.1'
    # Gazepoint Port
    PORT = 4242
    ADDRESS = (HOST, PORT)
    stri = " "
    povx=[]
    povy=[]
    try:
        HOST = '127.0.0.1'
    # Gazepoint Port
        PORT = 4242
        ADDRESS = (HOST, PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ADDRESS)
        s.send(str.encode('<SET ID="ENABLE_SEND_CURSOR" STATE="1" />\r\n')) # Start or stop the streaming of data from the server to client.
        s.send(str.encode('<SET ID="ENABLE_SEND_POG_FIX" STATE="1" />\r\n')) #Enable a data record variable in the data record string (described in Section 5 below).
        s.send(str.encode('<SET ID="ENABLE_SEND_DATA" STATE="1" />\r\n'))
        #(0,0) is top left, (0.5,0.5) is the screen center, and (1.0,1.0) is bottom right.
        #FPOGS = start time
        #FPOGD = Duration time
        #FPOGID = POG ID
        #FPOGV = 1 if valid, 0 if not
        #len(str)=133 per dataset

       
       

        while 79800 > len(stri): #Runs for approx 10 sec and collects 600 x and y coordinates
            rxdat = s.recv(1024)   
            if "ENABLE" not in bytes.decode(rxdat):
                stri = stri + bytes.decode(rxdat) 
                
        lst = stri.split()
        povx,povy = sort_data(lst)
        num,pos = fixated_eyes(povx,povy)
        if  num > 100: # should be 500
            print ("Fixated eyes detected!")  
            lines = 54 # This is the total number of lines that can be seen in the window
            row = pos*lines 
            return povx,povy, True, int(row)
        s.close()
    
    except ConnectionRefusedError as e:print ("ERROR:Unable to connect to ADRESS")
    return povx,povy,False


##########################################################################################
################################ Main function ##########################################
##########################################################################################
def run(): 
    "Main function to call"
    
    x_pos,y_pos,fixation,row = collect_data()
  
    temp = []
    
    if len(x_pos)<len(y_pos):
        for i in range(len(x_pos)):
            temp.append(y_pos[i])
        y_pos.clear()
        y_pos = temp
    if len(x_pos)>len(y_pos):
        for i in range(len(y_pos)):
            temp.append(y_pos[i])
        x_pos.clear()
        x_pos = temp
    x = [float(x_cord) for x_cord in x_pos]   
    y = [float(y_cord) for y_cord in y_pos]   
    sns.jointplot(x=x, y=y, kind='hex',marginal_kws=dict(bins=20, fill=False))
    plt.savefig('static/heatmap')
    if (fixation == True):
        #Create a text file
        status = (" It appears that you have gotten stuck at approx"+ " " + str(row)+":lines from the top")
        f = open('tracking_results','a')
        f.truncate(0)
        f.write(status)
        f.close()
        return True
    else:
        return False
      
run()
    #plotter(x_pos,y_pos)

