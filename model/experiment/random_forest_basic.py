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

from skopt.space import Categorical, Integer

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = None
iterations = 24

hyper_parameters = HyperParameters(search_space={
    'rf__n_estimators': Integer(50, 100),
    'rf__criterion': Categorical(['gini', 'entropy']),
    'rf__max_depth': Integer(4, 18),
    'rf__max_features': Categorical(['sqrt', 'log2', None]),
    'rf__bootstrap': Categorical([True, False])
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
