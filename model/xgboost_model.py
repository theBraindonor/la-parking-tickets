#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with a basic XGBoost Model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

import xgboost as xgb

from sklearn.externals import joblib
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn_pandas import DataFrameMapper

from utility import Runner
from model import load_data_frame

sample = None

mapper = DataFrameMapper([
    (['month'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['weekday'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['hour'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['make'], [SimpleImputer(strategy="constant", fill_value=0), MinMaxScaler()]),
    (['color'], [SimpleImputer(strategy="constant", fill_value=0), MinMaxScaler()]),
    (['latitude'], [SimpleImputer(strategy='median'), StandardScaler()]),
    (['longitude'], [SimpleImputer(strategy='median'), StandardScaler()])
])

xgboost_pipeline = Pipeline([
    ('mapper', mapper),
    ('xgb', xgb.XGBClassifier(
        tree_method='hist',
        colsample_bylevel=0.8,
        colsample_bynode=0.4,
        colsample_bytree=0.8,
        gamma=0.02092258872266934,
        learning_rate=0.3,
        max_depth=7,
        n_estimators=500,
        n_jobs=-1
    ))
])


def build_xgboost_model():
    runner = Runner(
        'model/output/xgboost_model',
        load_data_frame(),
        'violation',
        xgboost_pipeline,
        None
    )
    runner.run_classification_experiment(
        sample=sample,
        test_size=0.2,
        multiclass=True,
        record_predict_proba=True
    )
    joblib.dump(
        xgboost_pipeline,
        'model/output/xgboost_model.joblib'
    )


if __name__ == '__main__':
    build_xgboost_model()

