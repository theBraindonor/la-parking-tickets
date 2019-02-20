#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Experiment with a basic neural network model
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier

from utility import Runner
from model import load_sample_data_frame, ordinal_data_mapper

sample = 200000

neural_network_basic = Pipeline([
    ('mapper', ordinal_data_mapper),
    ('nn', MLPClassifier(hidden_layer_sizes=(200, 100,), max_iter=500))
])


def test_neural_network_basic():
    runner = Runner(
        'model/experiment/output/neural_network_basic',
        load_sample_data_frame(),
        'violation',
        neural_network_basic,
        None
    )
    runner.run_classification_experiment(
        sample=sample,
        multiclass=True,
        record_predict_proba=True
    )


if __name__ == '__main__':
    test_neural_network_basic()
