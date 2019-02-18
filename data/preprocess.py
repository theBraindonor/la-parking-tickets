#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Pre-Process the raw data from data.lacity.org.
    It will reduce the columns in the dataset to:
    'violation', 'month', 'weekday', 'hour', 'state', 'make', 'color', 'latitude', 'longitude'
"""

__author__ = "John Hoff"
__email__ = "john.hoff@braindonor.net"
__copyright__ = "Copyright 2019, John Hoff"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License"
__version__ = "1.0"

import csv
from datetime import datetime
import math

from utility import Logger, use_project_path

# In order to process
# Data Dictionaries
# Citation Codes and State Codes are Required.   Makes and Colors default to 0
#

# The raw violation codes are organized primarily by the citation code used on the ticket.  Many of
# these codes have names that overlap and some that cannot be fully resolved.  This list will reduce
# the full violation codes into one of 14 categories.
violation_code_mappings = {
    # ( 0) Street Cleaning
    '80.69BS': 0, '8069BS': 0,
    # ( 1) Meter Expired
    '88.13B+': 1, '8813B': 1,
    # ( 2) Red Zone
    '80.56E4+': 2, '8056E4': 2, '8936': 2,
    # ( 3) Preferred Parking
    '80.58L': 3, '8058L': 3,
    # ( 4) Display of Tabs/Plate
    '5204A-': 4, '5200': 4, '4000A1': 4, '5204A': 4, '5200A': 4,
    # ( 5) No Parking
    '80.69B': 5, '8069B': 5, '8603': 5, '80.66.1D': 5, '86.06': 5,
    # ( 6) Parked Over Time Limit
    '80.69C': 6, '80.73.2': 6, '88.63B+': 6, '80.69.2': 6, '80.54H1': 6, '6344K2': 6, '8069C': 6, '88.64A': 6,
    '80732': 6, '80.54': 6,
    # ( 7) White Zone
    '80.56E1': 7, '8939': 7, '8056E1': 7,
    # ( 8) No Stopping/Standing
    '80.69AP+': 8, '80.61': 8, '80.69A+': 8, '80.70': 8, '80.69AA+': 8, '80.53': 8,
    '8069A': 8, '80.69.1A': 8, '8069AP': 8, '8061': 8, '8069AA': 8,
    # ( 9) Yellow Zone
    '80.56E2': 9, '8056E2': 9,
    # (10) Improperly Parked
    '22500F': 10, '22502A': 10, '22500H': 10, '88.03A': 10, '80.49+': 10, '013': 10, '22500I-': 10, '22500B': 10,
    '21211B': 10, '22502E': 10, '22500C': 10, '22500A': 10, '22500E': 10, '88.53': 10, '6344K7': 10, '22522-': 10,
    # (11) Fire Hydrant
    '22514': 11, '22500.1+': 11,
    # (12) Disabled Parking
    '22507.8A-': 12, '22507.8A': 12, '225078A': 12, '22507.8C2': 12, '22507.8C': 12,
    # (13) Private Property
    '80.71.4': 13, '80714': 13, '80.71.3':13
}

# The violation codes for use after post-processing
violation_codes = {
    'Street Cleaning': 0,
    'Meter Expired': 1,
    'Red Zone': 2,
    'Preferred Parking': 3,
    'Display of Tabs/Plate': 4,
    'No Parking': 5,
    'Parked Over Time Limit': 6,
    'While Zone': 7,
    'No Stopping/Standing': 8,
    'Yellow Zone': 9,
    'Improperly Parked': 10,
    'Fire Hydrant': 11,
    'Disabled Parking': 12,
    'Private Property': 13
}

# State codes for using the data after pre-processing
state_codes = {
    'AL': 1, 'AK': 2, 'AZ': 3, 'AR': 4, 'CA': 5,
    'CO': 6, 'CT': 7, 'DE': 8, 'FL': 9, 'GA': 10,
    'HI': 11, 'ID': 12, 'IL': 13, 'IN': 14, 'IA': 15,
    'KS': 16, 'KY': 17, 'LA': 18, 'ME': 19, 'MD': 20,
    'MA': 21, 'MI': 22, 'MN': 23, 'MS': 24, 'MO': 25,
    'MT': 26, 'NE': 27, 'NV': 28, 'NH': 29, 'NJ': 30,
    'NM': 31, 'NY': 32, 'NC': 33, 'ND': 34, 'OH': 35,
    'OK': 36, 'OR': 37, 'PA': 38, 'RI': 39, 'SC': 40,
    'SD': 41, 'TN': 42, 'TX': 43, 'UT': 44, 'VT': 45,
    'VA': 46, 'WA': 47, 'WV': 48, 'WI': 49, 'WY': 50
}

# Car makes run into a similar problem as the violation codes.  There are a lot of transcription
# errors and usage of non-standard make codes.
make_code_mappings = {
    'OTHR': 0, 'UNK': 0,
    'OLDS': 1,
    'HOND': 2,
    'TOYT': 3, 'TOYO': 3,
    'RROV': 4, 'RANG': 4, 'LROV': 4, 'LAND': 4, 'LNDR': 4,
    'FORD': 5,
    'DODG': 6,
    'MAZD': 7, 'MAZ': 7,
    'CHEV': 8,
    'BMW': 9,
    'JEEP': 10,
    'HYUN': 11, 'HUND': 11,
    'CADI': 12,
    'AUDI': 13,
    'VOLK': 14,
    'MERZ': 15, 'MBNZ': 15, 'MBZ': 15, 'BENZ': 15, 'MERC': 15,
    'ISU': 16, 'ISUZ': 16,
    'LEXS': 17, 'LEXU': 17, 'LEX': 17,
    'NISS': 18,
    'CHRY': 19,
    'INFI': 20,
    'JAGR': 21, 'JAG': 21, 'JAGU': 21,
    'MITS': 22,
    'SUBA': 23,
    'KIA': 24,
    'ACUR': 25,
    'MINI': 26, 'MNNI': 26,
    'GMC': 27,
    'LINC': 28,
    'VOLV': 29,
    'SCIO': 30,
    'HUMM': 31,
    'PONT': 32,
    'BUIC': 33,
    'SAAB': 34, 'SAA': 34,
    'SATU': 35, 'SAT': 35, 'STRN': 35,
    'PLYM': 36,
    'FIAT': 37,
    'MASE': 38,
    'GEO': 39,
    'SUZI': 40,
    'TSMR': 41,
    'GRUM': 42,
    'SMRT': 43,
    'PORS': 44,
    'DAEW': 45,
    'KW': 46, 'KAWK': 46, 'KAWA': 46,
    'DATS': 47,
    'TRIU': 48,
    'YAMA': 49,
    'STLG': 50,
    'LAMO': 51,
    'BENT': 52,
    'FERR': 53,
    'ALFA': 54,
    'ASTO': 55,
    'ROL': 56,
    'RENA': 57
}

# Car make codes for using the data after pre-processing
make_codes = {
    'Other': 0,
    'Oldsmobile': 1,
    'Honda': 2,
    'Toyota': 3,
    'Range Rover': 4,
    'Ford': 5,
    'Dodge': 6,
    'Mazda': 7,
    'Chevrolet': 8,
    'BMW': 9,
    'Jeep': 10,
    'Hyundai': 11,
    'Cadillac': 12,
    'Audi': 13,
    'Volkswagen': 14,
    'Mercedes Benz': 15,
    'Isuzu': 16,
    'Lexus': 17,
    'Nissan': 18,
    'Chrysler': 19,
    'Infinity': 20,
    'Jaguar': 21,
    'Mitsubishi': 22,
    'Subaru': 23,
    'KIA': 24,
    'Acura': 25,
    'MINI': 26,
    'GMC': 27,
    'Lincoln': 28,
    'Volvo': 29,
    'Scion': 30,
    'Hummer': 31,
    'Pontiac': 32,
    'Buick': 33,
    'Saab': 34,
    'Saturn': 35,
    'Plymouth': 36,
    'Fiat': 37,
    'Maserati': 38,
    'Geo': 39,
    'Suzuki': 40,
    'Tesla': 41,
    'Grumman': 42,
    'Smart': 43,
    'Porsche': 44,
    'Daewoo': 45,
    'Kawasaki': 46,
    'Datsun': 47,
    'Triumph': 48,
    'Yamaha': 49,
    'Sterling': 50,
    'Lamborghini': 51,
    'Bentley': 52,
    'Ferrari': 53,
    'Alfa Romeo': 54,
    'Aston-Martin': 55,
    'Rolls-Royce': 56,
    'Renault': 57
}

# Color codes are not managed very cleanly.  I believe these are the best mappings for it based
# on looking at the raw data.
code_code_mappings = {
    'UN': 0, 'OT': 0, # unknown/other
    'GN': 1, 'GR': 11, # green
    'WT': 2, 'WH': 2, # white
    'SL': 3, 'SI': 3, # silver
    'BK': 4, # black
    'GY': 5, # grey
    'BL': 6, 'MR': 6, # blue
    'GO': 7, # gold
    'RE': 8, 'RD': 8, # red
    'BN': 9, 'BR': 9, # brown
    'TN': 10, 'TA': 10, # tan
    'OR': 11,  # orange
    'YE': 13,  # yellow
    'BG': 14   # beige
}

# The color codes for use after pre-processing
color_codes = {
    'Other': 0,
    'Green': 1,
    'White': 2,
    'Silver': 3,
    'Black': 4,
    'Grey': 5,
    'Blue': 6,
    'Gold': 7,
    'Red': 8,
    'Brown': 9,
    'Tan': 10,
    'Orange': 11,
    'Yellow': 12,
    'Beige': 13
}

column_names = [
    'violation',
    'month',
    'weekday',
    'hour',
    'state',
    'make',
    'color',
    'latitude',
    'longitude'
]

if __name__ == '__main__':
    use_project_path()

    logger = Logger('Data_Scratch/preprocess.txt')

    raw_record_count = -1
    processed_records = 0

    missing_data = {}
    for column in column_names:
        missing_data[column] = 0

    logger.time_log('Starting Data Pre-Processing...')

    with open('data_scratch/Parking_Citations.csv') as input_file:
        with open('data_scratch/preprocessed_citations.csv', 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            writer.writerow(column_names)

            for i, line in enumerate(reader):
                raw_record_count += 1
                if raw_record_count == 0:
                    continue

                violation_code = line[14]
                issue_date = line[1]
                issue_time = line[2]
                car_state = line[5]
                car_make = line[8]
                car_color = line[10]
                latitude = line[17]
                longitude = line[18]

                if violation_code in violation_code_mappings:
                    violation_code = violation_code_mappings[violation_code]
                else:
                    missing_data['violation'] += 1
                    violation_code = None

                issue_month = None
                issue_weekday = None
                issue_hour = None
                if issue_date:
                    date_object = datetime.strptime(issue_date, '%m/%d/%Y')
                    issue_weekday = date_object.weekday()
                    issue_month = date_object.month
                else:
                    missing_data['month'] += 1
                    missing_data['weekday'] += 1

                if issue_time:
                    issue_hour = math.floor(int(issue_time) / 100)
                else:
                    missing_data['hour'] += 1

                if car_state in state_codes:
                    car_state = state_codes[car_state]
                else:
                    missing_data['state'] += 1
                    car_state = None

                if car_make in make_code_mappings:
                    car_make = make_code_mappings[car_make]
                else:
                    car_make = 0

                if car_color in code_code_mappings:
                    car_color = code_code_mappings[car_color]
                else:
                    car_color = 0

                if latitude:
                    if latitude == '99999':
                        missing_data['latitude'] += 1
                        latitude = None
                else:
                    missing_data['latitude'] += 1
                    latitude = None

                if longitude:
                    if longitude == '99999':
                        missing_data['longitude'] += 1
                        longitude = None
                else:
                    missing_data['longitude'] += 1
                    longitude = None

                if (
                        violation_code is not None and
                        issue_month is not None and
                        issue_weekday is not None and
                        issue_hour is not None and
                        issue_time is not None and
                        car_state is not None and
                        latitude is not None and
                        longitude is not None
                ):
                    writer.writerow([
                        violation_code,
                        issue_month,
                        issue_weekday,
                        issue_hour,
                        car_state,
                        car_make,
                        car_color,
                        latitude,
                        longitude
                    ])
                    processed_records += 1

    logger.time_log('Data Pre-Processing Complete.\n')
    logger.log('    Total Records: %s' % raw_record_count)
    logger.log('Processed Records: %s\n' % processed_records)
    logger.log('Records with missing or incomplete data:')
    for column in column_names:
        logger.log("%s: %s" % (column, missing_data[column]))
    logger.close()
