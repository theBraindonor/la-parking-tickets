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

from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from utility import HyperParameters, Runner
from model import load_data_frame, ordinal_data_mapper

sample = None
iterations = 2

hyper_parameters = HyperParameters({
    'dt__max_depth': Integer(4, 20),
    'dt__min_samples_leaf': Integer(6, 120),
    'dt__min_samples_split': Integer(12, 240)
})

decision_tree_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('dt', DecisionTreeClassifier())
])


def test_decision_tree_basic():
    runner = Runner(
        'model/experiment/output/decision_tree_basic',
        load_data_frame(),
        'violation',
        decision_tree_basic,
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
    test_decision_tree_basic()
