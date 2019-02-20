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

from skopt.space import Integer

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_data_frame, ordinal_data_mapper

sample = 10000
iterations = 2

hyper_parameters = HyperParameters(search_space={
    'rf__n_estimators': Integer(50, 500),
    'rf__max_depth': Integer(5, 15),
    'rf__min_samples_leaf': Integer(6, 60),
    'rf__min_samples_split': Integer(12, 120)
})

random_forest_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('rf', RandomForestClassifier())
])


def test_random_forest_basic():
    runner = Runner(
        'model/experiment/output/random_forest_basic',
        load_data_frame(),
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
