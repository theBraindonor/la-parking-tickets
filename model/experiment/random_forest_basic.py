#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with a basic Random Forest model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

from skopt.space import Integer, Real

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = None
iterations = 2

hyper_parameters = HyperParameters(search_space={
    'rf__n_estimators': Integer(50, 500),
    'rf__max_depth': Integer(4, 16),
    'rf__min_samples_leaf': Real(0.00001, 0.001),
    'rf__min_samples_split': Real(0.00002, 0.002)
})

random_forest_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('rf', RandomForestClassifier())
])


def test_random_forest_basic():
    runner = Runner(
        'model/experiment/output/random_forest_basic',
        load_sample_data_frame(),
        'violation',
        random_forest_basic,
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
    test_random_forest_basic()
