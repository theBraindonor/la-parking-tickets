# Completed Experiments

Please note that the following experiments were conducted without setting a random_state value.
These models are for exploration of the data only. Final models will be constructed with
repeatability in mind.

The goal for most models with hyper-parameters is to run 24 iterations using BayesSearchCV.

## Bernoulli Naive Bayes

Performed on a 20% Sample (1473635 records); Single Iteration

```
Accuracy: 0.560130
Log-Loss: 1.425886
```

## Complement Naive Bayes

Performed on a 20% Sample (1473635 records); Single Iteration

```
Accuracy: 0.560592
Log-Loss: 1.424041
```

## Decision Tree

Performed on a 20% Sample (1473635 records); 24 Iterations

```
Accuracy: 0.594481
Log-Loss: 1.364006
```

## Extra Trees

Performed on a 20% Sample (1473635 records); 24 Iterations

```
Accuracy: 0.652468
Log-Loss: 1.496213
```

## Gradient Boosting

```
Accuracy: 0.546133
Log-Loss: 1.487148
```

## LightGBM Model

Performed on a 20% Sample; 24 Iterations

```
Accuracy: 0.674348
Log-Loss: 1.082473
```

## Neural Network Model

Performed on 200k Sample; Single Iteration

```
Accuracy: 0.627325
Log-Loss: 1.232498
```

## Random Forest Model

Performed on 200k Sample; 2 Iterations (More to Come) ~30 minute runtime

```
Accuracy: 0.595365
Log-Loss: 1.330450
```

## XGBoost Model

Performed on a 20% Sample; 24 Iterations
~ 45 minutes per iteration

```
Accuracy: 0.713297
Log-Loss: 0.946272
```
