# Los Angeles Parking Tickets

_A Machine Learning Application for Parking Tickets in Los Angeles, California._

This project was created for DSC 478: Programming Machine Learning Applications as part of the
Master's in Data Science program at DePaul University in Chicago, IL during the winter 2019
quarter.  In this class, students were tasked with creating a data analysis or application
development project.  This project is primarily a data analysis project but also contains a
small application to demonstrate how the predictive model can be deployed.

## Data Source

The data for this project was taken from the Los Angeles Open Data Portal:
https://data.lacity.org/A-Well-Run-City/Parking-Citations/wjz9-h9np

## Running the Application

The application is broken into two parts: a Python-based web service to service the model and a
React web application to call the model.

### Model Web Service

Running the web service requires Python3.6+ to be installed.  It is highly recommended that
a virtual environment be created.  The final model built as part of the data analysis has been
included.  It will not be necessary to replicate the data analysis prior to running the web
application.

On Windows:
```
python -m virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
python -m sevice.service
```

On OSX and Linux:

```
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m sevice.service
```

### Model Web UI

Running the web application requires that NodeJS and yarn be installed.  It can be run with the
following commands.

```
cd webapp
yarn install
yarn start
```

The final command will launch a web browser with the application.  The application contains a
map centered on Los Angeles.  Specific GPS coordinates can be selected by clicking on the map.
All other values required by the model can be selected via dropdown.  When the application calls
the model, it will display the four most likely tickets that would be received by a vehicle owner
given the values entered into the form.

## Analysis Replication

This analysis has been constructed with replication in mind.  Data from the Los Angeles Open
Data Portal should be saved in `data_scratch/Parking_Citations.csv`.  This file was too large
to be included.

### PreProcessing

```
python -m data.preprocess
python -m data.sample
```

### Initial Data Exploration

```
python -m jupyter notebook notebooks/data_exploration.ipynb
```

### Exploratory Model Building

```
python -m model.experiment.bernoulli_naive_bayes_basic
python -m model.experiment.complement_naive_bayes_basic
python -m model.experiment.decision_tree_basic
python -m model.experiment.extra_trees_basic
python -m model.experiment.gradient_boosting_basic
python -m model.experiment.lightgbm_basic
python -m model.experiment.neural_network_basic
python -m model.experiment.random_forest_basic
python -m model.experiment.xgboost_basic
```

### Exploratory Model Evaluation

```
python -m jupyter notebook notebooks/model_comparisons.ipynb
```

### Final Model Building

```
python -m model.xgboost_model
```