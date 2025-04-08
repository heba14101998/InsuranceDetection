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

# Create minimal README (optional)
cat > README.md << 'EOL'
# Insurance Detection - MLops Project

## Setup

1. Create conda environment:
```bash
conda env create -n mlops-env -y
pip install -r requirements.txt
conda activate mlops-env
```
2. Run the pipeline:
```bash
python src/data_factory.py
```
EOL