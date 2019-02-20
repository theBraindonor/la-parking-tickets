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

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB

from utility import Runner
from model import load_data_frame, one_hot_data_mapper

sample = None

gaussian_naive_bayes_basic = Pipeline([
    ('mapper', one_hot_data_mapper),
    ('ng', GaussianNB())
])


def test_gaussian_naive_bayes_basic():
    runner = Runner(
        'model/experiment/output/gaussian_naive_bayes_basic',
        load_data_frame(),
        'violation',
        gaussian_naive_bayes_basic,
        None
    )
    runner.run_classification_experiment(
        sample=sample,
        multiclass=True,
        record_predict_proba=True
    )


if __name__ == '__main__':
    test_gaussian_naive_bayes_basic()
