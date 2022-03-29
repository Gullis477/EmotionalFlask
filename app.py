import os
from flask import Flask, render_template, flash ,redirect, url_for,request,send_from_directory, send_file
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename


#UPLOAD_FOLDER = 'EmotionalFlask\uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads'


#vanliga funktioner
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

# Sending the file to the user
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
    app.run(debug = True)  






