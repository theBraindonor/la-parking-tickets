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

from skopt.space import Integer, Real

from sklearn.externals import joblib
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn_pandas import DataFrameMapper

from utility import HyperParameters, Runner
from model import load_data_frame

sample = None
iterations = 24

hyper_parameters = HyperParameters(search_space={
    'xgb__n_estimators': Integer(100, 500),
    'xgb__learning_rate': Real(0.1, 0.3),
    'xgb__gamma': Real(0.0001, 100.0, prior='log-uniform'),
    'xgb__max_depth': Integer(3, 7),
    'xgb__colsample_bytree': Real(0.4, 0.9),
    'xgb__colsample_bylevel': Real(0.4, 0.9),
    'xgb__colsample_bynode': Real(0.4, 0.9)
})

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
    ('xgb', xgb.XGBClassifier(tree_method='hist'))
])


def build_xgboost_model():
    runner = Runner(
        'model/output/xgboost_model',
        load_data_frame(),
        'violation',
        xgboost_pipeline,
        hyper_parameters
    )
    runner.run_classification_search_experiment(
        'neg_log_loss',
        sample=sample,
        n_iter=iterations,
        multiclass=True,
        record_predict_proba=True
    )
    joblib.dump(
        runner.trained_estimator,
        'model/output/xgboost_model.joblib'
    )


if __name__ == '__main__':
    build_xgboost_model()
