from flask import Flask, render_template, flash ,redirect, url_for,request
import matplotlib.pyplot as plt
import pandas
import csv

app = Flask(__name__)

def writeincsv( file, data ):
    '''Takes data that is a list of lists and writes them in the csv file file'''
    f = open( 'GitHub/EmotionalFlask/DataFiles/' + file, 'w' ) #Open file in write mode
    writer = csv.writer( f ) # Create the csv file 

    if len( data ) == 1:
        writer.writerow( data ) # Write one row to csv
    elif len( data ) > 1: 
        writer.writerows( data ) # Write multiple rows to csv

    f.close()
    return f







@app.route("/")
def home():
    return render_template('index.html')



if __name__ =="__main__":
    app.run
    writeincsv( 'test.csv', [['hej'], [1, 2, 3] , [['hej'], 'hej då'] ] )
    # writeincsv( 'test.csv', [1,2,3] )

