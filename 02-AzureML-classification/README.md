# Azure ML Studio: Classification

This demo illustrates using Azure ML Studio to run a Classification workload on a dataset.

## Dataset

See [data](./data) for Memphis bike facilities exports and an `MLTable` file for use as an Azure ML Studio data asset.

Suggested label columns for a classification demo:
- `status` (Existing vs programmed)
- `facility_c` (facility type)

## Prerequisites

- Azure Subscription
- An Azure Resource Group + Workspace

## Setup (Azure ML Designer)

1. In Azure ML Studio, go to **Data** → **Create**.
2. Create a **data asset** from this folder’s `MLTable` (recommended), or upload `Bike_Facilities_Existing_and_Programmed.cleaned.csv` as a tabular dataset.
3. Go to **Designer** and create a new pipeline.
4. Drag the dataset onto the canvas.
5. Add **Select Columns in Dataset** and choose a label column:
   - Simple 2-class demo: `status` (`Existing` vs programmed)
   - Multi-class demo: `facility_c` (facility type)
6. Add **Clean Missing Data** (optional) and then **Split Data** (e.g., 70/30).
7. Add **Train Model** + a classifier (e.g., **Two-Class Logistic Regression** for `status`). Set the label column.
8. Add **Score Model** and **Evaluate Model**, then **Submit** to run the pipeline.

## Additional Resources

- Video: [Learn Azure Maching Learning Designer](https://learn.microsoft.com/en-us/shows/ai-show/azure-machine-learning-designer)
- AzureML: [What is Designer in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer?view=azureml-api-1)
