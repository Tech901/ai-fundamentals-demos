# Running Inference with AzureML Models

After training models in AzureML, you have several options for running inference (making predictions). This guide covers both local inference and deploying models as endpoints.

---

## Prerequisites

- Completed training jobs (either AutoML or custom Python script)
- Downloaded model artifacts from AzureML
- Python environment with required packages:
  - **For custom models**: `pip install scikit-learn pandas joblib`
  - **For AutoML models**: `pip install mlflow` (if MLflow format)
  - Both model types use the same `.predict()` interface

---

## Step 1: Download Your Trained Model

First, get your job name and download the model artifacts:

```bash
# List recent jobs
az ml job list --max-results 10 -o table

# Set your job name (from the list above)
JOB_NAME="car-price-train-cli_XXXXX"  # or "car-price-automl-cli_XXXXX"

# Download all job outputs
mkdir -p ./downloads
az ml job download --name "$JOB_NAME" --download-path ./downloads
```

**Model locations after download:**
- **Custom training job** (`train.py`): `./downloads/<JOB_NAME>/outputs/model.joblib`
- **AutoML job** (MLflow): `./downloads/<JOB_NAME>/outputs/mlflow-model/` (directory)
- **AutoML job** (pickle): `./downloads/<JOB_NAME>/outputs/model.pkl` (file)

**Tip**: Use `ls -la ./downloads/<JOB_NAME>/outputs/` to see what format your model is in.

**⚠️ IMPORTANT: Feature Mismatch Issue**

Your AutoML model may have been trained on a dataset with **13 features** (including Path, name, mileage, engine, max_power, torque, seats), but the cleaned CSV in this repo only has **8 features**. 

To check what your model expects, look at the model signature in `MLmodel` file:
```bash
cat downloads/<JOB_NAME>/outputs/mlflow-model/MLmodel | grep -A 20 "signature:"
```

**Solutions:**
1. Use the test data file with all 13 features: `--data ./data/test-cars-full.csv`
2. Or download a model from the `train.py` job which only uses 6 features
3. Or retrain AutoML with the cleaned dataset that has fewer features

---

## Option 1: Local Inference (Quick & Simple)

### A. Using the Demo Script

Use the provided `inference_demo.py` script for quick testing. The script automatically detects the model format (joblib, pickle, or MLflow):

```bash
# For custom trained model (train.py) - joblib format
python src/inference_demo.py \
  --model-path ./downloads/<JOB_NAME>/outputs/model.joblib

# For AutoML model - MLflow directory format
python src/inference_demo.py \
  --model-path ./downloads/<JOB_NAME>/outputs/mlflow-model

# For AutoML model - pickle format (some AutoML versions)
python src/inference_demo.py \
  --model-path ./downloads/<JOB_NAME>/outputs/model.pkl

# With custom test data that matches model features (RECOMMENDED for AutoML)
python src/inference_demo.py \
  --model-path ./downloads/<JOB_NAME>/outputs/mlflow-model \
  --data ./data/test-cars-full.csv
```

**Note**: The script includes sample data with all 13 features for AutoML models. If your model expects different features, use the `--data` flag with a CSV that matches your model's training data.

The script supports multiple formats:
- **`.joblib`** files (custom models from `train.py`)
- **`.pkl`** files (pickle format)
- **MLflow directories** (typical AutoML output)

For MLflow models, ensure you have mlflow installed: `pip install mlflow`

### B. Manual Python Inference

Create a simple Python script or use in a Jupyter notebook:

**For Custom Models (joblib/pickle):**

```python
import joblib
import pandas as pd

# Load the model
model = joblib.load('./downloads/<JOB_NAME>/outputs/model.joblib')

# Prepare test data (must match training features)
test_data = pd.DataFrame({
    'year': [2015, 2018, 2020],
    'km_driven': [50000, 30000, 15000],
    'fuel': ['Petrol', 'Diesel', 'Diesel'],
    'seller_type': ['Individual', 'Dealer', 'Dealer'],
    'transmission': ['Manual', 'Manual', 'Automatic'],
    'owner': ['First Owner', 'First Owner', 'First Owner']
})

# Make predictions
predictions = model.predict(test_data)

# Display results
for idx, price in enumerate(predictions):
    print(f"Car {idx+1}: Predicted price = ₹{price:,.2f}")
```

