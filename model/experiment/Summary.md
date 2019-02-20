# Completed Experiments

Please note that the following experiments were conducted without setting a random_state value.
These models are for exploration of the data only. Final models will be constructed with
repeatability in mind.

The goal for most models with hyper-parameters is to run 24 iterations using BayesSearchCV.

## Bernoulli Naive Bayes

Performed on a 20% Sample (1473635 records); Single Iteration; Maximum size supported by current computing resources.

```
Accuracy: 0.560130
Log-Loss: 1.425886
```

## Complement Naive Bayes

Performed on a 20% Sample (1473635 records); Single Iteration; Maximum size supported by current computing resources.

```
Accuracy: 0.560592
Log-Loss: 1.424041
```

## Decision Tree

Performed on a 20% Sample (1473635 records); 24 Iterations

```
Accuracy: 0.594481
Log-Loss: 1.364006

Hyper-Parameters: {
    'dt__criterion': 'entropy',
    'dt__max_depth': 18,
    'dt__min_samples_leaf': 1e-06,
    'dt__min_samples_split': 0.001054546261691371
}
```

## LightGBM Model

Performed on a 20% Sample; 2 Iterations (More to Come)
~ 10 minutes per iteration

```
Accuracy: 0.605884
Log-Loss: 1.309127
```

## Neural Network Model

Performed on 200k Sample; Single Iteration

```
Accuracy:
Log-Loss
```

## Random Forest Model

```
Accuracy:
Log-Loss
```

## XGBoost Model

Performed on a 20% Sample; 2 Iterations (More to Come)
~ 20 minutes per iteration

```
Accuracy: 0.574036
Log-Loss: 1.378634
```