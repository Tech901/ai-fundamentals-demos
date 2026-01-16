# Azure ML Studio: Clustering

This demo illustrates using Azure ML Studio to run a Clustering workload on a dataset.

## Dataset

See [data](./data) for Memphis bike facilities exports and an `MLTable` file for use as an Azure ML Studio data asset.

## Prerequisites

- Azure Subscription
- An Azure Resource Group + Workspace

## Setup (Azure ML Designer)

1. In Azure ML Studio, go to **Data** → **Create**.
2. Create a **data asset** from this folder’s `MLTable` (recommended), or upload `Bike_Facilities_Existing_and_Programmed.cleaned.csv` as a tabular dataset.
3. Go to **Designer** and create a new pipeline.
4. Drag the data asset onto the canvas.
5. Build the data pipeline; The connected components should look something like the following.
   ```mermaid
   graph TD

   a[Convert to Dataset]
   b[Select Columns in Datset ]
   c[Clean Missing Data]
   d[Convert to Indicator Values]
   e[Normalize Data]
   f[Train Clustering Model]
   g[K-Means Clustering]
   h[Assign Data To Clusters]
   i[Export Data]

   a --> b
   b --> c
   c --> d
   d --> e
   e --> f
   e --> h
   g --> f
   f --> h
   h --> i
   ```
6. Click Configure & Submit.


## Additional Resources

- Video: [Learn Azure Maching Learning Designer](https://learn.microsoft.com/en-us/shows/ai-show/azure-machine-learning-designer)
- AzureML: [What is Designer in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer?view=azureml-api-1)
