#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with a basic gradient boosting model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

from skopt.space import Integer, Real

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = None
iterations = 24

hyper_parameters = HyperParameters({
    'gb__learning_rate': Real(0.001, 0.1),
    'gb__n_estimators': Integer(50, 500),
    'gb__subsample': Real(0.5, 1),
    'gb__max_depth': Integer(3, 7),
    'gb__min_samples_leaf': Real(0.00001, 0.01),
    'gb__min_samples_split': Real(0.00002, 0.02)
})

gradient_boosting_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('gb', GradientBoostingClassifier())
])


def test_gradient_boosting_basic():
    runner = Runner(
        'model/experiment/output/gradient_boosting_basic',
        load_sample_data_frame(),
        'violation',
        gradient_boosting_basic,
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
    test_gradient_boosting_basic()
