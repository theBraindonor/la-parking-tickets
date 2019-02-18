#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with several XGBoost Models
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
from model import ordinal_data_mapper

sample = 10000
iterations = 2

hyper_parameters = HyperParameters(search_space={
    'xgb__n_estimators': Integer(50, 500),
    'xgb__learning_rate': Real(0.1, 0.3),
    'xgb__gamma': Real(0.0001, 100.0, prior='log-uniform'),
    'xgb__max_depth': Integer(3, 7),
    'xgb__colsample_bytree': Real(0.4, 0.8),
    'xgb__colsample_bylevel': Real(0.4, 0.8),
    'xgb__colsample_bynode': Real(0.4, 0.8)
})

ordinal_unbalanced_pipeline = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('xgb', xgb.XGBClassifier(tree_method='hist'))
])


def test_ordinal_unbalanced_model():
    runner = Runner(
        'model/experiment/output/xgboost_ordinal_unbalanced',
        'data_scratch/sampled_citations.csv',
        'violation',
        ordinal_unbalanced_pipeline,
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
    test_ordinal_unbalanced_model()
