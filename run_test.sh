#!/bin/bash

# Activate the project virtual environment
. ./venv/Scripts/activate

# Execute the test suite
python -m pytest test_app.py

# collect exit code from pytest
# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

# Return exit code 0 if all tests passed, or 1 if something went wrong.
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi