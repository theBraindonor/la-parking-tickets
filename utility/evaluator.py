#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

import numpy as np
import pandas as pd

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, log_loss


class Evaluator:
    def __init__(self, logger):
        self.logger = logger

    def evaluate_classifier_result(self, results, test, train=None, multiclass=False):
        self.logger.log('')
        self.logger.log('Best Score:')
        self.logger.log(results.best_score_)
        self.logger.log('')

        self.logger.log('Best Parameters:')
        self.logger.log(results.best_params_)
        self.logger.log('')

        self.logger.log('Classification Report:')
        self.logger.log(classification_report(test.y_actual, test.y_predict))
        self.logger.log('')

        self.logger.log('Confusion Matrix:')
        self.logger.log(pd.DataFrame(confusion_matrix(test.y_actual, test.y_predict)))
        self.logger.log('')

        if train is not None:
            self.logger.log('Accuracy:')
            self.logger.log('   Train: %f' % accuracy_score(train.y_actual, train.y_predict))
            self.logger.log(' Testing: %f\n' % accuracy_score(test.y_actual, test.y_predict))
        else:
            self.logger.log('Accuracy: %f\n' % accuracy_score(test.y_actual, test.y_predict))

        if not multiclass:
            if train is not None:
                self.logger.log('     AUC:')
                self.logger.log('   Train: %f' % roc_auc_score(train.y_actual, train.y_predict))
                self.logger.log(' Testing: %f\n' % roc_auc_score(test.y_actual, test.y_predict))
            else:
                self.logger.log('     AUC: %f\n' % roc_auc_score(test.y_actual, test.y_predict))

        try:
            if train is not None:
                self.logger.log('Log Loss:')
                self.logger.log('   Train: %f' % log_loss(train.y_actual, train.y_predict))
                self.logger.log(' Testing: %f\n' % log_loss(test.y_actual, test.y_predict))
            else:
                self.logger.log('Log Loss: %f\n' % log_loss(test.y_actual, test.y_predict))
        except ValueError as error:
            self.logger.log('Unable to calculate log-loss: %s\n' % error)

        if 'pca' in results.best_estimator_.named_steps:
            pca_n_components = results.best_estimator_.named_steps['pca'].n_components_
            pca_explained_variance = np.sum(results.best_estimator_.named_steps['pca'].explained_variance_ratio_)
            self.logger.log('PCA:')
            self.logger.log('      N Components: %f' % pca_n_components)
            self.logger.log('Explained Variance: %f' % pca_explained_variance)
            self.logger.log('')

        self.logger.log('Search Scoring')
        scoring = pd.DataFrame(results.cv_results_)
        scoring = scoring.sort_values('mean_test_score', ascending=False)
        scoring = scoring.filter([
            'mean_test_score', 'std_test_score',
            'mean_train_score', 'std_train_score',
            'mean_fit_time', 'mean_score_time',
            'params'
        ])
        self.logger.log(scoring)
        self.logger.log('')
