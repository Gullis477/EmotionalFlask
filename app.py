
import os
import re
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file
import matplotlib.pyplot as plt
from numpy import result_type
from werkzeug.utils import secure_filename
import pandas as pd

from turbo_flask import Turbo #app
import time
import threading
import random
#import classification
import pickle
from Eyetracker import GazepointAPI
from flask_moment import Moment
from datetime import datetime

# initialization
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads'
app.config['DOWNLOAD_FOLDER'] = r'downloads'
# app.config['MAX_CONTENT_PATH']
turbo = Turbo(app)


# ------------------------------------------------------------------------------

#app funktioner



def byte_units(value, units=-1):
    UNITS=('Bytes', 'KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB')
    i=1
    value /= 1000.0
    while value > 1000 and (units == -1 or i < units) and i+1 < len(UNITS):
        value /= 1000.0
        i += 1
    return f'{round(value,3):.3f} {UNITS[i]}'

app.jinja_env.filters.update(byte_units = byte_units)
moment = Moment(app)

#########################
try:
    os.makedirs(app.config['DOWNLOAD_FOLDER'])
except:
    pass

def get_files(target):
    for file in os.listdir(target):
        path = os.path.join(target, file)
        if os.path.isfile(path):
            yield (
                file,
                datetime.utcfromtimestamp(os.path.getmtime(path)),
                os.path.getsize(path)
            )




@app.route('/download')
def display_download():
    # path = 'uploads'
    # list_of_files = os.listdir(path)
    
    files = get_files(app.config['DOWNLOAD_FOLDER'])

    return render_template('download.html', **locals())


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(
        app.config['DOWNLOAD_FOLDER'],
        filename,
        as_attachment=True
    )
    
    
##############################
    

#false
# test_eyetracker = True
# def getTracker():
#     return test_eyetracker

# def setTracker(value):
#     test_eyetracker=value




@app.route("/",methods=['GET', 'POST'])
def home():
        i = 0
        if (request.method == 'POST'):
            if (request.form.get('Start') == 'Start'):
                run_tracker = False
                while (GazepointAPI.run() == False):
                    print ("Tracking....Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...Tracking...")
                
            elif (request.form.get('Stop') == 'Stop'):
                GazepointAPI.calibrate()
              
      
        return render_template('index.html')

@app.route("/simulation")
def simulation():
    # file = pd.read_csv("hrtestdata.csv")
    return render_template('simulation.html')

@app.route('/upload', methods=['GET', 'POST'])  
def upload():  
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')

# @app.route('/download/<thing>')   outdated
# def something_file(thing):
#     path="uploads/"+thing
#     return send_file(path, as_attachment= True)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.before_first_request #Denna tag g??r s?? att funktionen k??rs innan den f??rsta "requesten". Koden i funktionen hade kunnat k??ras innan "run" i huvudprogrammet
def before_first_request():
    threading.Thread(target=update_load).start() #startar en till tr??d k??r update_load
    threading.Thread(target=update_eye).start()

@app.context_processor
def inject_load():
    df = pd.read_csv('csvfiles/SAM_arousal.csv')
    a_sample = df.sample()
    tmep = a_sample[a_sample.columns[1:53]]
    last_line = tmep.iloc[[0]]
    loaded_arousal_model = pickle.load(open('test_arousal_algoritm.sav', 'rb'))
    loaded_valence_model = pickle.load(open('test_valence_algoritm.sav', 'rb'))
    predicted_arousal = loaded_arousal_model.predict(last_line)
    predicted_valence = loaded_valence_model.predict(last_line)
    coffe = ''
    if predicted_arousal == 1 and predicted_valence == 1:
        face = "\U0001F603"

    elif predicted_arousal == 1 and predicted_valence == 0:
        face = "\U0001F92F"
        coffe = u"\u2615"

    elif predicted_arousal == 0 and predicted_valence == 0:
        face = "\U0001F62D"

    elif predicted_arousal == 0 and predicted_valence == 1:
        face = "\U0001F60C"
    
    with  open('tracking_results', 'r') as f:
        data = f.read().replace('[','')
        
    if(len(data)==0):   
        test_eyetracker = False 
        pic = " "
    else:
        pic = "\U0001F6A8"
    eye = data


    return {'load_emotion':face,'load_break': coffe,'load_eye' : eye, 'symbol' : pic}

# TURBO
def update_load():
    with app.app_context(): #app_context()
        while True:
            time.sleep(20)
            turbo.push(turbo.replace(render_template('turbo_template.html'), 'load')) #Tror att denna raden uppdaterar elementet med id 'load' i templated loadavg.html

def update_eye():
    with app.app_context(): #app_context()
        while True:
            time.sleep(10)
            turbo.push(turbo.replace(render_template('eye_template.html'), 'eyes')) #Tror att denna raden uppdaterar elementet med id 'load' i templated loadavg.html


# ------------------------------------------------------------------------------
# Run code

if __name__ == '__main__':
    app.run(debug=True)  # Om man ??ndrar och sparar n??r servern ??r ig??ng startar den om automatiskt


# ------------------------------------------------------------------------------

# $env:FLASK_APP = "hello"
# $ flask run
