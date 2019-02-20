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

from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

# Takes about 15 minutes per iteration at a 20% sample rate.
sample = None
iterations = 2

hyper_parameters = HyperParameters(search_space={
    'xgb__n_estimators': Integer(100, 500),
    'xgb__learning_rate': Real(0.1, 0.3),
    'xgb__gamma': Real(0.0001, 100.0, prior='log-uniform'),
    'xgb__max_depth': Integer(3, 7),
    'xgb__colsample_bytree': Real(0.4, 0.8),
    'xgb__colsample_bylevel': Real(0.4, 0.8),
    'xgb__colsample_bynode': Real(0.4, 0.8)
})

xgboost_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('xgb', xgb.XGBClassifier(tree_method='hist'))
])


def test_xgboost_basic():
    runner = Runner(
        'model/experiment/output/xgboost_basic',
        load_sample_data_frame(),
        'violation',
        xgboost_basic,
        hyper_parameters
    )
    runner.run_classification_search_experiment(
        'neg_log_loss',
        sample=sample,
        n_iter=iterations,
        multiclass=True,
        record_predict_proba=True
    )


if __name__ == '__main__':
    test_xgboost_basic()
