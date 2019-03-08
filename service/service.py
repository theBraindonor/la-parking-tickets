#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Serve the ticket model on port 8080
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

import pandas as pd

from flask import Flask, jsonify, request

from sklearn.externals import joblib

from utility import use_project_path

app = Flask(__name__)

model = None


@app.route('/ticketPrediction', methods=['POST'])
def ticket_prediction():
    input_df = pd.DataFrame(request.json, index=[0])
    prediction = model.predict_proba(input_df)
    return jsonify(prediction[0].tolist())
    pass


if __name__ == '__main__':
    use_project_path()
    model = joblib.load('model/output/xgboost_model.joblib')
    app.run(port=8080)
