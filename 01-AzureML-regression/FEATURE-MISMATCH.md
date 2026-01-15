# Quick Reference: Model Features

This document explains the feature mismatch between training datasets and models.

## The Issue

Your **AutoML model** was trained on a dataset with **13 features**, but the cleaned CSV files in this repo only have **8 features**. This causes inference to fail with a "missing inputs" error.

## Feature Comparison

### Cleaned Dataset (8 features)
Used by `train.py`:
- name
- year
- selling_price (target)
- km_driven
- fuel
- seller_type
- transmission
- owner

### Full Dataset (13+ features)
Used by AutoML (your model expects these):
- **Path** ⬅️ Missing
- **name** ✓
- **year** ✓
- **km_driven** ✓
- **fuel** ✓
- **seller_type** ✓
- **transmission** ✓
- **owner** ✓
- **mileage** ⬅️ Missing
- **engine** ⬅️ Missing
- **max_power** ⬅️ Missing
- **torque** ⬅️ Missing
- **seats** ⬅️ Missing

## Solutions

### Option 1: Use Test Data with All Features
```bash
python src/inference_demo.py \
  --model-path ./downloads/<AUTOML_JOB>/outputs/mlflow-model \
  --data ./data/test-cars-full.csv
```

### Option 2: Use Custom Trained Model
The `train.py` script only uses 6 features (year, km_driven, fuel, seller_type, transmission, owner):
```bash
# Download the custom training job
JOB_NAME="car-price-train-cli_XXXXX"
az ml job download --name "$JOB_NAME" --download-path ./downloads

# Run inference (works with cleaned data)
python src/inference_demo.py \
  --model-path ./downloads/$JOB_NAME/outputs/model.joblib
```

### Option 3: Retrain AutoML with Cleaned Data
Modify `car-price-automl-job.yml` to ensure it uses the cleaned dataset, then retrain:
```bash
az ml job create --file car-price-automl-job.yml
```

## Checking Your Model's Requirements

To see what features your model expects:
```bash
# For MLflow models
cat downloads/<JOB_NAME>/outputs/mlflow-model/MLmodel | grep -A 20 "signature:"

# This will show you the exact input schema
```

## For Students

**Key Takeaway**: Models must receive the **same features** they were trained on. If training used 13 features, inference must provide all 13 features in the same format.

This is a common real-world issue when:
- Different team members use different datasets
- Data preprocessing varies between training and production
- Models are retrained on updated datasets

Always document and version your:
1. Training data schema
2. Feature engineering steps
3. Model input requirements
