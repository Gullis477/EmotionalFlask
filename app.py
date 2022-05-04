
import os
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file
import matplotlib.pyplot as plt
from numpy import result_type
from werkzeug.utils import secure_filename
import pandas as pd

from turbo_flask import Turbo #app
import time
import threading
import random
import classification
import pickle

# initialization
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads'
turbo = Turbo(app)

# ------------------------------------------------------------------------------

#app funktioner

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/simulation")
def simulation():
    return render_template('simulation.html')


@app.route('/upload', methods=['GET', 'POST'])  
def upload():  
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')


@app.route('/download')
def display_download():
    path = 'uploads'
    list_of_files = os.listdir(path)
    return render_template('download.html', list_of_files=list_of_files)


@app.route('/download/<thing>')
def something_file(thing):
    path="uploads/"+thing
    return send_file(path, as_attachment= True)



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


@app.before_first_request #Denna tag gör så att funktionen körs innan den första "requesten". Koden i funktionen hade kunnat köras innan "run" i huvudprogrammet
def before_first_request():
    threading.Thread(target=update_load).start() #startar en till tråd kör update_load



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
    return {'load_data': last_line,'load_emotion':[predicted_arousal[0],predicted_valence[0]]}

# TURBO
def update_load():
    with app.app_context(): #Fattar inte vad app_context() är
        while True:
            time.sleep(2)
            turbo.push(turbo.replace(render_template('turbo_template.html'), 'load')) #Tror att denna raden uppdaterar elementet med id 'load' i templated loadavg.html


# ------------------------------------------------------------------------------
# Run code

if __name__ == '__main__':
    app.run(debug=True)  # Om man ändrar och sparar när servern är igång startar den om automatiskt


# ------------------------------------------------------------------------------

# $env:FLASK_APP = "hello"
# $ flask run
