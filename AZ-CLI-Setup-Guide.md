# Azure CLI (`az`) Setup Guide (AI-900 demos)

This guide helps you install and use the Azure CLI (`az`) for this course, including submitting a simple **Azure Machine Learning** job.

## Requirements

- An Azure subscription you can create resources in
  - If you’re using a school subscription, you may need the instructor to grant permissions.
- A terminal
  - Windows: PowerShell / Windows Terminal
  - macOS/Linux: Terminal
- (Recommended) A code editor: VS Code

## Helpful links

- Azure CLI: Get started + install
  - https://learn.microsoft.com/cli/azure/get-started-with-azure-cli
- Install Azure CLI (OS-specific)
  - https://learn.microsoft.com/cli/azure/install-azure-cli
- Azure ML CLI v2 (`az ml`) overview
  - https://learn.microsoft.com/azure/machine-learning/how-to-configure-cli
- Azure ML “hello world” style job concepts
  - https://learn.microsoft.com/azure/machine-learning/how-to-train-with-cli

---

## 1) Install Azure CLI

Follow the official install instructions for your OS:

- Windows: https://learn.microsoft.com/cli/azure/install-azure-cli-windows
- macOS: https://learn.microsoft.com/cli/azure/install-azure-cli-macos
- Linux: https://learn.microsoft.com/cli/azure/install-azure-cli-linux

Verify the install:

```bash
az version
```

---

## 2) Log in and choose your subscription

Log in (opens a browser):

```bash
az login
```

If a browser can’t open, use device code:

```bash
az login --use-device-code
```

List subscriptions and pick the one you’ll use:

```bash
az account list --output table
az account set --subscription "<SUBSCRIPTION_NAME_OR_ID>"
az account show --output table
```

---

## 3) Install the Azure ML extension (`az ml`)

Azure ML commands are provided by an extension.

```bash
az extension add -n ml -y
az extension show -n ml --output table
```

(If you run into “provider not registered” errors later, register these once per subscription.)

```bash
az provider register -n Microsoft.MachineLearningServices
az provider register -n Microsoft.Storage
az provider register -n Microsoft.KeyVault
az provider register -n Microsoft.ContainerRegistry
```

---

## 4) Create an Azure ML workspace

Pick a region supported by Azure ML (example uses `eastus`).

```bash
# Set variables (bash/zsh)
RG="ai900-rg"
WS="ai900-mlw"
LOC="eastus"

az group create -n "$RG" -l "$LOC"
az ml workspace create -n "$WS" -g "$RG" -l "$LOC"
```

(Optional) Set defaults so you don’t have to pass `-g` and `-w` every time:

```bash
az configure --defaults group="$RG" workspace="$WS"
```

Confirm the workspace:

```bash
az ml workspace show --output table
```

---

## 5) Create compute for jobs

Create a small CPU cluster (this may take a few minutes):

```bash
az ml compute create \
  -n cpu-cluster \
  --type amlcompute \
  --size Standard_DS3_v2 \
  --min-instances 0 \
  --max-instances 2

az ml compute show -n cpu-cluster --output table
```

---

## 6) Submit a simple Azure ML job (command job)

In an empty folder (or a demo folder), create these two files.

### `src/hello.py`

```python
print("Hello from an Azure ML job!")
```

### `hello-mljob.yml`

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
name: hello-ai900
display_name: hello-ai900
experiment_name: ai900-cli

code: ./src
command: python hello.py

environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster
```

Submit the job:

```bash
az ml job create --file hello-mljob.yml --web
```

Track the job (replace the job name/id if needed):

```bash
az ml job list --max-results 10 --output table
az ml job show -n hello-ai900
az ml job stream -n hello-ai900
```

---

## Troubleshooting

- **`az: command not found`**: Azure CLI isn’t installed (or your terminal needs to be restarted).
- **Permission errors** (403/AuthorizationFailed): you don’t have rights to create resources in that subscription/resource group.
- **Region/Quota errors** when creating compute: try a different region, different VM size, or ask for quota increases.
- **Extension issues**: update extensions:

```bash
az extension update -n ml
```
