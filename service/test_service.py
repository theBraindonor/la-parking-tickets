#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Test the ticket model being serviced on localhost:8080
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

import json
import requests

from utility import use_project_path
from model import load_sample_data_frame

if __name__ == '__main__':
    use_project_path()

    for index, row in load_sample_data_frame().iterrows():
        print(row.to_json())
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post('http://127.0.0.1:8080/ticketPrediction', data=row.to_json(), headers=headers)
        print(json.loads(response.text))

        if index > 100:
            break

