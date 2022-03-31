# ------------------------------------------------------------------------------


import os
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

import handelCSV

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads'


# ------------------------------------------------------------------------------
# app functions


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
    list_of_files = list_of_files = os.listdir(path)
    return render_template('download.html', list_of_files=list_of_files)


@app.route('/download/<thing>')
def something_file(thing):
    path = "uploads/" + thing
    return send_file(path, as_attachment=True)


# ------------------------------------------------------------------------------
# Run code

if __name__ == '__main__':
    app.run(debug=True)  # Om man ändrar och sparar när servern är igång startar den om automatiskt


# ------------------------------------------------------------------------------

# $env:FLASK_APP = "hello"
# $ flask run
