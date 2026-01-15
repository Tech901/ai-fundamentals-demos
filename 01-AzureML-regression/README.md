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

### Goal

Run **(1)** a simple Python regression training job and **(2)** an AutoML regression job from the CLI.

### Files for CLI demos

- `./src/train.py` – trains a simple regression model and writes `outputs/model.joblib`
- `./car-price-train-job.yml` – `command` job (Python script)
- `./car-price-automl-job.yml` – AutoML regression job (restricted algorithms + metric)
- `./car-price-train-schedule.yml` – example schedule (optional)

### 1. Select your workspace (assumes it already exists)

```bash
# If you don't know the resource group, list workspaces first:
az ml workspace list -o table

RG="<YOUR_RESOURCE_GROUP>"
WS="tech901-workspace"

az configure --defaults group="$RG" workspace="$WS"
az ml workspace show -o table
```

### 2. Create a data asset (uploaded to the workspace blob storage)

This folder already includes an `MLTable` definition pointing at `car-details-from-car-dehko.cleaned.csv`.

```bash
cd 01-AzureML-regression

az ml data create \
  --name car-details-dehko \
  --version 1 \
  --type mltable \
  --path ./data

az ml data show --name car-details-dehko --version 1 -o table
```

### 3. Compute (prefer serverless; otherwise use an existing cluster)

```bash
# Serverless requires no setup; if it isn't enabled, use an existing compute instead.
az ml compute list -o table

# Optional: create a small CPU cluster if you need one
az ml compute create \
  --name cpu-cluster \
  --type amlcompute \
  --size Standard_DS3_v2 \
  --min-instances 0 \
  --max-instances 2
```

⚠️ If serverless **is NOT** available in your workspace/subscription, explicitly set a compute target in the job YAML.

- In `car-price-train-job.yml`, add: `compute: azureml:cpu-cluster`
- (And make sure the cluster exists first: `az ml compute create --name cpu-cluster --type amlcompute ...`)

### 4. Run the simple Python regression job (CLI command job)

```bash
az ml job create --file car-price-train-job.yml --stream
```

### 5. Run AutoML regression from the CLI (restricted algorithms)

This job uses:
- task: `regression`
- primary metric: `normalized_root_mean_squared_error`
- allowed models: `LightGBM`, `KNN`, `XGBoostRegressor`

Note: some Azure ML CLI/extension versions don’t expose AutoML “explain best model” in YAML; if you need that, enable it in Studio/SDK for the AutoML run.

```bash
az ml job create --file car-price-automl-job.yml --web
```

### 6. (Optional) Schedule the training job
Do this if you want a model to be retrained periodically ... assuming you have new data to re-train the model.

```bash
az ml schedule create --file car-price-train-schedule.yml
az ml schedule list -o table
```

### 7. Check job status

```bash
az ml job list --max-results 10 -o table

# Replace with your returned job name (e.g., "car-price-train-cli_...")
JOB_NAME="<JOB_NAME>"
az ml job show --name "$JOB_NAME" -o table
az ml job stream --name "$JOB_NAME"
```

### 8. Fetch results/artifacts

```bash
mkdir -p ./downloads
az ml job download --name "$JOB_NAME" --download-path ./downloads

# For the Python job, your trained model will be at:
# ./downloads/<JOB_NAME>/outputs/model.joblib
```

---

## Running Inference

Once you've downloaded your model, see **[INFERENCE.md](INFERENCE.md)** for detailed instructions on:
- Running local inference with the demo script
- Understanding model input requirements
- Deploying models as endpoints
- Handling different model formats (joblib, pickle, MLflow)

**Quick start:**
```bash
# For custom trained model (train.py)
python src/inference_demo.py --model-path ./downloads/<JOB_NAME>/outputs/model.joblib

# For AutoML model with full feature set
python src/inference_demo.py --model-path ./downloads/<JOB_NAME>/outputs/mlflow-model --data ./data/test-cars-full.csv
```

---

## Additional Resources

- Azure [Tutorial on AutoML](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml?view=azureml-api-2)
- [Inference Guide](INFERENCE.md) - Detailed guide on running predictions