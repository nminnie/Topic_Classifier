import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from data_cleaning import clean_text

app = Flask(__name__)
model = pickle.load(open('LR_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input_text = [str(value) for value in request.form.values()][0]

    cleaned_text = [clean_text(input_text)]
    
    prediction = model.predict_proba(cleaned_text)[0]
    pred_scores = [round(score * 100, 2) for score in prediction]
    results = dict(zip(model.classes_, pred_scores))
    sorted_results = [(k, v) for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)]
    top_result = sorted_results[0]

    return render_template('index.html', prediction=f'The model is {top_result[1]}% confident that the topic is {top_result[0]}.')


if __name__ == "__main__":
    app.run(debug=True)