**For AutoML Models (MLflow format):**

```python
import mlflow.pyfunc
import pandas as pd

# Load the MLflow model
model = mlflow.pyfunc.load_model('./downloads/<JOB_NAME>/outputs/mlflow-model')

# Prepare test data (same as above)
test_data = pd.DataFrame({
    'year': [2015, 2018, 2020],
    'km_driven': [50000, 30000, 15000],
    'fuel': ['Petrol', 'Diesel', 'Diesel'],
    'seller_type': ['Individual', 'Dealer', 'Dealer'],
    'transmission': ['Manual', 'Manual', 'Automatic'],
    'owner': ['First Owner', 'First Owner', 'First Owner']
})

# Make predictions (same interface!)
predictions = model.predict(test_data)

# Display results
for idx, price in enumerate(predictions):
    print(f"Car {idx+1}: Predicted price = ₹{price:,.2f}")
```

**Note**: Both joblib and MLflow models use the same `.predict()` interface, making the code very similar!

---

## Option 2: Deploy as AzureML Endpoint (Production)

For production scenarios, deploy your model as a managed online endpoint.

### A. Register the Model

```bash
# For custom training job
az ml model create \
  --name car-price-model \
  --version 1 \
  --path azureml://jobs/$JOB_NAME/outputs/model.joblib \
  --type custom_model

# For AutoML job (typically MLflow format)
az ml model create \
  --name car-price-automl \
  --version 1 \
  --path azureml://jobs/$JOB_NAME/outputs/model \
  --type mlflow_model

# Verify registration
az ml model list -o table
```

### B. Create Scoring Script (Custom Models Only)

For custom models, create `src/score.py`:

```python
import json
import joblib
import pandas as pd
import os


def init():
    """Called when the endpoint initializes."""
    global model
    # AZUREML_MODEL_DIR points to the model directory
    model_path = os.path.join(
        os.getenv('AZUREML_MODEL_DIR'),
        'model.joblib'
    )
    model = joblib.load(model_path)
    print("Model loaded successfully")


def run(raw_data):
    """Called for each prediction request."""
    try:
        # Parse input JSON
        data = json.loads(raw_data)
        
        # Convert to DataFrame
        df = pd.DataFrame(data['data'])
        
        # Make predictions
        predictions = model.predict(df)
        
        # Return as list
        return predictions.tolist()
    
    except Exception as e:
        error = str(e)
        return {"error": error}
```

### C. Create Deployment Configuration

Create `deployment.yml`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: car-price-endpoint
model: azureml:car-price-model:1
code_configuration:
  code: ./src
  scoring_script: score.py
environment:
  conda_file: conda.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
instance_type: Standard_DS2_v2
instance_count: 1
```

Create `conda.yml`:

```yaml
name: inference_env
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pip
  - pip:
    - scikit-learn==1.0.2
    - pandas==1.3.5
    - joblib==1.1.0
    - azureml-defaults
```

### D. Deploy the Endpoint

```bash
# Create the endpoint
az ml online-endpoint create \
  --name car-price-endpoint

# Deploy the model
az ml online-deployment create \
  --file deployment.yml

# Set traffic to 100% for this deployment
az ml online-endpoint update \
  --name car-price-endpoint \
  --traffic "blue=100"

# Check endpoint status
az ml online-endpoint show \
  --name car-price-endpoint -o table
```

### E. Test the Endpoint

See the `src/test-request.json` file.

Invoke the endpoint:

```bash
# Test the endpoint
az ml online-endpoint invoke \
  --name tech901-workspace-zujbb \
  --request-file test-request.json

# Get endpoint logs (for debugging)
az ml online-deployment get-logs \
  --name blue \
  --endpoint-name tech901-workspace-zujbb
