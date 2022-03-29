from flask import Flask, render_template, flash ,redirect, url_for,request
import matplotlib.pyplot as plt
import pandas
import csv

 
def writecsvrow( file, data ):
    f = open( 'Datafiles/' + file, 'w' ) #Open file in write mode
    writer = csv.writer( f ) # Create the csv file 

    if len( data ) == 1:
        writer.writerow( data ) # Write one row to csv
    elif len( data ) > 1: 
        writer.writerows( data) # Write multiple rows to csv
    f.close()
    return f



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')



