
# Project Blueprint: Insurance Detection
This project aims to build a machine learning pipeline for predicting insurance claims using a dataset of insurance records.

#### **Project Goals**
- Build a machine learning pipeline for predicting insurance claims.
- Implement MLOps best practices for version control, data management, and experiment tracking.
- Deploy the model using Streamlit for easy access and visualization.
- Ensure reproducibility and collaboration through a well-structured project layout.
- Use GitHub Actions for CI/CD to automate testing and deployment.
- Use DVC for data versioning and management.
- Use MLflow for experiment tracking and model management.
- Use Docker for containerization and deployment.

#### **Project Scope**
The project will be structured into four phases:
- **1. Data Preparation**: Load, clean, and preprocess the dataset.
- **2. Model Training**: Train a machine learning model using the preprocessed data.
- **3. Experiment Tracking**: Use MLflow to track experiments, parameters, and metrics.
- **4. Deployment**: Deploy the model using Streamlit for easy access and visualization.

---
## Dataset
- **Data Files**: `data/raw/train.csv`, `data/raw/test.csv`, `data/raw/production.csv`
- **Data Format**: CSV
- **Data Size**: 10,000 records
- **Features**:
  - Categorical: `Gender`, `HasDrivingLicense`, `RegionID`, `Switch`, `PastAccident`, `SalesChannelID`
  - Numerical: `Age`, `VehicleAge`, `AnnualPremium`, `DaysSinceCreated`
- **Target**: `Result`

#### **Data Characteristics**
- **Data Type**: Mixed (categorical and numerical)
- **Missing Values**: data has missing and inconsistancy
- **Outliers**: data has some outliers
- **Columns Descriptions**:
  - `Gender`: Male/Female
  - `HasDrivingLicense`: Yes/No
  - `RegionID`: Identifies the region
  - `Switch`: Switched from an existing plan
  - `PastAccident`: Has had an accident in the past
  - `SalesChannelID`: Identifies the sales channel
  - `Age`: Age of the policyholder
  - `VehicleAge`: Age of the vehicle
  - `AnnualPremium`: Annual premium of the policy
  - `DaysSinceCreated`: Days since the policy was created
  - `Result`: Target variable (0 or 1)

---
## Phase 1:  Create Project Structure
We'll create a well-organized directory structure following MLOps best practices:

```bash
InsuranceDetection/
├── .github/               # GitHub Actions for CI/CD
│   └── workflows/
│       └── cicd.yml
├── data/
│   ├── raw/               # Raw data files (tracked by DVC)
│   │   └── train.csv
│   └── processed/         # Processed data (to be tracked by DVC later)
├── checkpoint/
│   ├── models             # Trained models (tracked by DVC/MLflow)
│   └── preprocessor       # Preprocessing models (tracked by DVC/MLflow)
├── notebooks/             # Jupyter notebooks (optional)
│   └── exploratory_analysis.ipynb
|── artifacts/             # Artifacts (e.g., plots, reports)
|   ├── reports
|   └── figures
├── src/
│   ├── __init__.py
│   ├── base.py
│   ├── data_factory.py
│   ├── prediction.py
│   ├── train.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_base.py
│   ├── test_data_factory.py
│   ├── test_train.py
│   └── test_prediction.py
├── docs/                  # Documentation (optional)
├── logs/                  # Logs (tracked by DVC)
├── mlruns/                # MLflow tracking server (optional)
├── .gitignore             # Git ignore file
├── config.yaml            # Configuration file for the project
├── requirements.txt       # Python dependencies
├── Dockerfile             # Dockerfile for containerization
├── README.md              # Project overview and setup instructions
├── app.py                 # Streamlit app for deployment
```

Let's create essential directories and files using Linux terminal or bash script. This will help us to set up the project structure quickly and efficiently.


### 1. Create Directory Structure and Files
Create essentioal directories and file and minimal README using this bash script **bluprint.sh** file , run it in cmd or powershell.

```bash
#!/bin/bash

# Create main project directory
mkdir -p InsuranceDetection
cd InsuranceDetection

# Create directory structure
mkdir -p .github/workflows \
         data/raw \
         data/processed \
         docs \
         checkpoint/models \
         checkpoint/preprocessor \
         src \
         logs \
         artifacts/figures \
         artifacts/reports \
         tests

# Create empty files
touch .gitignore \
      .dvcignore \
      Dockerfile \
      requirements.txt \
      config.yaml \
      MLproject \
      README.md \
      app.py \
      src/__init__.py \
      src/base.py \
      src/data_fractory.py \
      src/train.py \
      src/prediction.py \
      src/train_pipeline \
      src/utils.py \
      tests/__init__.py \
      tests/test_base.py \
      tests/test_data_fractory.py \
      tests/test_train.py \
      tests/test_prediction.py \
      tests/train_train_pipeline \
      .github/workflows/cicd.yml
```

### 2. Configure `**.gitignore**` file

```plaintext
# Environment
.env
.venv/
venv/
.conda/
.vscode/

# Python
__pycache__/
*.py[cod]

# MLflow
mlruns/

# DVC
.dvc/tmp
.dvc/cache

# Data
data/raw/
data/processed/
checkpoint/

# others
draft/
```
#### 3. Set Up requirements.txt 
We'll create a `requirements.txt` file with the following content:

```plaintext
# Add your project dependencies here
numpy==1.24.4
pandas==2.0.3
scikit-learn==1.3.2
matplotlib==3.7.5
joblib==1.4.2
pyyaml==6.0.2

```

## Phase 2: Machine Learning Pipeline

- **Binary classification:** Insurance Detection

| Class         | Description                                      | Key Methods                                                                                   |
| ------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Base**      | Sets up configuration and logging                | `_read_config`, `_setup_logger`, `setup_mlflow`                                               |
| **DataFactory** | Handles data cleaning and preprocessing          | `data_clean`, `_make_preprocessor`, `fit_preprocessor`, `transform_data`, `save_transformed_data`, `save_preprocessor` |
| **Train**     | Trains the model and evaluates performance       | `train_model`, `evaluate_model`, `save_model`, `load_model`|
| **Prediction** | Makes predictions using the trained model       | ``, ``, ``|
| **Utils**     | Utility functions for logging and configuration  | ``, ``, ``|
| **TrainPipeline** | Main pipeline for training and evaluation     | ``, ``, ``|
| **Test**      | Unit tests for the pipeline                     | `test_data_clean`, `test_train_model`, `test_evaluate_model`, `test_save_model`               |

