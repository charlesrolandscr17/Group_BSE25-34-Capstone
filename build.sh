#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install --upgrade pip

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Run tests
python manage.py test

# Fix lint errors
pip install autopep8
autopep8 --in-place --aggressive --aggressive $(find . -name "*.py")

# Check for lint errors
pip install --upgrade flake8 pycodestyle
flake8 .
