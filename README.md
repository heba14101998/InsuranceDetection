# Insurance Detection - MLops Project

## Project Details

* **Project Name:** Insurance Detection
* **Project Type:** Machine Learning Binary classification
* **Description:** This project is a machine learning model that detects whether a person has insurance or not based on their demographic and health information.

## Installation and Running

First, create a conda environment with the required packages using:

```bash
conda create --name insurance-env python=3.8
```

Then, activate the environment:

```bash
conda activate insurance-env
```
Next, install the required packages. You can use the `requirements.txt` file provided in the repository:

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Ensure that the raw data files are placed in the `data/raw/` directory.
2. Run the preprocessing script to transform the data:
   ```bash
   python src/data_factory.py
   ```