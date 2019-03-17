#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with a basic extra trees model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0.0"

from skopt.space import Categorical, Integer, Real

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.pipeline import Pipeline

from utility import HyperParameters, Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = None
iterations = 24

hyper_parameters = HyperParameters({
    'et__n_estimators': Integer(10, 20),
    'et__criterion': Categorical(['gini', 'entropy']),
    'et__max_depth': Integer(4, 24),
    'et__min_samples_leaf': Real(0.000001, 0.001),
    'et__min_samples_split': Real(0.000002, 0.002)
})

extra_trees_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('et', ExtraTreesClassifier())
])


def test_extra_trees_basic():
    runner = Runner(
        'model/experiment/output/extra_trees_basic',
        load_sample_data_frame(),
        'violation',
        extra_trees_basic,
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
    test_extra_trees_basic()
