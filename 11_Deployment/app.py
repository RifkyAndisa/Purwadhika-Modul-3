from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd


app = Flask(__name__)

# Bikin Halaman Home
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    filename = 'logit_final.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)
