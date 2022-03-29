from flask import Flask, render_template, flash ,redirect, url_for,request
import matplotlib.pyplot as plt





app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')



