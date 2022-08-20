import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('dt_model.sav', 'rb'))

def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1, 14)
	loaded_model = pickle.load(open("dt_model.sav", "rb"))
	result = loaded_model.predict(to_predict)
	return result[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods = ['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    features_list = [np.array(int_features)]
    prediction = model.predict(features_list)

    print(features_list)
    print("Prediction Value : ",prediction)

    result = ""
    if prediction == 1:
        result = "Income is more than 50k "
    elif prediction == 0:
        result = "Income is less than 50K"

    return render_template('home.html', prediction_text=result)


if __name__ == '__main__':
    app.run(debug=True)

