#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with several a basic LightGBM Model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0.0"

import lightgbm as lgb

from skopt.space import Integer, Real

from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = None
iterations = 24

hyper_parameters = HyperParameters(search_space={
    'lgb__n_estimators': Integer(50, 500),
    'lgb__learning_rate': Real(0.001, 0.05),
    'lgb__num_leaves': Integer(7, 63),
    'lgb__max_bin': Integer(32, 256),
    'lgb__min_child_samples': Integer(10, 50),
    'lgb__subsample': Real(0.5, 0.9),
    'lgb__colsample_bytree': Real(0.5, 0.9)
})

lightgbm_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('lgb', lgb.LGBMClassifier())
])


def test_lightgbm_basic():
    runner = Runner(
        'model/experiment/output/lightgbm_basic',
        load_sample_data_frame(),
        'violation',
        lightgbm_basic,
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
    test_lightgbm_basic()
