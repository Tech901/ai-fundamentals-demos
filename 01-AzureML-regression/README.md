# Azure ML Studio: Regression

This demo illustrates using Azure ML Studio to predict car prices based on past data.

## Prerequisites

- Azure Subscription
- An Azure Resource Group + Workspace

## Option 1: Automated ML (AutoML)

**Goal**: Use Automated Machine learning to implement a linear regression model(s) to predict a future outcome.

### Setting up the AutoML Regression Job

Steps to set up a Regression Job:

1. Select _Automated ML_
2. Training Method: _Regression_.
3. Upload data & specify Schema:
    - Choose Tabular data.
    - Upload a CSV or XLSX file.
    - Ensure the Schema looks good.
4. Task type & Data: Rleoad & select the data set you uploaded.
5. Review compute infrastructure & submit job.

## Option 2: Using `az ml`

TBD.


## Additional Resources

- Azure [Tutorial on AutoML](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml?view=azureml-api-2)