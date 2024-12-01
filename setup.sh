#!/bin/bash

# Define the virtual environment directory and requirements file
VENV_DIR="./.venv"
REQUIREMENTS_FILE="./requirements.txt"

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
  echo "Virtual environment already exists at $VENV_DIR."
else
  echo "Virtual environment not found. Creating one at $VENV_DIR..."

  # Create the virtual environment
  python3 -m venv "$VENV_DIR"
  if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment. Ensure Python 3 is installed and accessible."
    exit 1
  fi

  echo "Virtual environment created."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"
if [ $? -ne 0 ]; then
  echo "Failed to activate virtual environment."
  exit 1
fi

# Check if requirements.txt exists
if [ -f "$REQUIREMENTS_FILE" ]; then
  echo "Installing dependencies from $REQUIREMENTS_FILE..."

  # Install dependencies
  pip install -r "$REQUIREMENTS_FILE"
  if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    deactivate
    exit 1
  fi

  echo "Dependencies installed successfully."
else
  echo "No requirements file found at $REQUIREMENTS_FILE. Skipping dependency installation."
fi

# Deactivate the virtual environment
deactivate

echo "Setup complete."
