#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <environment_name>"
    exit 1
fi

# Store the environment name
env_name="$1"

# Create virtual environment
python -m venv "$env_name"

# Deactivate any existing environment
conda deactivate

# Activate the newly created virtual environment
source "$env_name"/bin/activate

# Install requirements
pip install -r requirements.txt
