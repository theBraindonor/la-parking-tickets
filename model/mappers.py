#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Common Data Mappers for Experiments
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

from sklearn_pandas import DataFrameMapper

ordinal_data_mapper = DataFrameMapper([
    (['month'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['weekday'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['hour'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['state'], [SimpleImputer(strategy='most_frequent'), MinMaxScaler()]),
    (['make'], [SimpleImputer(strategy="constant", fill_value=0), MinMaxScaler()]),
    (['color'], [SimpleImputer(strategy="constant", fill_value=0), MinMaxScaler()]),
    (['latitude'], [SimpleImputer(strategy='median'), StandardScaler()]),
    (['longitude'], [SimpleImputer(strategy='median'), StandardScaler()])
])

one_hot_data_mapper = DataFrameMapper([
    (['month'], [SimpleImputer(strategy='most_frequent'), OneHotEncoder(handle_unknown='ignore')]),
    (['weekday'], [SimpleImputer(strategy='most_frequent'), OneHotEncoder(handle_unknown='ignore')]),
    (['hour'], [SimpleImputer(strategy='most_frequent'), OneHotEncoder(handle_unknown='ignore')]),
    (['state'], [SimpleImputer(strategy='most_frequent'), OneHotEncoder(handle_unknown='ignore')]),
    (['make'], [SimpleImputer(strategy="constant", fill_value=0), OneHotEncoder(handle_unknown='ignore')]),
    (['color'], [SimpleImputer(strategy="constant", fill_value=0), OneHotEncoder(handle_unknown='ignore')]),
    (['latitude'], [SimpleImputer(strategy='median'), StandardScaler()]),
    (['longitude'], [SimpleImputer(strategy='median'), StandardScaler()])
])
