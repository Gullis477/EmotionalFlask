import os
from flask import Flask, render_template, flash ,redirect, url_for,request,send_from_directory, send_file
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename




import os
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, send_file
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from turbo_flask import Turbo
import handelCSV
import time
import threading

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
    items = os.listdir(r'uploads')
    output = (items if items else 'Nothing to download :(' )
    choice= request.args.get('datafile','')
    if choice:
        send_file(choice,as_attachment=True)
    return render_template('download.html',output = output)

@app.route('/download/get/<thing>')
def something_file(thing):
    path="uploads/"+thing
    return send_file(path, as_attachment= True)

if __name__ == '__main__':  
    app.run(debug = True)  #Om man ändrar och sparar när servern är igång startar den om automatiskt



# TURBO
def update_load():
    with app.app_context(): #Fattar inte vad app_context() är
        while True:
            time.sleep(2)
            turbo.push(turbo.replace(render_template('turbo_template.html'), 'load')) #Tror att denna raden uppdaterar elementet med id 'load' i templated loadavg.html

@app.before_first_request #Denna tag gör så att funktionen körs innan den första "requesten". Koden i funktionen hade kunnat köras innan "run" i huvudprogrammet
def before_first_request():
    threading.Thread(target=update_load).start() #startar en till tråd kör update_load

@app.context_processor #Taggen gör att alla templates kan använda variablerna (nycklarna i return-dictionaryn) dvs load i detta fallet.
def inject_load():
    inputFile = 'CSVFILE.csv'
    f1 = open(inputFile, "r")
    last_line = f1.readlines()[-1]
    f1.close()
    return {'load':last_line }
# ------------------------------------------------------------------------------
# Run code

if __name__ == '__main__':
    app.run(debug=True)  # Om man ändrar och sparar när servern är igång startar den om automatiskt


# ------------------------------------------------------------------------------

# $env:FLASK_APP = "hello"
# $ flask run