```

---

## Option 3: Batch Inference (Large Datasets)

For processing large amounts of data, use batch endpoints:

```bash
# Create batch endpoint
az ml batch-endpoint create --name car-price-batch

# Create batch deployment
az ml batch-deployment create \
  --name batch-deployment \
  --endpoint-name car-price-batch \
  --model azureml:car-price-model:1 \
  --compute-name cpu-cluster

# Invoke batch prediction
az ml batch-endpoint invoke \
  --name car-price-batch \
  --input azureml:car-details-dehko@latest
```

---

## AutoML Specific Notes

**AutoML models are typically MLflow format**, which means:

1. **Easier deployment**: No need to write a scoring script
2. **Model signature**: Input/output schema is automatically tracked
3. **Direct invocation**: Can use MLflow's `predict()` directly
4. **Multiple file formats**: AutoML may output as MLflow directory, pickle, or joblib

### Loading AutoML Models

**MLflow Directory (most common):**
```python
import mlflow.pyfunc

# Load from MLflow model directory
model = mlflow.pyfunc.load_model('./downloads/<JOB_NAME>/outputs/mlflow-model')
predictions = model.predict(test_data)
```

**Pickle/Joblib Files (some AutoML versions):**
```python
import joblib

# Some AutoML jobs save as pickle
model = joblib.load('./downloads/<JOB_NAME>/outputs/model.pkl')
predictions = model.predict(test_data)
```

**Using inference_demo.py (handles all formats automatically):**
```bash
# Works with MLflow directories, .pkl, or .joblib files
python src/inference_demo.py --model-path ./downloads/<JOB_NAME>/outputs/mlflow-model
python src/inference_demo.py --model-path ./downloads/<JOB_NAME>/outputs/model.pkl
```

### AutoML Endpoint Deployment

```bash
# AutoML models deploy more easily (no scoring script needed)
az ml online-endpoint create --name car-price-automl-endpoint
az ml online-deployment create \
  --name blue \
  --endpoint car-price-automl-endpoint \
  --model azureml:car-price-automl:1 \
  --instance-type Standard_DS2_v2
```

---

## Troubleshooting

### Model Loading Errors
- **Issue**: `ModuleNotFoundError` or import errors
- **Solution**: 
  - For joblib models: `pip install scikit-learn pandas joblib`
  - For MLflow models: `pip install mlflow`
  - Ensure versions match training environment

### MLflow Not Found
- **Issue**: `ImportError: No module named 'mlflow'`
- **Solution**: Install MLflow: `pip install mlflow`
- **Note**: Only needed for AutoML MLflow directory models

### Prediction Errors
- **Issue**: Feature mismatch or wrong data types
- **Solution**: Verify test data has exact same columns and types as training data

### Endpoint Deployment Failures
- **Issue**: Endpoint stays in "Creating" state
- **Solution**: Check logs with `az ml online-deployment get-logs`

### Feature Order Mismatch
- **Issue**: Predictions are nonsensical
- **Solution**: Ensure DataFrame columns are in the same order as training

---

## Cost Management

**Online endpoints** run continuously and incur compute costs:
- Use smallest instance type during testing (`Standard_DS2_v2`)
- Scale to zero when not in use or delete the endpoint
- For infrequent predictions, use local inference or batch endpoints

```bash
# Delete endpoint when done
az ml online-endpoint delete --name car-price-endpoint --yes
```

---

## Summary for Students

| Method | Use Case | Pros | Cons |
|--------|----------|------|------|
| **Local Inference** | Development, testing, demos | Free, fast setup, easy debugging | Manual scaling, no REST API |
| **Online Endpoint** | Production, real-time predictions | Auto-scaling, managed, REST API | Costs money, more complex setup |
| **Batch Endpoint** | Large datasets, scheduled jobs | Cost-effective for bulk predictions | Not real-time, more setup |

**Recommendation**: Start with local inference using `inference_demo.py`, then move to online endpoints when ready for production.

---

## Additional Resources

- [Azure ML Managed Online Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-managed-online-endpoints)
- [Deploy MLflow models](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models)
- [Batch Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-batch-endpoint)
